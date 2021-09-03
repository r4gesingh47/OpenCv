import cv2 
import numpy as np

def sketch(image):
   grayimg=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
   blurimg=cv2.GaussianBlur(grayimg,(3,3),0)
   edges=cv2.Canny(blurimg,10,80)
   ret,mimg=cv2.threshold(edges,50,255,cv2.THRESH_BINARY_INV)
   return mimg

vid_capt=cv2.VideoCapture(0)
while True:
   ret,pic_capt=vid_capt.read()
   cv2.imshow('Your Sketch',sketch(pic_capt))
   if cv2.waitKey(1)==13:
    break
vid_capt.release()
cv2.destroyAllWindows()
