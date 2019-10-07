'''
    line segmentation
'''

# processCordinates_22Intermediate.py on github

import copy
import os
import pandas as pd
import cv2
import sys
from visualize import *
from copy import deepcopy
import configProcessCordinates

cwd=os.getcwd()+"//"

yStart=0
yDict={}


'''
    for all files present in folder
'''

cor = pd.DataFrame(columns=["fileName","word", "0", "1", "2", "3", "4", "5", "6", "7", "8", "table"])
cor1 = pd.DataFrame(columns=["fileName","word", "0", "1", "2", "3", "4", "5", "6", "7", "8", "table"])



def getWords(fileName1,image3,curtLineNo,currentCor,wordCorLine,wordIndx,wordLine,cor,cor1,wordFeatureIndx,cuLinePrev,cuLineNext):

        try:
            #print("\n\t\t this gives near words")
            showFlag = 0
            x1,x2=currentCor[0],currentCor[2]
            y1,y2=currentCor[1],currentCor[3]

            '''
                table coordinate from original file
            '''
            #annot1 = annot[annot["fileName"] == fileName]
            #print("\n\t annot1:\n\t",[annot1["x1"],annot1["y1"],annot1["x2"],annot1["y2"]])

            #print("\n\t type=",type(annot1["x1"]))
            #print("\n\t annot1:\n\t",annot1["x1"].values[0])
            # print("\n\t annot1:\n\t",annot1["y1"][1])
            # print("\n\t annot1:\n\t",annot1["x2"][1])
            # print("\n\t annot1:\n\t",annot1["y1"][1])
            #input("check")

            forWord=wordLine[curtLineNo][wordIndx]

            '''
                table related code
            '''

            #t,oriX, oriY, oriX1, oriY1=tableInsert(fileName1,image11,cor,currentCor,annot1,wordFeatureIndx,forWord)

            '''
                table drawing
            '''
            '''
            cv2.rectangle(image11, (oriX, oriX1), (oriY, oriY1), (0, 0, 255), 5)

            if t >= 0:
                 print("\n\t t=",t)
                 cor.loc[wordFeatureIndx, "table"] = 1
                 cv2.rectangle(image11, (currentCor[0], currentCor[1]), (currentCor[2], currentCor[3]), (0, 255, 0), 2)
                 #cv2.rectangle(image11, (currentCor[0], currentCor[2]), (currentCor[1], currentCor[3]), (0, 0, 255), 5)


                 #cv2.rectangle(image11, (oriX1, oriY1), (oriX, oriY), (0,255,0), 5)
                 #cv2.rectangle(image11, (oriX, oriX1), (oriY, oriY1), (0,0, 255), 5)
                 #cv2.rectangle(image11, (oriX, oriY), (oriX1, oriY1), (0,0, 255), 5)
                 #print("\n\t t=", t)
                 #input("t")
                 name=str(str(currentCor[0])+"\t"+ str(currentCor[1])+"\t"+str(currentCor[2])+"\t"+ str(currentCor[3])+"\t")
                 #plot(image11, name)

            else:
                 cor.loc[wordFeatureIndx, "table"] = 0

            #print("\n\t t=>>>", t)
            '''
            overlapFlag=0

            cor.loc[wordFeatureIndx,"word"]=forWord

            '''
                current word coordinate
            '''
            cor.loc[wordFeatureIndx,"0"]=[x1,y1,x2,y2]
            cor1.loc[wordFeatureIndx,"0"]=forWord
            #cor.loc[wordFeatureIndx,"table"]=1

            # print("\n\t\t 2.current word coordinate:",currentCor)
            # print("\n\t\t 2.current word:",wordLine[curtLineNo][wordIndx])
            # print("\n\t\t 2.current line no:",curtLineNo)
            # print("\n\t\t 2.last line dict=",wordLine[curtLineNo-1])

            # try:
            #     print("\n\t\t 2.next line dict=",wordLine[curtLineNo+1])
            # except Exception as e:
            #     pass

            lastWord,nextWord="",""

            '''
                gathers last line neccessary features
            '''


            #drawRect([currentCor[0],currentCor[1]], [currentCor[2],currentCor[3]], image11)

            for indx1,val1 in enumerate(wordCorLine[curtLineNo-1]):

                p0, p1, p2, p3, p4, p5, p6, p7, p8, p9 = None, None, None, None, None, None, None, None, None, None
                p0, p1, p2,p8=currentCor,currentCor,currentCor,currentCor
                p0,p6,p2 = currentCor,cuLinePrev,cuLineNext
                #print("***********************************************************")
                #image3=image11 #copy.deepcopy(image11)
                image11=copy.deepcopy(image3)
                byWord=wordLine[curtLineNo-1][indx1]
                nextWord, prevWord = "", ""
                #print("\n\t val1=",val1)

                allTemp=val1
                #print("\n\t allTemp=",allTemp)

                xTemp1,xTemp2=allTemp[0],allTemp[2]
                yTemp1,yTemp2=allTemp[1],allTemp[3]

                if yTemp1 >=y1 or yTemp1 >=y2 or yTemp2 >=y1 or yTemp2 >=y2 :
                    break

                if xTemp1<=x2 and xTemp2>x2:
                    #print("\n\t overlap 1")
                    overlapFlag =1

                elif xTemp2>=x1 and xTemp1<=x1:
                    #print("\n\t overlap2")
                    overlapFlag =2
                elif xTemp1>=x1 and x2>=xTemp2:
                    #print("\n\t overlap4")
                    overlapFlag = 4

                elif x2>=xTemp1 and x2<=xTemp1:
                    #print("\n\t overlap5")
                    overlapFlag = 5


                if overlapFlag>0:

                    overlapFlag1=copy.deepcopy(overlapFlag)
                    # print("\n\t 2.word x1:",x1,"\t 2.x2:",x2)
                    # print("\n\t 2.overlap word xTemp1:",xTemp1,"\t 2.xTemp2:",xTemp2)
                    # print("\n\t 2.flag=",overlapFlag)
                    #cv2.rectangle(image3,(xTemp2, yTemp2), (xTemp1, yTemp1),(0, 255, 0), 5)
                    #cv2.rectangle(image3,(x1, y1), (x2, y2),(255,0, 0), 5)
                    #cv2.line(image3,(x1,y1),(x2,y2), (0, 0, 255), 3)

                    #cv2.line(image3,(xTemp2,yTemp2),(xTemp1,yTemp1), (0, 0, 255), 3)
                    #cv2.line(image3,(x1,y1),(xTemp2,yTemp2), (0, 255,0), 5)
                    #ims=cv2.resize(image3,(700,700))
                    overlapFlag=0
                    #print("\n\t forWOrd-",str(forWord),"\t byWord-",str(byWord))
                    name=str(forWord)+"_"+str(byWord)+"_"+str(nextWord)+"_"+str(prevWord)

                    '''
                        above word coordinate
                    '''

                    cor.loc[wordFeatureIndx, "8"] = [xTemp1, yTemp1, xTemp2, yTemp2]
                    cor1.loc[wordFeatureIndx, "8"] = byWord

                    p8=[xTemp1, yTemp1, xTemp2, yTemp2]
                    p1,p7=p8,p8

                    # print("\n\t 0.wordCorLine::>", len(wordCorLine[curtLineNo - 1]))
                    # print("\n\t 1.wordCorLine::>", len(wordCorLine[curtLineNo - 1][indx1 - 1]))
                    # print("\n\t 2.wordCorLine:", len(wordCorLine[curtLineNo - 1][indx1]))

                    '''
                        gathers last line previous word features
                        indx1 is index of above word coordinate
                    '''
                    if indx1 > 0:
                        prevCord = wordCorLine[curtLineNo - 1][indx1 - 1]
                        xTempL0, xTempL1 = prevCord[0], prevCord[2]
                        yTempL0, yTempL1 = prevCord[1], prevCord[3]
                        #print("\n\t above prev=", prevCord)
                        prevWord = wordLine[curtLineNo - 1][indx1 - 1]
                        #print("\n\t above prevWord =", prevWord)

                        '''
                            above left word coordinate
                        '''
                        cor.loc[wordFeatureIndx, "7"] = [xTempL0, yTempL0, xTempL1, yTempL1]
                        cor1.loc[wordFeatureIndx, "7"] = prevWord
                        p7=prevCord

                    elif indx1 == 0:
                        # cor.loc[wordFeatureIndx, "7"] = [0,0,0,0]
                        # cor1.loc[wordFeatureIndx, "7"] = [0,0,0,0]
                        cor.loc[wordFeatureIndx, "7"] = p7
                        cor1.loc[wordFeatureIndx, "7"] = p7

                        '''
                            if 1st word no previous coordinate exists so above word is made previous coordimnate
                        '''
                        p7=p8

                    '''
                        gathers last line next word features
                        condition makes sure next word exists and above word is not the last word
                    '''

                    if (indx1 + 1) < len(wordCorLine[curtLineNo - 1]):
                        nextCord = wordCorLine[curtLineNo - 1][indx1 + 1]
                        xTempR1, xTempR2 = nextCord[0], nextCord[2]
                        yTempR1, yTempR2 = nextCord[1], nextCord[3]
                        #print("\n\t nextCord=", nextCord)

                        # nextCord=wordCorLine[curtLineNo - 1][indx1+1]

                        nextWord = wordLine[curtLineNo - 1][indx1 + 1]
                        #print("\n\t nextWord =", nextWord)

                        '''
                            above right word coordinate
                        '''
                        p1=[xTempR1, yTempR1, xTempR2, yTempR2]
                        cor.loc[wordFeatureIndx, "1"] = [xTempR1, yTempR1, xTempR2, yTempR2]
                        cor1.loc[wordFeatureIndx, "1"] = nextWord

                    elif (indx1) == len(wordCorLine[curtLineNo - 1]):

                        # cor.loc[wordFeatureIndx, "1"] = [10000, 10000, 10000, 10000]
                        # cor1.loc[wordFeatureIndx, "1"] = [10000, 10000, 10000, 10000]

                        cor.loc[wordFeatureIndx, "1"] = p1
                        cor1.loc[wordFeatureIndx, "1"] = p1

                        '''
                            if next word do not exist then next word is current word
                        '''
                        p1=p8

                    '''
                        above word next and previous word line drawing
                    '''

                    dp0p8,dp7p8,dp8p1=None,None,None
                    dp0p4,dp5p4,dp4p3=None,None,None

                    #if (abs(p0[0]-p8[0])<=15 and abs(p2[0]-p1[0])<=15) and (abs(p0[0]-p2[0]) == abs(p8[0]-p1[0])):


                    print("\n\t abs(p0[0]-p8[0])=",abs(p0[0]-p8[0]),"\t abs(p2[0]-p1[0])=",abs(p2[0]-p1[0]))
                    if  ((abs(p0[0]-p8[0])<=20 and abs(p2[0]-p1[0])<=20)) :#or ((abs(p0[2]-p8[2])<=20 and abs(p2[2]-p1[2])<=20)): #or ((abs(p0[2]-p8[2])<=20 and abs(p2[2]-p1[2])<=20)):
                        drawLine(p0, p8, image3, (255, 255, 255))
                        drawLine(p1, p2, image3, (255, 255, 255))
                        drawLine(p8, p1, image3,(255,255,255))
                        drawLine(p0, p2, image3,(255,255,255))
                        drawLine(p0, p1, image3, (255, 255, 255))
                        #drawLine(p2, p8, image3, (255, 255, 255))
                        #cv2.rectangle(image3, (p1[2], p1[3]), (p0[0], p0[1]), (0, 255, 0),thickness=cv2.FILLED)  # ,thickness=cv2.cv.CV_FILLED)
                        showFlag = 0
                        #print("\n  p0=",p0,"\t p1=",p1)
                        #print("\n  p0=",p0,"\t p1=",p1)
                        image3[p0[1]:p1[1],p0[0]:p1[1]]=255
                        #drawRect(p0,p1)
                        showFlag=1
                    #cv2.line(image3, (p0[0], p0[1]), (p0[2], p0[3]), (0,255,0), 1)
                    #drawLine(p0, p1, image3,(0,0,255))
                    #drawLine(p0, p7, image3,(255,0,0))
                    #drawLine(p0, p8, image3,(0,0,255))


                    try:
                        print("\n\t p0=",p0,"\t ",abs(p0[0]-p8[0]))
                        print("\n\t p8=",p8)
                        print("\n\t p1=",p1,"\t ",abs(p2[0]-p1[0]))
                        print("\n\t p2=",p2)

                        #cv2.rectangle(image11, (p1[2], p1[3]), (p0[0], p0[1]), (0, 255, 0),3)  # ,thickness=cv2.cv.CV_FILLED)
                        cv2.rectangle(image11, (p0[0], p0[1]), (p1[0], p1[1]), (0, 255, 0),3)  # ,thickness=cv2.cv.CV_FILLED)
                        cv2.rectangle(image11, (p8[0], p8[1]), (p2[0], p2[1]), (0, 0, 255),3)  # ,thickness=cv2.cv.CV_FILLED)
                        cv2.circle(image11, (p1[0], p1[1]),5, (0, 0, 255), -1)
                        cv2.circle(image11, (p2[0], p2[1]),5, (0, 255, 255), -1)
                        show(255-image11,str([str(abs(p0[0]-p8[0])),str(abs(p2[0]-p1[0]))]),[700,900],[700,0],1,1)

                    except Exception as e:
                          input("check coordinates")
                          pass

                    #plot(image11, name)
                    break
                else:
                    print("^^^^^^^^^^^^^^^^")
                    print("\n\t abs(p0[0]-p8[0])=",abs(p0[0]-p8[0]),"\t abs(p2[0]-p1[0])=",abs(p2[0]-p1[0]))
                    print("******************")
                    # drawLine(p2, p0, image3, (255, 0, 0))
                    # drawLine(p8, p0, image3, (0, 0, 255))
            '''
                next line features
            '''

            ### disable strart

            # for indx1,val1 in enumerate(wordCorLine[curtLineNo+1]):
            #
            #     allTemp=val1
            #     xTemp1,xTemp2=allTemp[0],allTemp[2]
            #     yTemp1,yTemp2=allTemp[1],allTemp[3]
            #
            #     '''
            #         below word coordinate
            #     '''
            #     cor.loc[wordFeatureIndx, "4"] =[xTemp1,yTemp1,xTemp2,yTemp2]
            #
            #     # print("\n\t 00.wordCorLine::>",len(wordCorLine[curtLineNo + 1]))
            #     # print("\n\t 11.wordCorLine::>",len(wordCorLine[curtLineNo + 1][indx1-1]))
            #     # print("\n\t 22.wordCorLine:",len(wordCorLine[curtLineNo + 1][indx1]))
            #
            #     #
            #     # if yTemp1 >=y1 or yTemp1 >=y2 or yTemp2 >=y1 or yTemp2 >=y2 :
            #     #     break
            #
            #     # print("\n\t rule 1:",xTemp1<=x2 and xTemp2>x2)
            #     # print("\n\t rule 2:",xTemp2>=x1 and xTemp1<=x1)
            #     # print("\n\t rule 3:",xTemp1>=x1 and xTemp2>=x2)
            #     # print("\n\t rule 4:",xTemp1>=x1 and x2>=xTemp2)
            #     # print("\n\t rule 5:",x2>=xTemp1 and x2<=xTemp1)
            #
            #     if xTemp1<=x2 and xTemp2>x2:
            #         #print("\n\t overlap 1")
            #         overlapFlag =1
            #
            #     elif xTemp2>=x1 and xTemp1<=x1:
            #         #print("\n\t overlap2")
            #         overlapFlag =2
            #     elif xTemp1>=x1 and x2>=xTemp2:
            #         #print("\n\t overlap4")
            #         overlapFlag = 4
            #
            #     elif x2>=xTemp1 and x2<=xTemp1:
            #         #print("\n\t overlap5")
            #         overlapFlag = 5
            #
            #     if overlapFlag > 0:
            #         # print("\n\t 2.word x1:",x1,"\t 2.x2:",x2)
            #         # print("\n\t 2.overlap word xTemp1:",xTemp1,"\t 2.xTemp2:",xTemp2)
            #         #print("\n\t 2.flag=",overlapFlag)
            #         #cv2.rectangle(image3, (xTemp2, yTemp2), (xTemp1, yTemp1), (0, 255, 0), 5)
            #         #cv2.rectangle(image3, (x1, y1), (x2, y2), (255, 0, 0), 5)
            #         #cv2.line(image3, (x1, y1), (x2, y2), (0, 0, 255), 3)
            #         #cv2.line(image3, (xTemp2, yTemp2), (xTemp1, yTemp1), (0, 0, 255), 3)
            #         #cv2.line(image3, (x1, y1), (xTemp2, yTemp2), (255, 255, 0), 5)
            #         #ims = cv2.resize(image3, (700, 700))
            #
            #         # print("\n\t forWOrd-",str(forWord),"\t byWord-",str(byWord))
            #         # cv2.imshow(str(forWord) + "_" + str(byWord) + "_" + str(nextWord) + "_" + str(prevWord), ims)
            #         # cv2.moveWindow(str(forWord) + "_" + str(byWord) + "_" + str(nextWord) + "_" + str(prevWord), 100, 100)
            #         # cv2.waitKey()
            #         #plot(image3,name)
            #         overlapFlag = 0
            #         #cv2.destroyAllWindows()
            #
            #         '''
            #             gathers next line previous word
            #         '''
            #
            #         if indx1 > 0:
            #             prevCord = wordCorLine[curtLineNo + 1][indx1 - 1]
            #             xTempL0, xTempL1 = prevCord[0], prevCord[2]
            #             yTempL0, yTempL1 = prevCord[1], prevCord[3]
            #             #print("\n\t prev below line=", prevCord)
            #             prevWord = wordLine[curtLineNo + 1][indx1 - 1]
            #             #print("\n\t prevWord =", prevWord)
            #
            #             '''
            #                 above left word coordinate
            #             '''
            #             cor.loc[wordFeatureIndx, "5"] = [xTempL0, yTempL0, xTempL1, yTempL1]
            #             cor1.loc[wordFeatureIndx, "5"] = prevWord
            #
            #         elif indx1==0:
            #
            #             cor.loc[wordFeatureIndx, "5"] = [0,0,0,0]
            #             cor1.loc[wordFeatureIndx, "5"] = [0,0,0,0]
            #
            #
            #         '''
            #             next line next word
            #         '''
            #         if (indx1 + 1) < len(wordCorLine[curtLineNo + 1]):
            #             nextCord = wordCorLine[curtLineNo + 1][indx1 + 1]
            #             xTempR1, xTempR2 = nextCord[0], nextCord[2]
            #             yTempR1, yTempR2 = nextCord[1], nextCord[3]
            #             #print("\n\t nextCord=", nextCord)
            #             nextWord = wordLine[curtLineNo + 1][indx1 + 1]
            #             #print("\n\t nextWord =", nextWord)
            #
            #             '''
            #                 above right word coordinate
            #             '''
            #             cor.loc[wordFeatureIndx, "3"] = [xTempR1, yTempR1, xTempR2, yTempR2]
            #             cor1.loc[wordFeatureIndx, "3"] = nextWord
            #
            #
            #         elif indx1 == len(wordCorLine[curtLineNo + 1]):
            #             cor.loc[wordFeatureIndx, "3"] = [10000,10000,10000,10000]
            #             cor1.loc[wordFeatureIndx, "3"] = [10000,10000,10000,10000]
            #
            #return image

            ### disable ends

            if 0:#showFlag==1:
                show(255-image3, str([str(abs(p0[0]-p8[0])),str(abs(p2[0]-p1[0]))]), [700, 900], [100, 0], 1, 1)
                showFlag=0
            return cor,cor1,wordFeatureIndx,image3
        except Exception as e:
            print("\n\t exception in getWords:",e)
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("\n\t line no::", fname, exc_tb.tb_lineno)
            #input("exception in getWords")



def lineSegmentation(df1,fileName1,cor,cor1):

    #try:
    wordCorLine={} # this store line level word cordinate information
    wordLine={}
    lineSegment={}
    #print("\n\t this segments line")
    threshold=10
    #image = cv2.imread(cwd+"//images//" + fileName1)
    image = cv2.imread(imagePath + fileName1)
    #hocrImage = copy.deepcopy(image)

    #image1 = cv2.imread(cwd+"//image//" + fileName1)
    lastX,lastY=None,None
    lastX2,lastY2=None,None
    startX,startY=None,None
    lineCount=0
    countWords=0
    w=""
    tempWord = []# stores actual word
    tempWordCord=[] # stores actual word cordinate for single line
    totWordProcess=0 # no of words processed by line segmentation module

    #df=pd.DataFrame(columns=["fileName","x1","y1","x11","y11","lineNo","table"])


    '''
        line segmentation
    '''
    for rowNo, row in df1.iterrows():

        #print("\n\t rowNo:",rowNo,"\t line count=",lineCount)

        #print("\n\t 1.line no:",lineCount)
        # print("\n\t\t 1.word no from csv:",countWords)
        # print("\n\t\t 1.word=",df1.loc[rowNo,"word_1"])

        cuX,cuY= int(df1.loc[rowNo, 'x1']), int(df1.loc[rowNo,'y1'])
        cuX2,cuY2= int(df1.loc[rowNo, 'x2']), int(df1.loc[rowNo,'y2'])
        # midX,midY=(cuX+cuX2)/2,(cuY+cuY2)/2 ## current cell mid coordinate
        # currentCor=[cuX,cuY,cuX2,cuY2]

        w = df1.loc[rowNo, "word_1"]

        #print("\n\t cuX:",cuX,"\t cuY:",cuY)

        '''
            current line begining
        '''
        if countWords==0:
            startX, startY = cuX, cuY
            lastX,lastY=startX, startY

        if countWords==0 and rowNo==0:
            lastX,lastY=startX, startY

        '''
            word line
        '''
        #cv2.line(image, (cuX, cuY), (cuX2, cuY2), (0, 0, 255), 3)

        #cv2.putText(hocrImage,str(rowNo),(cuX2, cuY),cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,255))#, lineType=cv2.LINE_AA
        #hocrImage=drawRect((cuX, cuY), (cuX2, cuY2),hocrImage)
        #print("\n\t ",abs(cuY-lastY)>threshold,"\t abs(cuY-lastY):",abs(cuY-lastY))

        if abs(cuY-lastY)>threshold:

            wordCorLine[lineCount] = tempWordCord
            totWordProcess=totWordProcess+len(tempWordCord)
            tempWordCord=[]
            tempWordCord.append([cuX,cuY,cuX2,cuY2])
            lineSegment[lineCount]=[startX, startY,lastX2,lastY2]

            '''
                entire row line segment
            '''
            #cv2.line(image, (startX, startY), (lastX2,lastY2), (255, 0, 0), 3)

            countWords=0

            #print("\n\t cuY=",cuY,"\t lastY=",lastY)
            #winname = str(w)+"_"+str(int(abs(cuY - lastY)))

            '''
                puts all words in last line to dictionary
            '''
            wordLine[lineCount]=tempWord
            #print("\n\t wordLine[lineCount]=",wordLine[lineCount])
            #print("\n\t last line co-ordinate:",wordCorLine[lineCount])

            tempWord=[]
            tempWord.append(df1.loc[rowNo, "word_1"])

            #drawLine((startX, startY), (lastX2,lastY2),image)

            #show(image, "lineMap", [500, 500], [0, 0], 1, 1)

            startX, startY = cuX, cuY
            lineCount+=1
        else:

            try:
                w = w + "\t " + str(df1.loc[rowNo, "word_1"])
            except Exception as e:
                w=w
            tempWord.append(df1.loc[rowNo, "word_1"])
            #tempLastLineWords[df1.loc[rowNo, "word_1"]]=[cuX,cuY,cuX2,cuY2]
            try:

                #wordCorLine[lineCount]=[cuX,cuY,cuX2,cuY2]
                tempWordCord.append([cuX,cuY,cuX2,cuY2])

                #drawLine((cuX,cuY), (cuX2,cuY2), image)

                #show(image, "wordMap", [500, 500], [500, 0], 100, 1)

                #xTemp11,yTemp11=xTemp1,yTemp1
            except Exception as e:
                pass

        lastX, lastY = cuX,cuY
        lastX2, lastY2 = cuX2,cuY2
        countWords+=1


    '''
        inserts last line on page not working
    '''
    # lineCount += 1
    # wordCorLine[lineCount] = tempWordCord

    totWordProcess = totWordProcess + len(tempWordCord)

    #cv2.imwrite(delmePath+"hocr_"+fileName1,image)
    #show(hocrImage,"hocrMap",[500,500],[0,0],1,1)

    # print("\n\t keys:",len(wordCorLine.keys()),"\t df1.shape:",df1.shape,"\t rowNo:",rowNo)
    #input("no of keys")

    '''
        extracts co-ordinate level features for each coordinate present in wordCorLine
    '''
    cor,cor1=cordinateProcessing(fileName1,image,wordCorLine,wordLine,cor,cor1)

    #print("\n\t ###################################################",image.shape)

    return cor,cor1,totWordProcess
    # except Exception as e:
    #     print("\n\t inside line segmentation error")
    #     exc_type, exc_obj, exc_tb = sys.exc_info()
    #     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #     print("\n\t exception location:---->", exc_tb.tb_lineno)


def cordinateProcessing(fileName1,image,wordCorLine,wordLine,cor,cor1):

    #print("\n\t inside cordinateProcessing")

    '''
    wordImage=copy.deepcopy(image)
    lineImage=copy.deepcopy(image)
    pageImage=copy.deepcopy(image)
    '''
    try:

        wordFeatureIndx = cor.shape[0]
        totLineCount=len(wordCorLine)

        for curtLineNo in wordCorLine:
            curLineWordCount=len(wordCorLine[curtLineNo])
            # print("\n\t Line no from dictionary=",curtLineNo,"\t total lines=",len(wordCorLine))
            # print("\n\t value:",wordCorLine[curtLineNo])
            # print("\n\t number of word cordinates:",len(wordCorLine[curtLineNo]))
            # print("\n\t allWords in current line=",wordLine[curtLineNo])
            # print("\n\t number of word=",len(wordLine[curtLineNo]))

            '''
                requires previous line co-ordinates so below condition
            '''

            #print("\n\t lineNo:--->",curtLineNo)

            for wordIndx,currentCor1 in enumerate(wordCorLine[curtLineNo]):
                #image11 = image

                cuLinePrev,cuLineNext="",""
                cor,cor1=initialize(cor, cor1, wordFeatureIndx,fileName1)

                '''
                    adds the previous words if 1st word then hard code
                '''

                if wordIndx == 0:
                    cuLinePrev =currentCor1  #wordCorLine[curtLineNo][wordIndx]#[0,0,0,0]

                else:
                    #cuLinePrev=wordCorLine[curtLineNo][wordIndx-1] # previous word
                    cuLinePrev=wordCorLine[curtLineNo][wordIndx-1]
                #p9=cuLinePrev
                # wordImage=drawLine(wordCorLine[curtLineNo][wordIndx],cuLinePrev,wordImage)
                # show(wordImage,"Prev_wordImage",[500,500],[700,0],200,1)

                #print("\n\t cuLinePrev=",cuLinePrev)
                cor.loc[wordFeatureIndx, "6"] = cuLinePrev
                #print("\n\t cuLineNext =",cuLineNext)

                '''
                    last word in the line
                '''

                if (wordIndx+1) < curLineWordCount:
                    cuLineNext = wordCorLine[curtLineNo][wordIndx + 1]
                    cor.loc[wordFeatureIndx, "2"] = cuLineNext
                    # print("\n\t cuLineNext =",cuLineNext)

                    #wordImage = drawLine(wordCorLine[curtLineNo][wordIndx], cuLineNext, wordImage)
                    #show(wordImage, "Next_wordImage", [500, 500], [50, 0], 200, 1)

                elif (wordIndx+1) == curLineWordCount:
                    cor.loc[wordFeatureIndx, "2"] = wordCorLine[curtLineNo][wordIndx]
                    cuLineNext=currentCor1
                '''
                    not the 1st or last line
                '''
                if (curtLineNo + 1) < totLineCount and curtLineNo > 0:
                #if (wordIndx)<(len(wordCorLine[curtLineNo])) and  (curtLineNo+1)<(len(wordCorLine)) and curtLineNo>0 :
                #wordIndx<(len(wordCorLine[curtLineNo])) and  (curtLineNo+1)<(len(wordCorLine)): #
                    '''
                        for last word next set to high
                    '''
                    if wordIndx == (curLineWordCount-1):
                        #cor.loc[wordFeatureIndx, "2"] = [100000, 100000, 100000, 100000]
                        cor.loc[wordFeatureIndx, "2"] = wordCorLine[curtLineNo][wordIndx]
                    # else:
                    #     cuLineNext =wordCorLine[curtLineNo][wordIndx+1]
                    #     cor.loc[wordFeatureIndx, "2"] = cuLineNext
                    #     #print("\n\t cuLineNext =",cuLineNext)
                    #
                    #     wordImage=drawLine(wordCorLine[curtLineNo][wordIndx],cuLineNext,wordImage)
                    #     show(wordImage,"wordImage",[500,500],[0,0],200,1)

                    wordWidth,wordHeight=abs(cuLinePrev[1]-cuLinePrev[3]),abs(cuLinePrev[0]-cuLinePrev[2])
                    if wordWidth>10 and wordHeight>10:
                        cor,cor1,wordFeatureIndx,image111=getWords(fileName1,image, curtLineNo, currentCor1, wordCorLine,wordIndx,wordLine,cor,cor1,wordFeatureIndx,cuLinePrev,cuLineNext)
                    #plot(image111,str(wordFeatureIndx))

                    wordFeatureIndx+=1
                elif curtLineNo==0 or (curtLineNo+1)==totLineCount: #(len(wordCorLine)): # this should handle 1st and last line
                    #print("1st and last line handling")

                    if curtLineNo==0:
                        cor.loc[wordFeatureIndx, "1"] = currentCor1 #[0,0, 0, 0]
                        cor.loc[wordFeatureIndx, "7"] = currentCor1#[0,0, 0, 0]
                        cor.loc[wordFeatureIndx, "8"] = currentCor1 #[100000, 100000, 100000, 100000]
                    elif (curtLineNo+1)== totLineCount :#(len(wordCorLine)):
                        cor.loc[wordFeatureIndx, "3"] = currentCor1#[0,0, 0, 0]
                        cor.loc[wordFeatureIndx, "4"] = currentCor1#[0,0, 0, 0]
                        cor.loc[wordFeatureIndx, "5"] = currentCor1#[100000, 100000, 100000, 100000]

                    if wordIndx == (curLineWordCount-1):
                        cor.loc[wordFeatureIndx, "2"] = currentCor1#[100000, 100000, 100000, 100000]
                    else:
                        cuLineNext =wordCorLine[curtLineNo][wordIndx+1]
                        cor.loc[wordFeatureIndx, "2"] = cuLineNext
                        #print("\n\t cuLineNext =",cuLineNext)

                    #del image11

            #show(lineImage,"lineImage",[500,500],[0,0],1,1)
    except Exception as e1:
        print("\n\t e1=",e1)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("\n\t exception location inside  cordinateProcessing2:---->", exc_tb.tb_lineno)

        input("exception2:")
    try:
        cv2.imwrite(writePath+ fileName1,image111)
        del image111
    except Exception as e:
        pass

    return cor,cor1



def initialize(cor,cor1,wordFeatureIndx,fileName1):


    cor.loc[wordFeatureIndx, "fileName"] = fileName1
    cor.loc[wordFeatureIndx, "0"] = [0, 0, 0, 0]
    cor.loc[wordFeatureIndx, "1"] = [0, 0, 0, 0]
    cor.loc[wordFeatureIndx, "2"] = [0, 0, 0, 0]
    cor.loc[wordFeatureIndx, "3"] = [0, 0, 0, 0]

    cor.loc[wordFeatureIndx, "4"] = [0, 0, 0, 0]
    cor.loc[wordFeatureIndx, "5"] = [0, 0, 0, 0]
    cor.loc[wordFeatureIndx, "6"] = [0, 0, 0, 0]
    cor.loc[wordFeatureIndx, "7"] = [0, 0, 0, 0]
    cor.loc[wordFeatureIndx, "8"] = [0, 0, 0, 0]

    return cor,cor1


def tableInsert(fileName1,image11,cor,currentCor,annot1,wordFeatureIndx,forWord):

    t=0
    try:
        #print("inside 1")

        from shapely.geometry import Polygon
        #print("inside 2")
        x1, x2 = currentCor[0], currentCor[2]
        y1, y2 = currentCor[1], currentCor[3]
        #print("inside 3")

        #print("\n\t ------>",annot1.values[0][0])


        '''
            table coordinates
        '''

        oriX, oriY, oriX1, oriY1 = annot1.values[0][2], annot1.values[0][3], annot1.values[0][4], annot1.values[0][5]
        #print("inside 4")
        #print("\n\t co-ordinates:",oriX, oriY, oriX1, oriY1 )
        #print("\n\t x1=",x1)


        # if (x1>oriX and x1<oriX1 and x2>oriX and x2<oriX1 ):
        #     if (y1<oriY and y1>oriY1 and y2<oriY1 and y2>oriY1):
        #         t=1
        # else:
        #     t=0

        if (x1>oriX and x1<oriX1) and (y1>oriY and y1<oriY1):
            if (x2>oriX and x2<oriX1) and (y2>oriY and y2<oriY1):
                t=1
                print("\n\t fileName=",fileName1)
                print("\n\t rectangle:",(oriX, oriY),"\t",(oriX1, oriY1))
                print("\n\t coordinate:",(x1, y1),"\t",(x2, y2))
                print("\n\t word in table:",forWord)
                #input("rectangle")
        else:
            t=-1
        # a = Polygon([(oriX, oriY), (oriX1, oriY), (oriX1, oriY1), (oriX, oriY1)])
        # b = Polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y1)])

        #t = a.intersection(b).area / a.union(b).area
    except Exception as e:

        print("\n\t e:",e)
        import sys
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("\n\t line no::", fname, exc_tb.tb_lineno)
        input("exception")

    return t,oriX, oriY, oriX1, oriY1

#imagePath=cwd+"//images//"
#imagePath="./newImages/train//"


## test
# imagePath="/home/kapitsa/PycharmProjects/objectLocalization/wsl/tableStructure/publicationData/8/test//"
# writePath="/home/kapitsa/PycharmProjects/objectLocalization/wsl/tableStructure/delMe2//"

## train

# imagePath="//home/kapitsa/PycharmProjects/objectLocalization/wsl/tableStructure/publicationData/8/train/tableInvert//"
# writePath="/home/kapitsa/PycharmProjects/objectLocalization/wsl/tableStructure//delMe3//"

imagePath=configProcessCordinates.imagePath
writePath=configProcessCordinates.writePath

# imagePath="/home/kapitsa/PycharmProjects/objectLocalization/wsl/tableStructure/publicationData/8/train//tableInvert4//"
# writePath="/home/kapitsa/PycharmProjects/objectLocalization/wsl/tableStructure//delMe4//"

#annotateFilePath="./csv//train.csv"
#annotateFilePath="./csv//out2.csv"
#annotateFilePath="./csv//trainOut.csv"

annotateFilePath=configProcessCordinates.annotateFilePath
annot=pd.read_csv(annotateFilePath)
df=annot

for fileIndx,fileName in enumerate(os.listdir(imagePath)):

    #print("\n\t imagePath=",imagePath)
    #print("\n\t is file:",os.path.isfile(imagePath+fileName))

    if os.path.isfile(writePath+fileName):
        print("\n\t file already processed:",fileName)
        #input("pause")
        continue

    print("\n\t fileIndx:",fileIndx,"\t fileName:",fileName)

    #df1 = df[df["fileName"] == fileName]

    df1 = df[df["fileName"].str.strip() == fileName]
    #print("\n\t df1=",df1.shape)
    #input("check")
    df1.reset_index(inplace=True)

    #try:

    oldCorShape=cor.shape

    if df1.shape[0]<=1:
        print("\n\t fileName",fileName)
        #input("check ")

    cor,cor1,totWordProcess=lineSegmentation(df1,fileName,cor,cor1)
    newCorShape=cor.shape

    '''
    print("\n\t 2.oldCorShape=",oldCorShape,"\t newCorShape=",newCorShape)
    print("\n\t lines adde:",newCorShape[0]-oldCorShape[0])
    print("\n\t df1 shape=",df1.shape)
    print("\n\t tempWordCord=",totWordProcess)
    '''
    newCorShape =oldCorShape
    #input("shape")
    # except Exception as e:
    #     print("\n\t Exception in lineSegmentation:",e)
    #
    #     exc_type, exc_obj, exc_tb = sys.exc_info()
    #     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #     print("\n\t Exception in for loop:::", fname, exc_tb.tb_lineno)
    #     #input("exception in getWords")
    #     pass



    cor.to_csv(cwd+"//csv//feature.csv")
    cor1.to_csv(cwd+"//csv//feature1.csv")
    #cv2.imwrite(cwd+"//featureImage//"+fileName1+".png",image11)


