import cv2
import os
import sys

def show(image,nm,imgShape,move,imgPause,imgDestroy):
    #print("display image")
    newShape=imgShape

    #print("\n\t image=",image.shape)
    image=cv2.resize(image,(newShape[0],newShape[1]))
    cv2.imshow(nm,image)

    cv2.moveWindow(nm,move[0],move[1])
    if imgPause==1:
        cv2.waitKey()
    elif imgPause>1:
        cv2.waitKey(imgPause)

    if imgDestroy:
        cv2.destroyAllWindows()


def drawLine(p1,p2,image,c=(0,255,0)):

    try:


        # print("\n\t p1=",p1)
        # print("\n\t p2=",p2)

        cv2.line(image,(p1[0],p1[1]),(p2[0],p2[1]),c,3)
    except Exception as e:

        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("\n\t line no::", fname, exc_tb.tb_lineno)
        print("\n\t shape=",image.shape)
        print("\n\t exception in line drawing::",e)


    return image



def drawRect(p1,p2,image):

    try:


        #print("\n\t p1=",p1)
        #print("\n\t p2=",p2)
        cv2.rectangle(image,(p1[0],p1[1]),(p2[0],p2[1]),(0,255,0),1)#,thickness=cv2.cv.CV_FILLED)
        #cv2.line(image,(p1[0],p1[1]),(p2[0],p2[1]),(0,255,0),3)
    except Exception as e:

        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("\n\t line no::", fname, exc_tb.tb_lineno)
        print("\n\t shape=",image.shape)
        print("\n\t exception in line drawing::",e)


    return image

def writeFile(image,path):

    cv2.imwrite(path,image)




