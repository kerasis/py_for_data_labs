# -*- coding: utf-8 -*-
from argparse import ArgumentParser
from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt


def main():
    arg_pars = ArgumentParser()   #именованные аргументы
    arg_pars.add_argument('-ftype', type=str, default = '.png')
    arg_pars.add_argument('--files', nargs = '+')
    
    args = arg_pars.parse_args()
    files_type = Path(args.ftype)
    files_list = args.files
    
    fixed_size = (50,50)
    
    plt.figure(figsize=(10, 5))
    
    for ind, img_name in enumerate(files_list):
        with Image.open(img_name) as img:
             img.thumbnail(fixed_size)  #изменение размера
             plt.subplot(1, len(files_list), ind + 1) 
             plt.imshow(img)
             plt.title(img_name)
             plt.axis('off')
            
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
