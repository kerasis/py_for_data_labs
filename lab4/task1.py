from sys import argv
#from pathlib import Path
from moviepy.editor import VideoFileClip

def main():
    if len(argv) == 5:
        path = str(argv[1]) 
        time_start = str(argv[2])
        time_end = str(argv[3])
        result_name = str(argv[4])
    else:
        print("Неверное количество аргументов, требуется: \n \
              1. имя входного файла  \n \
              2. время начала фрагмента hh:mm:ss \n \
              3. время окончания фрагмента hh:mm:ss \n \
              4. имя выходного файла") 
        return

    
    with VideoFileClip(str(path)) as my_clip:
        my_clip.subclip(time_start, time_end).write_videofile(str(result_name))
if __name__ == "__main__":
    main()

