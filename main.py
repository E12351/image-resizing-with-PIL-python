# import the necessary packages
# import cv2
 
# # load the image and show it
# image = cv2.imread("jurassic-park-tour-jeep.jpg")
# cv2.imshow("original", image)
# cv2.waitKey(0)

import PIL
from PIL import Image
from PIL import ImageTk
from PIL import ImageEnhance
import os
import glob
import math
import sys

def indices( mylist, value):
    return [i for i,x in enumerate(mylist) if x==value]

def generate_empty_canvas(width, height, color='white'):
    size = (width, height)
    return Image.new('RGB', size, color=color)


if __name__ == "__main__":

    dir_path = os.path.dirname(os.path.realpath(__file__))
    # print dir_path
    saturation = 1.0
    print '\n Recomonded 1.0 and 1.1 \n'
    saturation = raw_input("Please enter saturation increment level : ")
    saturation = float(saturation)

    DIR_Large = str(dir_path) + '\\LargeJPG'
    DIR_Small = str(dir_path) + '\\SmallJPG'
    DIR_1920px = str(dir_path) + '\\1920px_72ppi'
    DIR_Original = str(dir_path) + '\\XLargeTIFF'
    # basewidth = 1920
    # width300 = 3600
    

    # make directory
    file_path = DIR_Large
    directory = os.path.dirname(DIR_Large)

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    file_path = DIR_Small
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    file_path = DIR_Original
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    file_path = DIR_1920px
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    # list all files
    DIR  =  str(dir_path) +'\RAW'
    images = glob.glob(DIR+"\*.TIF")

    number_of_images = len(images)

    
    print 'Number of Images  : '+ str(number_of_images)
    for x in xrange(0,number_of_images):
       
        # print images[x]
        name = str(images[x]).split('\\')
        n = len(name)
        
        nameF = name[n-1]
        print nameF

        imgE = Image.open(images[x])
        converter  = PIL.ImageEnhance.Color(imgE)
        img = converter.enhance(saturation)
        # print 'Hight : '+ str(img.size[1])
        # print 'Width : '+ str(img.size[0])
        # __1920px-------------------------------------------------------------------
        y = [1,2]
        y[0] = abs(float(0) - float(img.size[0]))  # 0 -- width
        y[1] = abs(float(0) - float(img.size[1]))

        # print y
        minS = max(y)
        index = y.index(minS)

        
        if index == 0:
            # print index
            basewidth = 1920
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
            img.save(DIR_1920px+'/'+str(nameF),dpi=(72, 72)) 
            # print 'width : '+str(basewidth)
            # print 'hight : ' + str(hsize)

        if index == 1:
            # print index
            basewidth = 1920
            wpercent = (basewidth/float(img.size[1]))
            hsize = int((float(img.size[0])*float(wpercent)))
            img = img.resize((hsize,basewidth), PIL.Image.ANTIALIAS)
            img.save(DIR_1920px+'/'+str(nameF),dpi=(72, 72)) 
            # print 'width : '+str(basewidth)
            # print 'hight : ' + str(hsize)

        # -------------------------------------------------------------------
        # img = Image.open(images[x])

        x1 = [1,2,3,4]
        # x = [1,2]
        T_FLAG = [0,1,2,3]

        T = [0,1,2,3]
        T[0] = (3600/float(img.size[0]))
        T[1] = (3600/float(img.size[1]))
        T[2] = (5400/float(img.size[0]))
        T[3] = (5400/float(img.size[1]))

        T_FLAG[0] = 0
        T_FLAG[1] = 0
        T_FLAG[2] = 0
        T_FLAG[3] = 0

        # print T
        # T_FLAG = [0,1,2,3]

        if T[0] >= 1:
            T_FLAG[0] = 1
            pass
        if T[1] >= 1:
            T_FLAG[1] = 1
            pass
        if T[2] >= 1:
            T_FLAG[2] = 1
            pass
        if T[3] >= 1:
            T_FLAG[3] = 1
            pass

        x1[0] = abs(float(3600) - float(img.size[0]))  # 0 -- width
        x1[1] = abs(float(3600) - float(img.size[1]))

        x1[2] = abs(float(5400) - float(img.size[0]))
        x1[3] = abs(float(5400) - float(img.size[1]))

        # print T_FLAG
        # minT = min(T_FLAG)
        indexF = indices(T_FLAG, 1)
    

        # print indexF

        try:
            for i in xrange(0,len(indexF)):
                x[indexF[i]] = 99999999
                pass
            pass
        except Exception, e:
            # print e
            pass
        
        # print x1

        minS = min(x1)
        index = x1.index(minS)


        

        # print str(minS) + '   '+str(index)+'  '+str(T_FLAG[0])+'  '+str(T_FLAG[1])+'  '+str(T_FLAG[2])+'  '+str(T_FLAG[3])
        # print str(minS) + '   '+str(index)

        # WIDTH-----------------------------------------
        # if (index == 0) & (T_FLAG[0] == 0):
        if (index == 0):
            basewidth = 3600
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
            # print 'width : '+str(basewidth)
            # print 'hight : ' + str(hsize)

            img.save(DIR_Large+'/'+str(nameF),dpi=(300, 300))

            basewidth = 864
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
            # print 'width : '+str(basewidth)
            # print 'hight : ' + str(hsize)

            img.save(DIR_Small+'/'+str(nameF),dpi=(72, 72)) 
            # print index
            pass

        if (index == 3):
         # & (T_FLAG[3] == 0):
            basewidth = 5400
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
            # print 'width : '+str(basewidth)
            # print 'hight : ' + str(hsize)

            img.save(DIR_Large+'/'+str(nameF),dpi=(300, 300)) 

            basewidth = 1080
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
            # print 'width : '+str(basewidth)
            # print 'hight : ' + str(hsize)

            img.save(DIR_Small+'/'+str(nameF),dpi=(72, 72)) 
            # print index
            pass
        # HIGHT-------------------------------------------------
        if (index == 1):
         # & (T_FLAG[1] == 0):
            # print 'test'
            basewidth = 3600
            wpercent = (basewidth/float(img.size[1]))
            hsize = int((float(img.size[0])*float(wpercent)))
            img = img.resize((hsize,basewidth), PIL.Image.ANTIALIAS)
            # print 'width : '+str(basewidth)
            # print 'hight : ' + str(hsize)

            img.save(DIR_Large+'/'+str(nameF),dpi=(300, 300)) 

            basewidth = 864
            wpercent = (basewidth/float(img.size[1]))
            hsize = int((float(img.size[0])*float(wpercent)))
            img = img.resize((hsize,basewidth), PIL.Image.ANTIALIAS)
            # print 'width : '+str(basewidth)
            # print 'hight : ' + str(hsize)

            img.save(DIR_Small+'/'+str(nameF),dpi=(72, 72)) 
            # print index
            pass
        if (index == 2):
         # & (T_FLAG[2] == 0):
            basewidth = 5400
            wpercent = (basewidth/float(img.size[1]))
            hsize = int((float(img.size[0])*float(wpercent)))
            img = img.resize((hsize,basewidth), PIL.Image.ANTIALIAS)

            # print 'width : '+str(basewidth)
            # print 'hight : ' + str(hsize)

            img.save(DIR_Large+'/'+str(nameF),dpi=(300, 300)) 
            
            basewidth = 1080
            wpercent = (basewidth/float(img.size[1]))
            hsize = int((float(img.size[0])*float(wpercent)))
            img = img.resize((hsize,basewidth), PIL.Image.ANTIALIAS)

            # print 'width : '+str(basewidth)
            # print 'hight : ' + str(hsize)

            img.save(DIR_Small+'/'+str(nameF),dpi=(72, 72)) 
            pass
        # ----------------------------------------------------------------------------------------
        # time.sleep(0.1) # do real work here
        # update the bar
        
        # print '\r'
        print 'Completed ' + str(x) + ' images out of ' + str(number_of_images)
        # sys.stdout.write("\033[K")
        # try:
        #     # canvas = generate_empty_canvas(200, 50)
        #     # img.save('low_quality.jpg', dpi=(72, 72))
        #     # img.save('C:\Users\AnjelDehwings_HP\Desktop\Fiverr\Opencv image resize\high_quality\high_quality.jpg', dpi=(600, 600))
        #     pass

        # except Exception, e:
        #     print e

    # img = Image.open(DIR+"\jurassic-park-tour-jeep.jpg")
    # img_O = img

    
    # im.save("test-600.png", dpi=(50,50) )
    
    # img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
    # img.save('sompic.jpg') 
    # img.show()
    # img_O.show()

    


