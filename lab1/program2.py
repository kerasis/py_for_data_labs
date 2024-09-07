from argparse import ArgumentParser
from pathlib import Path


def main():
    arg_pars = ArgumentParser()
    arg_pars.add_argument('--dirpath', type=str, default = str(Path.cwd()))
    arg_pars.add_argument('--files', nargs = '+')
    
    args = arg_pars.parse_args()
    path = Path(args.dirpath)
    files_list = args.files
    
    if not path.is_dir():
        print("Dir doesn't exists")
        return
    
    if files_list:
        directory_files = [f.name for f in path.glob('*') if not(f.is_dir())]
        existing_files = [f for f in files_list if f in directory_files]
        missing_files = [f for f in files_list if f not in directory_files]
        
        if existing_files:   
            with open(path/'existingFiles.txt', 'w') as file:
                for f in existing_files:
                    print(f, " exists")
                    file.write(f)
                    
        else: 
            print("There are no files present in the folder")
                
         
        if missing_files:          
            with open(path/'missingFiles.txt', 'w') as file:
                for f in missing_files:
                    print(f, " missing")
                    file.write(f)
            
        else: 
            print("There are no files missing in the folder")
               
                      
    else: 
        print("Directory info:")
        entries = list(path.iterdir())
        
        total_size = sum([i.stat().st_size for i in entries]) / 1024
        
        print(f"Total size of directory: {total_size} Kb")
        print(f"Elements : {[i.name for i in entries]}")
        
   
        
if __name__ == "__main__":
    main()