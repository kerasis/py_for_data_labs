# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

def create_img(number, output_path):
    img = Image.new('RGB', (100, 100), color='white')
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, 100, 100], outline='blue', width=5) # рамка
    text = str(number)
    
    text_bbox = draw.textbbox((0, 0), text, font=ImageFont.truetype("verdana.ttf", 30)) #позиционирование цифры
    text_width = text_bbox[2] - text_bbox[0]
    text_height = (text_bbox[3] - text_bbox[1])
    text_position = ((100 - text_width) // 2, (100 - text_height) // 2)

    draw.text(text_position, text, fill="red", font=ImageFont.truetype("verdana.ttf", 30))
    
    img.save(output_path, format="PNG")
    return img

def main():
    imgss = []
    for i in range(1, 4):
        output_path = f"card{i}.png"
        card_img = create_img(i, output_path)
        imgss.append(card_img)
        
    plt.figure(figsize=(5, 2)) #отображение карточек
    for idx, card in enumerate(imgss, start=1):
        plt.subplot(1, 3, idx)
        plt.imshow(card)
        plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
