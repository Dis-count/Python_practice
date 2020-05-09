from PIL import Image

#预处理（将图片尺寸压缩，并转为灰度图）
def preprocess(img_path,delta=100):
    img = Image.open(img_path)
    # 获取图片尺寸
    width, height = img.size
    # 获取图片最大边的长度
    if width > height:
        max = width
    else:
        max = height

    # 伸缩倍数scale
    scale = max / delta
    width, height = int(width / scale), int(height / scale)
    img = img.resize((width, height))

    return img
    
