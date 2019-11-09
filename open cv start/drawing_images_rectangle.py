# Drawing images with mouses

import cv2
import numpy as np


#######################
##### Variables #######
#######################

drawing = False # True if mouse is pressed
ix,iy = -1,-1

########################
#### FUNCTION ##########
########################



def draw_rect(event, x,y, flags, param):
    global ix,iy,drawing,mode
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        
        if drawing:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        
img = np.zeros((512,512, 3), np.uint8)
        
cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_rect)
    


##############################################
########## SHOWING IMAGE WITH OPENCV #########
##############################################

while True:
    
    cv2.imshow('my_drawing', img)
    
    # if we waited atleast 1 ms AND pressed escape key
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()