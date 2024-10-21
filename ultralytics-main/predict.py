from ultralytics import YOLO
import pandas as pd

# 读取模型，这里传入训练好的模型
# model = YOLO('D:/Experiennces/ultralytics-main/usefulresult/新建文件夹/train61-yolov8-BiFPN/weights/best.pt')
model = YOLO('D:/Experiennces/ultralytics-main/usefulresult/train3-v8/train3/weights/best.pt')
# 模型预测，save=True 的时候表示直接保 存yolov8的预测结果
metrics = model.predict('D://Experiennces//yolov8//yolov8//datasets//HanYang+wuhan_10_2755//test//images', save=True,save_conf=True,save_txt=True,conf=0.4)
# metrics = model.predict('D:\Experiennces\yolov8\yolov8\datasets\cug-2', save=True,save_conf=True,save_txt=True,conf=0.18)
# 如果想自定义的处理预测结果可以这么操作，遍历每个预测结果分别的去处理
# for m in metrics:
#     # 获取每个boxes的结果
#     box = m.boxes
#     # 获取box的位置，
#     xywh = box.xywh
#     # 获取预测的类别
#     cls = box.cls
#
#     xyxy = box.xyxy
#
#     print(box, xywh, cls)
