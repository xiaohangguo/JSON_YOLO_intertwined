# JSON_YOLO_intertwined
 COCO JSON 格式 和YOLO 相互转化的代码，包含YOLO2JSON 和JSON2YOLO，在很多数据集上测试有效。



# 文件结构

## YOLO

-images

--train

---*.jpg……

--val

---*.jpg……

--test

---*.jpg……

-labels

--train

---*.txt……

--val

---*.txt……

--test

---*.txt……

## COCO JSON

-2017train

--*.jpg……

-2017val

--*.jpg……

-2017test

--*.jpg……

-annotations

--instances_train.json

--instances_val.json

--instances_test.json

# 使用方法

## YOLO2JSON

修改`yolo_base_folder`  对应存放着 images 和labels 两个文件的根目录。

在我这里是`/public/home/lvshuhang/pea_od/yolov8-main/mydata`

直接执行即可在当前目录得到`instances_train.json` ，`instances_val.json`



## JSON2YOLO_ignore_0

直接执行即可，默认代码是放在COCOdataset 数据集根目录下执行。

程序会跳过标签为0的标签，然后导出标签会-1 ，如果不需要这部分功能需要调整。

这部分是针对公开数据集[SeaDronesSee](https://github.com/Ben93kie/SeaDronesSee)v2开发的。

https://seadronessee.cs.uni-tuebingen.de/dataset



## JSON2YOLO

直接执行即可，默认代码是放在COCOdataset 数据集根目录下执行。
