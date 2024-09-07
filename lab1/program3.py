from sys import argv
from pathlib import Path

def main():
    if len(argv) > 1:
        path = Path(argv[1]) 
    else:
        path = Path.cwd()  
    
    if not path.is_dir():
        print("Dir doesn't exists")
        return
    
    entries = list(path.iterdir())
    if path/'missingFiles.txt' in entries:
        with open(path/'missingFiles.txt', 'r') as file:
            for line in file:
                f = path/line
                f.touch()         
                print(f, ' created')       
    
    else:
        print("There are no missingFiles.txt in the folder")

if __name__ == "__main__":
    main()