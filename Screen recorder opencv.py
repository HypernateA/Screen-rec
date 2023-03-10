import pyautogui as pygui
import cv2
import numpy as np
from glob import glob

option = input("#1 Record \n#2 Play \n")

def record_video():
    file_name = str(input("Enter the file name you'd like to save with: "))

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    output = cv2.VideoWriter(file_name + ".avi", fourcc, 15, (1920,1080))

    cv2.namedWindow("Recording", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Recording", 480, 320)
     
    while True:
        img = pygui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        output.write(frame)
        cv2.imshow('Recording', frame)

        t = cv2.waitKey(30)
        if t == ord('q'):
            break

    output.release()
    print("Recording successful")


def play_video():
    videos = glob('*.avi')
    for i, vid in enumerate(videos):
        print("#" + str(i+1), str(vid))

    file = int(input("Choose the file to play: "))
    video = cv2.VideoCapture(videos[file-1])

    cv2.namedWindow(videos[file-1], cv2.WINDOW_NORMAL)
    cv2.resizeWindow(videos[file-1], 960, 640)
    
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        
        cv2.imshow(videos[file-1], frame)

        t = cv2.waitKey(60)
        if t == ord('q'):
            break

    video.release()
    
    

if option == "1":
    record_video()

elif option == "2":
    play_video()

else: print("Enter a valid option next time")    

cv2.destroyAllWindows()


