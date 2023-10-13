import cv2
import numpy as np

def IMGconvert2HEX(file_name):
    img = cv2.imread(file_name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    array = np.array(img)
    f = open(file_name + ".txt", "a")
    if array.shape[0] <= 110 and array.shape[1] <= 110:
        f.write('\n{')
        count = 0
        for i in range(array.shape[0]):
            f.write('\n')
            for j in range(array.shape[1]):
                count += 1
                if count < array.shape[0] * array.shape[1]:
                    f.write('0x%02x%02x%02x' % (tuple(array[i][j])) + ', ')
                else:
                    f.write('0x%02x%02x%02x' % (tuple(array[i][j])) + '\n}')
        f.close()
        cv2.imshow('test', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
        cv2.waitKey(1000)
    else:
        f.write('')


def IMGconvert2DEC(file_name):
    img = cv2.imread(file_name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    array = np.array(img)
    f = open(file_name + ".txt", "a")
    if array.shape[0] <= 110 and array.shape[1] <= 110:
        f.write('\n{')
        count = 0
        for i in range(array.shape[0]):
            f.write('\n')
            for j in range(array.shape[1]):
                count += 1
                pixel_list = array[i][j]
                if count < array.shape[0] * array.shape[1]:
                    f.write(str(pixel_list[2] + pixel_list[1] * 256 + pixel_list[0] * 65536) + ',')
                else:
                    f.write(str(pixel_list[2] + pixel_list[1] * 256 + pixel_list[0] * 65536) + '\n}')
        f.close()
        cv2.imshow('test', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
        cv2.waitKey(1000)



# IMGconvert2HEX('/Users/mitty/Desktop/arduino.bmp')

'''!!!change the FILENAME !!!'''
# IMGconvert2HEX('FILENAME')
# IMGconvert2DEC('FILENAME')