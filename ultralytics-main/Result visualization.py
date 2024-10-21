import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

if __name__ == '__main__':
    # 列出待获取数据内容的文件位置
    # v5、v8都是csv格式的，v7是txt格式的,需要更改的地方：仅为result_dict中的内容，每行表示的是模型名称和该模型训练得到的result文件地址

    result_dict = {
        'yolov8': r'D:\Experiennces\ultralytics-main\usefulresult\train3-v8\train3\results.csv',
        # 'yolov8-GSConv-SlimNeck': r'D:\Experiennces\ultralytics-main\usefulresult\trainGSConv-SlimNeck\results.csv',
        # 'train49-CoordAtt': r'D:\Experiennces\ultralytics-main\usefulresult\train49-CoordAtt\results.csv',
        # 'train47-BiFPN': r'D:\Experiennces\ultralytics-main\usefulresult\train47-BiFPN\results.csv',
        # 'train48-BiFPN-slim': r'D:\Experiennces\ultralytics-main\usefulresult\train48-BiFPN-slim\results.csv',
        # 'train50-BiFPN-CoordAtt': r'D:\Experiennces\ultralytics-main\usefulresult\train50-BiFPN-CoordAtt\train50\results.csv',
        # 'trainGSConv-SlimNeck': r'D:\Experiennces\ultralytics-main\usefulresult\trainGSConv-SlimNeck\results.csv',
        # 'yolov8':r'D:\Experiennces\ultralytics-main\usefulresult\train62-yolov8\results.csv',
        'yolov8-BiFPN-CoordAtt-200': r'D:\Experiennces\ultralytics-main\usefulresult\train51-BiFPN-CoordAtt-200\train51\results.csv',
        'yolov8-GSConv-SlimNeck':r'D:\Experiennces\ultralytics-main\usefulresult\train61-yolov8-GSConv-SlimNeck\results.csv',
        'yolov8-ADown':r'D:\Experiennces\ultralytics-main\usefulresult\train61-yolov8-ADown\results.csv',
        'yolov8-BiFPN':r'D:\Experiennces\ultralytics-main\usefulresult\train61-yolov8-BiFPN\results.csv',
        'yolov8-BiFPN-slim':r'D:\Experiennces\ultralytics-main\usefulresult\train61-yolov8-BiFPN-slim\results.csv',
        'yolov8-CoordAtt':r'D:\Experiennces\ultralytics-main\usefulresult\train61-yolov8-CoordAtt\results.csv',
        'yolov8-GSConv-SlimNeck':r'D:\Experiennces\ultralytics-main\usefulresult\trainGSConv-SlimNeck\results.csv',
        'yolov8-RepNcs':r'D:\Experiennces\ultralytics-main\usefulresult\train60--RepNcs\train60\results.csv',
        'yolov8-coordatt-bifpn-siou':r'D:\Experiennces\ultralytics-main\usefulresult\train61-coordatt-bifpn-siou\results.csv'

    }

    # 绘制map50
    for modelname in result_dict:
        res_path = result_dict[modelname]
        ext = res_path.split('.')[-1]
        if ext == 'csv':
            data = pd.read_csv(res_path, usecols=[6]).values.ravel()    # 6是指map50的下标（每行从0开始向右数）
        else:   # 文件后缀是txt
            with open(res_path, 'r') as f:
                datalist = f.readlines()
                data = []
                for d in datalist:
                    data.append(float(d.strip().split()[10]))   # 10是指map50的下标（每行从0开始向右数）
                data = np.array(data)
        x = range(len(data))
        plt.plot(x, data, label=modelname, linewidth='1')   # 线条粗细设为1

    # 添加x轴和y轴标签
    plt.xlabel('Epochs')
    plt.ylabel('mAP@0.5')
    plt.legend()
    plt.grid()
    # 显示图像
    plt.savefig("mAP50.png", dpi=600)   # dpi可设为300/600/900，表示存为更高清的矢量图
    plt.show()


    # 绘制map50-95
    for modelname in result_dict:
        res_path = result_dict[modelname]
        ext = res_path.split('.')[-1]
        if ext == 'csv':
            data = pd.read_csv(res_path, usecols=[7]).values.ravel()    # 7是指map50-95的下标（每行从0开始向右数）
        else:
            with open(res_path, 'r') as f:
                datalist = f.readlines()
                data = []
                for d in datalist:
                    data.append(float(d.strip().split()[11]))   # 11是指map50-95的下标（每行从0开始向右数）
                data = np.array(data)
        x = range(len(data))
        plt.plot(x, data, label=modelname, linewidth='1')

    # 添加x轴和y轴标签
    plt.xlabel('Epochs')
    plt.ylabel('mAP@0.5:0.95')
    plt.legend()
    plt.grid()
    # 显示图像
    plt.savefig("mAP50-95.png", dpi=600)
    plt.show()

    # 绘制训练的总loss
    for modelname in result_dict:
        res_path = result_dict[modelname]
        ext = res_path.split('.')[-1]
        if ext == 'csv':
            box_loss = pd.read_csv(res_path, usecols=[1]).values.ravel()
            obj_loss = pd.read_csv(res_path, usecols=[2]).values.ravel()
            cls_loss = pd.read_csv(res_path, usecols=[3]).values.ravel()
            data = np.round(box_loss + obj_loss + cls_loss, 5)    # 3个loss相加并且保留小数点后5位（与v7一致）

        else:
            with open(res_path, 'r') as f:
                datalist = f.readlines()
                data = []
                for d in datalist:
                    data.append(float(d.strip().split()[5]))
                data = np.array(data)
        x = range(len(data))
        plt.plot(x, data, label=modelname, linewidth='1')

    # 添加x轴和y轴标签
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid()
    # 显示图像
    plt.savefig("loss.png", dpi=600)
    plt.show()
