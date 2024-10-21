from ultralytics import RTDETR, YOLO
from ultralytics.utils import (ASSETS, DEFAULT_CFG, DEFAULT_CFG_PATH, LINUX, MACOS, ONLINE, ROOT, WEIGHTS_DIR, WINDOWS,
                               checks, is_dir_writeable)
#MODEL ='D:/Experiennces/ultralytics-main/ultralytics-main/ultralytics/yolov8n.pt'
CFG = 'D://Experiennces//ultralytics-main//ultralytics-main//ultralytics//cfg//models//v8//yolov8-CoordAtt-BiFPN.yaml' #自己添加、修改模块后的yaml文件
SOURCE = ROOT / 'assets/bus.jpg'
#如果运行后出现PASSED 说明模块被正常添加


def test_model_forward():
    """Test the forward pass of the YOLO model."""
    model = YOLO(CFG)
    model(SOURCE)  # also test no source and augment
