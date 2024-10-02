import matplotlib.pyplot as plt
from sys import argv
from pathlib import Path
from skimage import exposure
from PIL import Image
import matplotlib.gridspec as gridspec
import numpy as np

def show_histogram(image_path):
    with Image.open(image_path) as image:       
        image_np = np.array(image)
        fig = plt.figure(figsize=(10, 6))
        gs = gridspec.GridSpec(4, 2, width_ratios=[2, 1]) 

        ax_main = plt.subplot(gs[:, 0])  
        ax_main.set_title("Image")
        ax_main.imshow(image_np)
        ax_main.axis('off')  

       #pillow
        ax_hist = plt.subplot(gs[0, 1])  
        ax_hist.set_title("Mixed Histogram")
        colors = ('r', 'g', 'b')
        for i, color in enumerate(colors):
            ax_hist.hist(image_np[:, :, i].ravel(), bins=256, color=color, alpha=0.6) #ravel преобразует в одномерный массив(из двумерного массива пикселей)
        
        #skimage
        for i, color in enumerate(colors):
            cur_pl = plt.subplot(gs[i+1, 1]) 
            hist, bins = exposure.histogram(image_np[:, :, i], nbins=256)
            cur_pl.plot(bins, hist, color=color, label=f'{colors[i]} channel')

       
        plt.tight_layout()
        plt.show()

def main():
    if len(argv) > 1:
        path = Path(argv[1])
    else:
        path = Path.cwd() / '0001.jpg'  

    show_histogram(path)


if __name__ == "__main__":
    main()
