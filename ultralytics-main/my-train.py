from ultralytics import YOLO

# 加载一个模型
model = YOLO('D://Experiennces//ultralytics-main//ultralytics-main//ultralytics//cfg//models//v8//yolov8-CoordAtt-BiFPN.yaml')  # 从YAML建立一个新模型
model = YOLO('D://Experiennces//ultralytics-main//ultralytics-main//ultralytics//yolov8n.pt')  # 加载预训练模型（推荐用于训练）
model = YOLO('yolov8-CoordAtt-BiFPN.yaml').load('yolov8n.pt')  # 从YAML建立并转移权重

# 训练模型
# if __name__ == '__main__':
results = model.train(data='D://Experiennces//ultralytics-main//ultralytics-main//ultralytics//cfg//datasets//streeview2.yaml', epochs=200)
result = model.val()
    # yolo predict model=D:/Experiennces/ultralytics-main/usefulresult/train51-BiFPN-CoordAtt-200/train51/weights/best.pt source=D:/Experiennces/yolov8/yolov8/datasets/cug