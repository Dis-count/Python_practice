def img2char(img_obj, savepath):
    txt = ''
    width, height = img_obj.size
    # 获取像素点的rgb元组值，如(254, 0, 0)，并将其转化为字符
    for i in range(height):
        line = ''
        for j in range(width):
            line += rgb2char(*img_obj.getpixel((j, i)))
        txt = txt + line + '\n'

    # 保存字符画
    with open(savepath, 'w+', encoding='utf-8') as f:
        f.write(txt)



img_obj = preprocess(img_path)
img2char(img_obj, savepath)     
