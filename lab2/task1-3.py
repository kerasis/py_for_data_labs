# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
from sys import argv
import matplotlib.pyplot as plt
import numpy as np

def show_image_and_channels(image_path): #task1
    with Image.open(image_path) as img:
        r, g, b = img.split()   #каналы R, G, B
        fig, axes = plt.subplots(1, 4, figsize=(16, 5)) # сетка для отображения изображений

        axes[0].imshow(img)                     #отображаем спектры
        axes[0].set_title("Original Image")
        axes[0].axis('off')  
        
        axes[1].imshow(r, cmap='Reds')
        axes[1].set_title("Red Channel")
        axes[1].axis('off')
        
        axes[2].imshow(g, cmap='Greens')
        axes[2].set_title("Green Channel")
        axes[2].axis('off')
    
        axes[3].imshow(b, cmap='Blues')
        axes[3].set_title("Blue Channel")
        axes[3].axis('off')

        plt.show()

def most_common_channel(image_path): #task2 
    with Image.open(image_path) as img:
        r, g, b = img.split()     #split разделяет изображение на слои которые мы можем представить как двумерные массивы np
        sum_rgb = [np.sum(np.array(r)), np.sum(np.array(g)), np.sum(np.array(b))]
        print(f"color intensity:  red -  {sum_rgb[0]}, green - {sum_rgb[1]}, blue - {sum_rgb[2]}.")
        
        if sum_rgb[0] > sum_rgb[1] and sum_rgb[0] > sum_rgb[2]:
            most_common_c = 'red'
        if sum_rgb[1] > sum_rgb[0] and sum_rgb[1] > sum_rgb[2]:
            most_common_c = 'green'
        if sum_rgb[2] > sum_rgb[1] and sum_rgb[2] > sum_rgb[0]:
            most_common_c = 'blue'
        if sum_rgb[0] == sum_rgb[1]:
            most_common_c = 'red and green'
        if sum_rgb[0] == sum_rgb[2]:
            most_common_c = 'red and blue'
        if sum_rgb[2] == sum_rgb[1]:
            most_common_c = 'blue and green'
        print(f"Most common channel(s) - {most_common_c}")
        return most_common_c

def add_watermark(image_path, watermark_path, output_path):  #task3
    with Image.open(image_path).convert("RGBA") as img: #конвертим в ргба 
        with Image.open(watermark_path).convert("RGBA") as watermark:
            watermark = watermark.resize((int(img.size[0] * 0.3), int(img.size[1] * 0.3)))

            # меняем прозрачность 
            watermark_with_alpha = watermark.copy()
            alpha = watermark_with_alpha.split()[3]  
            alpha = alpha.point(lambda p: p * 0.7)  # прозрачность 70%
            watermark_with_alpha.putalpha(alpha)

            img_w, img_h = img.size # позиционирование
            watermark_w, watermark_h = watermark_with_alpha.size
            position = (img_w - watermark_w - 20, img_h - watermark_h - 20)  

            # текст
            txt_overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(txt_overlay)
            font = ImageFont.truetype("verdana.ttf", 100)  
            text = "watermark"
            draw.text((20,20), text, font=font, fill=(255, 0, 255, 128))  

            # объединяем
            out_img = Image.new('RGBA', img.size, (0, 0, 0, 0))
            out_img.paste(img, (0, 0)) 
            out_img.paste(watermark_with_alpha, position, mask=watermark_with_alpha) 
            out_img = Image.alpha_composite(out_img, txt_overlay)  

            out_img.save(output_path, format="PNG")
            plt.imshow(out_img)
            plt.axis('off')
            plt.show()
        


def main():
    if len(argv) > 1:         
        file_path = str(argv[1]) 
    else:
        file_path = 'kitti.jpg'
    watermark_path = 'dog.png'   
    #show_image_and_channels(file_path)
    #most_common_channel(file_path)
    add_watermark(file_path, watermark_path, 'outImg.png')    
    

    
if __name__ == "__main__":
    main()
    




