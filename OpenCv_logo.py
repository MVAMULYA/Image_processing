
import cv2
import numpy as np

def drawing_functions():
    '''
    '''
    img = np.zeros((512,512,3),np.uint8)
    img = cv2.circle(img,(256,128),40,(0,0,255),30)
    pts = np.array([[256,128],[216,188],[296,188]],np.int32)
    pts = pts.reshape(-1,1,2)   
    img = cv2.fillPoly(img,[pts],(0,0,0))
    img = cv2.circle(img,(178,236),40,(0,255,0),30)
    pts = np.array([[178,236],[217,187],[242,236]],np.int32)
    img = cv2.fillPoly(img,[pts],(0,0,0))
    img = cv2.circle(img,(316,236),40,(255,0,0),30)
    pts = np.array([[316,236],[285,181],[345,181]],np.int32)
    img = cv2.fillPoly(img,[pts],(0,0,0))
    cv2.putText(img,"OpenCV logo",(50,400),1,3,(255,255,255))

    cv2.imshow("circle",img) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    

drawing_functions()


