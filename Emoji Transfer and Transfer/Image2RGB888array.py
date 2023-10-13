import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def IMGconvert2HEX(file_name):
    img = cv2.imread(file_name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    f = open(file_name + ".txt", "a")
    if img.shape[0] > 110 or img.shape[1] > 110:
        img_array = np.array(cv2.resize(img, (110, 110), interpolation=cv2.INTER_AREA))
    else:
        img_array = np.array(img)
    f.write('\n{')
    count = 0
    for i in range(img_array.shape[0]):
        f.write('\n')
        for j in range(img_array.shape[1]):
            count += 1
            if count < img_array.shape[0] * img_array.shape[1]:
                f.write('0x%02x%02x%02x' % (tuple(img_array[i][j])) + ', ')
            else:
                f.write('0x%02x%02x%02x' % (tuple(img_array[i][j])) + '\n}')
    f.close()
    cv2.imshow('test', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    cv2.waitKey(1000)



def IMGconvert2DEC(file_name):
    img = cv2.imread(file_name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    f = open(file_name + ".txt", "a")
    if img.shape[0] > 110 or img.shape[1] > 110:
        img_array = np.array(cv2.resize(img, (110, 110), interpolation=cv2.INTER_AREA))
    else:
        img_array = np.array(img)
    f.write('\n{')
    count = 0
    for i in range(img_array.shape[0]):
        f.write('\n')
        for j in range(img_array.shape[1]):
            count += 1
            pixel_list = img_array[i][j]
            if count < img_array.shape[0] * img_array.shape[1]:
                f.write(str(pixel_list[2] + pixel_list[1] * 256 + pixel_list[0] * 65536) + ',')
            else:
                f.write(str(pixel_list[2] + pixel_list[1] * 256 + pixel_list[0] * 65536) + '\n}')
    f.close()
    cv2.imshow('test', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    cv2.waitKey(1000)


IMGconvert2HEX('/Users/mitty/Desktop/arduino.bmp')

# IMGconvert2HEX('/Users/mitty/Desktop/表情设计-01.png')
# IMGconvert2HEX('/Users/mitty/Desktop/表情设计-02.png')
# IMGconvert2HEX('/Users/mitty/Desktop/表情设计-03.png')
# IMGconvert2HEX('/Users/mitty/Desktop/表情设计-04.png')
# IMGconvert2HEX('/Users/mitty/Desktop/表情设计-05.png')
# IMGconvert2HEX('/Users/mitty/Desktop/表情设计-06.png')
# IMGconvert2HEX('/Users/mitty/Desktop/表情设计-07.png')
# IMGconvert2HEX('/Users/mitty/Desktop/表情设计-08.png')
# IMGconvert2HEX('/Users/mitty/Desktop/表情设计-09.png')
# IMGconvert2HEX('/Users/mitty/Desktop/表情设计-10.png')
# IMGconvert2HEX('/Users/mitty/Desktop/表情设计-11.png')
# IMGconvert2HEX('/Users/mitty/Desktop/表情设计-12.png')

'''!!!change the FILENAME !!!'''
# IMGconvert2HEX('FILENAME')
# IMGconvert2DEC('FILENAME')