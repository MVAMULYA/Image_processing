import cv2 as cv
import numpy as np
import math

### set of images with different resulutions are called image pyramids

def get_highest_powerOf_2(num):
    '''get to the highest power of 2 less than or equal to the number   
        so that when the image resolution is brought down and up to get gaussian pyramids,
        they are equal and there occurs no rounding loss when calculating Laplacian pyramids.
    '''
    power = int(math.log(num,2))
    return int(pow(2,power))

if __name__ == "__main__":
    orange =cv.imread('orange flower.jpg')
    purple = cv.imread('purple flower.jpg')

    if orange.shape < purple.shape:
        dim = (get_highest_powerOf_2(orange.shape[1]),get_highest_powerOf_2(orange.shape[0]))
        purple = cv.resize(purple,dim,interpolation=cv.INTER_AREA)
        orange = cv.resize(orange,dim,interpolation=cv.INTER_AREA)
    else:
        dim = (get_highest_powerOf_2(purple.shape[1]),get_highest_powerOf_2(purple.shape[0]))
        orange = cv.resize(orange,dim,interpolation=cv.INTER_AREA)
        purple = cv.resize(purple,dim,interpolation=cv.INTER_AREA)

    # create Guassian Pyramids
    ga = orange.copy()
    gb = purple.copy()
    gpA = [ga]
    gpB = [gb]

    for i in range(6):
        ga = cv.pyrDown(ga)
        gpA.append(ga)
        gb = cv.pyrDown(gb)
        gpB.append(gb)

    # create Laplacian pyramid
    
    lpA = [gpA[5]]
    lpB = [gpB[5]]
    for i in range(5,0,-1):
        gau = cv.pyrUp(gpA[i])
        lp = cv.subtract(gpA[i-1],gau)
        lpA.append(lp)
        gbu = cv.pyrUp(gpB[i])
        lp = cv.subtract(gpB[i-1],gbu)
        lpB.append(lp)

    Ls = []
    for la,lb in zip(lpA,lpB):
        rows,cols,dpt = la.shape
        ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))
        Ls.append(ls)
    ls_ = Ls[0]
    for i in range(1,6):
        ls_ = cv.pyrUp(ls_)
        ls_ = cv.add(ls_,Ls[i])

    direct = np.hstack((orange[:,:cols//2], purple[:,cols//2:]))

    cv.imwrite('Pyramid blending.jpg',ls_)
    cv.imwrite('Direct blending.jpg', direct)
    py = cv.imread("Pyramid blending.jpg")
    dr = cv.imread("Direct blending.jpg")
    cv.imshow('Pyramid Blending',py)
    cv.imshow('Diresct Blending',dr)
    cv.waitKey(0)
    cv.destroyAllWindows()

