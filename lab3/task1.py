from skimage import io, transform, color, filters, exposure
#import matplotlib.pyplot as plt
from sys import argv
from pathlib import Path
import random 
import numpy as np

def choose_option():
    print("какие преобразования вы хотите применить: \n \
          1.Поворот \n \
          2.Искажения цвета \n \
          3.Повышение резкости/размытости \n \
          4.Удаление информации \n \
          5.Отзеркаливание по горизонтали/вертикали \n \
          6.Комплексное из модуля transform \n \
          7.Выйти")
    n = int(input("Выбранная опция: "))
    return n

def normalize_image(image): # фикс ошибок размерности выходных изображений после трансформаций
    if image.ndim == 2:
        return image
    elif image.ndim == 3:
        if image.shape[2] == 3 or image.shape[2] == 4:
            return image[:, :, :3] 
        elif image.shape[2] == 2:
            return np.stack([image[:, :, 0], image[:, :, 1], (image[:, :, 0] + image[:, :, 1]) / 2], axis=-1)
        else:
            return image[:, :, :3]
    else:
        return color.gray2rgb(image[:, :, 0])

#######################     6 пункт     ######################
def complex_transform(image):
    transformations = [
        transform.rescale,       # масштаб
        transform.rotate,        # поворот
        transform.warp,          # просто трансформация
        transform.swirl,         # скручивание
        transform.resize,        # изменение размера
    ]
    transf = random.choice(transformations)
    
    match transf:
        case transform.rescale:
            new_image = transf(np.array(image), random.uniform(0.5, 2.0))
  
        case transform.rotate:
            new_image =  transf(np.array(image), random.uniform(1, 359))
        
        case transform.warp:
            new_image =  transf(np.array(image), transform.AffineTransform(scale=(random.uniform(0.8, 1.2), random.uniform(0.8, 1.2))))
            
        case transform.swirl:
            strength = random.uniform(0, 2)
            radius = random.uniform(50, 200)
            new_image =  transf(np.array(image), strength=strength, radius=radius)
            
        case transform.resize:
            new_image =  transf(np.array(image), (random.randint(100, 300), random.randint(100, 300)))
            
    return new_image  

def apply_complex_transformations(image_collection, n = 5):  
    transformed_images = [complex_transform(image) for image in image_collection]
    normalized_images = [normalize_image(img) for img in transformed_images]
    if n > 1:
        for i in range(n-1):
           transformed_images = [complex_transform(image) for image in transformed_images]
           normalized_images = [normalize_image(img) for img in transformed_images]
    return normalized_images


#######################     1 пункт     ######################
def rotation(image):
    new_image =  transform.rotate(np.array(image), random.uniform(1, 359))
    return new_image 

def apply_rotation(image_collection):
    transformed_images = [rotation(image) for image in image_collection]
    normalized_images = [normalize_image(img) for img in transformed_images]
    return normalized_images


#######################     2 пункт     ######################
def change_color(image, color_variations):
    match color_variations:    
        case 'hsv':
            return color.rgb2hsv(image)
        case 'lab':
            return color.rgb2lab(image)
        case 'yuv':
            return color.rgb2yuv(image)
        case 'gray':
            return color.rgb2gray(image)
    
def apply_color_changes(image_collection):
    color_variations = ['hsv', 'lab', 'yuv', 'gray']
    transformed_images = []
    
    for image in image_collection:
        color = random.choice(color_variations)
        transformed_image = change_color(image, color)
        if color == 'gray': # тк двйхканальный добавим еще 1 канал
            transformed_image = np.stack([transformed_image] * 3, axis=-1) 
        transformed_image = np.clip(transformed_image, 0, 1) # диапазон допустимых цветовых значений 
        transformed_images.append(transformed_image)
        
    return transformed_images


#######################     3 пункт     ######################
def sharpness_blur(image, method):
    if image.ndim == 3:  # проверка на ргб
        channel_axis = -1
    else: 
        channel_axis = None
     
    match method:
        case 'blur':
            processed_image = filters.gaussian(image, sigma=4.0, channel_axis=channel_axis)
        case 'sharp':
            processed_image = filters.unsharp_mask(image, radius=1, amount=1)
    
     # иногда возникают проблемы связанные с контрастом, фиксим экспозицию
    processed_image = exposure.rescale_intensity(processed_image, in_range='image', out_range=(0, 1))
    if exposure.is_low_contrast(processed_image):
        processed_image = exposure.equalize_adapthist(processed_image)
    
    return processed_image
        

def apply_sharpness_blur(image_collection):
    transformed_images = [sharpness_blur(image, random.choice(['sharp', 'blur'])) for image in image_collection]
    return transformed_images


#######################     4 пункт     ######################
def del_info(image):
    height, width, _ = image.shape
    max_square_area = int(0.15 * height * width) # площадь квадрата будет не более 15% от общей площади картинки
    square_side = random.randint(1, int(np.sqrt(max_square_area)))
    top_left_x = random.randint(0, height - square_side)
    top_left_y = random.randint(0, width - square_side)
    image[top_left_x:top_left_x + square_side, top_left_y:top_left_y + square_side] = [0, 0, 0] # заменяем на черный   
    return image

def apply_del_info(image_collection):
    transformed_images = [del_info(image) for image in image_collection]
    return transformed_images


#######################     5 пункт     ######################
def mirror_image(image, axis='horizontal'):   
    if axis == 'horizontal':
        mirrored_image = np.flipud(image)
    elif axis == 'vertical':
        mirrored_image = np.fliplr(image)

    return mirrored_image

def apply_mirror_image(image_collection):
    transf_variations = ['horizontal', 'vertical']
    transformed_images = []
    
    for image in image_collection:
        transformed_image = mirror_image(image,  random.choice(transf_variations))
        transformed_images.append(transformed_image)
        
    return transformed_images


def get_max_image_number(file_collection):
    numbers = []
    for f in file_collection:
        try:       
            number = int(Path(f).stem)  
            numbers.append(number)
        except ValueError:
            pass 
    return max(numbers) if numbers else -1  

def save_new_images(path, image_collection, max_number):
    for im in image_collection:     
        if im.dtype == np.float32 or im.dtype == np.float64: # сохраняет только uint8
            if np.max(im) <= 1.0:  
                im = im * 255

        im_uint8 = np.clip(im, 0, 255).astype(np.uint8)
        max_number += 1
        filename = f'{max_number:04d}.jpg'  # именz файла с 4 цифрами
        io.imsave(path / filename, im_uint8)
    return max_number

def main():
    
    if len(argv) > 1:
        path = Path(argv[1])
    else:
        path = Path.cwd() / 'plates' / 'train' / 'cleaned'      # для отладки, в идеале всегда при вызове файла указываем путь до конкретной папки.
 
    if not path.is_dir():
        
        print("Dir doesn't exists:", path)
        return
    print(path)
    file_collection = [str(f) for f in path.glob('*.jpg')]
    image_collection = io.imread_collection(file_collection)
    
    flag = True
    max_number = get_max_image_number(file_collection)
    
    while flag:      
        option = choose_option()
        new_collection = []
        
        match option:
            case 1:
                new_collection = apply_rotation(image_collection)
            case 2:
                new_collection = apply_color_changes(image_collection)
            case 3:
                new_collection = apply_sharpness_blur(image_collection)
            case 4:
                new_collection = apply_del_info(image_collection)
            case 5:
                new_collection = apply_mirror_image(image_collection)
            case 6:
                new_collection = apply_complex_transformations(image_collection)
            case 7: 
                flag = False
        if new_collection:     
            max_number = save_new_images(path, new_collection, max_number)
        
    
    
if __name__ == "__main__":
    main()