import os
from PIL import Image

def remove_white_background(image_path, output_path):
    image = Image.open(image_path)
    image = image.convert("RGBA")
    
    datas = image.getdata()
    newData = []
    for item in datas:
        # 设置颜色的阈值，如果是白色或者接近白色，就设置为透明
        if item[0] > 200 and item[1] > 200 and item[2] > 200:  # 颜色阈值可能需要调整
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    
    image.putdata(newData)
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))
    image.save(output_path, "PNG")

def process_images_in_directory(directory):
    supported_formats = ['.jpg', '.jpeg', '.png']
    for filename in os.listdir(directory):
        if os.path.splitext(filename)[1].lower() in supported_formats:
            file_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, 'png', os.path.splitext(filename)[0] + '.png')
            remove_white_background(file_path, output_path)

# 从当前目录开始处理图片
current_directory = os.getcwd()
process_images_in_directory(current_directory)
