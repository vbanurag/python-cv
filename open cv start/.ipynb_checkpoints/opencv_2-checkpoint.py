import cv2

img = cv2.imread('../Computer-Vision-with-Python/DATA/00-puppy.jpg')

print(img)

while True:
    
    cv2.imshow('Puppy', img)
    
    # if we waited atleast 1 ms AND pressed escape key
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()