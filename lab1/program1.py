from sys import argv
from pathlib import Path
from shutil import copy


def main():
    if len(argv) > 1:
        path = Path(argv[1]) 
    else:
        path = Path.cwd()  
    
    if not path.is_dir():
        print("Dir doesn't exists")
        return
    
    files_list = [f for f in path.glob('*') if not(f.is_dir())]  
    for f in files_list:
        print("File: ", f.name," Size: ", f.stat().st_size/1024, "Kb")
        
    small_files = [f for f in files_list if f.stat().st_size/1024 < 2]
    
    if small_files:
        small_dir = path / "small"
        small_dir.mkdir(exist_ok=True)
        print("Dir for small files if done")
        for file in small_files:
            copy(file, small_dir / file.name)
            print(file.name, "copied")
    else:
        print("This path hasn't small files")
        
if __name__ == "__main__":
    main()