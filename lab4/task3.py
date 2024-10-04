from sys import argv
import cv2

def main():
    if len(argv) > 1:
        path = str(argv[1])
    else:
        print("Enter the path!")
        return
    
    vid =  cv2.VideoCapture(path)
    fps = vid.get(cv2.CAP_PROP_FPS)
    name = path.split('/')[-1]
         
    while vid.isOpened():
        ret, frame = vid.read()
        if not ret:
            print("End")
            break
        cv2.putText(frame, f'File: {name}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)   
        cv2.putText(frame, f'FPS: {fps:.2f}', (10, 70),  cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)   
        cv2.imshow('sss', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'): # прерываем на q (добавление задержки между катдрами посогает избежать серого окна с загрузкой....)
            break


    vid.release()
    cv2.destroyAllWindows()
                
if __name__ == "__main__":
    main()        
