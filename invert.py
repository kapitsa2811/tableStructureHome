import cv2
import os


filePath="./newImages/train1//"
filePath1="./newImages/train1//"
for indx,img in enumerate(os.listdir(filePath)):

    in1=filePath+img
    image=cv2.imread(in1)
    print("\n\t indx:",indx,"\t img",img)
    #out1=filePath1+img+".txt"

    #os.system(" ".join(["tesseract",in1,out1,"hocr"]))
    cv2.imwrite(filePath1+img,255-image)
