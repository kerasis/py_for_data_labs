from sys import argv
#from pathlib import Path
from moviepy.editor import VideoFileClip
from PIL import Image

def main():
    if len(argv) == 5 or len(argv) == 6:
        path = str(argv[1]) 
        time_start = str(argv[2])
        time_end = str(argv[3])
        result_name =  str(argv[4])
        if len(argv) == 6:
            step = int(argv[5])   #step шаг в секундах
        else:
            step = 10
    else:
        print("Неверное количество аргументов, требуется: \n \
              1. имя входного файла  \n \
              2. время начала фрагмента hh:mm:ss \n \
              3. время окончания фрагмента hh:mm:ss \n \
              4. путь для записи кадров  \n \
              5. шаг извлечения кадров(не обязательно)") 
        return

    new_dir = result_name
    new_dir.mkdir(exist_ok=True)
    
    with VideoFileClip(str(path)) as my_clip:
        sub_clip = my_clip.subclip(time_start, time_end)
        picture_number = 0
        
        for i in range(0, int(sub_clip.duration), step):
            picture = sub_clip.get_frame(i) 
            image = Image.fromarray(picture)    
            image_resized = image.resize((250, int(image.height * 250 / image.width)))
            output_path = new_dir / f"{picture_number}.png"
            image_resized.save(output_path)
          
            picture_number += 1
            
        

if __name__ == "__main__":
    main()

