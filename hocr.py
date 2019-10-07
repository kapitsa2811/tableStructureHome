import cv2
import os
from PIL import Image
#import commands

# ('tesseract ' + pathName + '/' + filename + ' -  -psm 0')


#/home/kapitsa/PycharmProjects/objectLocalization/wsl/tableStructure/newImages/train
filePath="./newImages/train//"
#filePath="./newImages/test//"
filePath1="./newImages/trainHocr//"
#filePath1="./newImages/testHocr//"

for indx,img in enumerate(os.listdir(filePath)):

    in1=filePath+img
    image=cv2.imread(in1)
    #image2=Image.open(in1)

    #print("\n\t info=",image2.info['dpi'])
    #print(image2.info['dpi'])
    print("\n\t indx:",indx,"\t img",img)
    out1=filePath1+img+".txt"

    os.system(" ".join(["tesseract ",in1," ",out1," ","-psm 11","-l eng"," hocr"]))
    #os.system(" ".join(["tesseract ",in1," ",out1," ","-psm 11"," hocr"]))
    #os.system(" ".join(["tesseract",in1,out1," hocr"," psm-- 11"]))
    #cv2.imwrite(filePath1+img,255-image)


    if indx>10:
        break
    #input("check")