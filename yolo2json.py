import glob
import json
import os
from PIL import Image

def yolo_to_coco_for_subset(yolo_images_folder, yolo_labels_folder, categories):
    # Initialize COCO dataset structure for the subset
    coco_format = {
        "images": [],
        "annotations": [],
        "categories": []
    }

    # Add category information
    for i, category in enumerate(categories):
        coco_format["categories"].append({
            "id": i + 1,
            "name": category,
            "supercategory": "none"
        })

    image_id = 0
    annotation_id = 0

    for image_file in glob.glob(f"{yolo_images_folder}/*.jpg"):
        # Read image to get width and height
        with Image.open(image_file) as img:
            width, height = img.size

        # Add image information with size
        coco_format["images"].append({
            "id": image_id + 1,
            "file_name": os.path.basename(image_file),
            "width": width,
            "height": height
        })

        # Corresponding annotation file
        yolo_annotation_file = os.path.join(yolo_labels_folder, os.path.basename(image_file).replace(".jpg", ".txt"))
        if os.path.exists(yolo_annotation_file):
            with open(yolo_annotation_file, "r") as file:
                for line in file:
                    category_id, x_center, y_center, bbox_width, bbox_height = map(float, line.split())

                    # Convert YOLO format to COCO format
                    x_min = (x_center - bbox_width / 2) * width
                    y_min = (y_center - bbox_height / 2) * height
                    coco_bbox_width = bbox_width * width
                    coco_bbox_height = bbox_height * height

                    # Add annotation information
                    coco_format["annotations"].append({
                        "id": annotation_id + 1,
                        "image_id": image_id + 1,
                        "category_id": int(category_id) + 1,
                        "bbox": [x_min, y_min, coco_bbox_width, coco_bbox_height],
                        "area": coco_bbox_width * coco_bbox_height,
                        "segmentation": [],  # Optional
                        "iscrowd": 0
                    })
                    annotation_id += 1
        image_id += 1

    return coco_format

def save_coco_format(coco_format, output_file):
    with open(output_file, "w") as file:
        json.dump(coco_format, file, indent=4)

# Example usage
yolo_base_folder = "/public/home/lvshuhang/pea_od/yolov8-main/mydata"
categories = ["pea"]

# Convert train set
train_coco_format = yolo_to_coco_for_subset(
    os.path.join(yolo_base_folder, "images/train"),
    os.path.join(yolo_base_folder, "labels/train"),
    categories
)
save_coco_format(train_coco_format, "instances_train.json")

# Convert val set
val_coco_format = yolo_to_coco_for_subset(
    os.path.join(yolo_base_folder, "images/val"),
    os.path.join(yolo_base_folder, "labels/val"),
    categories
)
save_coco_format(val_coco_format, "instances_val.json")
