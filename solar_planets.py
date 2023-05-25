import cv2
img = cv2.imread("solar-system.jpg")
print(img)
cv2.putText(img,  
           "Sun",
           (0, 213),  
           fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX ,
           fontScale=2,  
           thickness = 4,
           color=(255, 255, 255)
           )
cv2.putText(img,  
           "Mercury",
           (100, 106),  
           fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX ,
           fontScale=1,  
           thickness = 2,
           color=(0, 255, 0)
           )
cv2.putText(img,  
           "Venus",
           (175, 318),  
           fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX ,
           fontScale=1,  
           thickness = 2,
           color=(255, 0, 0)
           )
cv2.putText(img,  
           "Earth",
           (275, 106),  
           fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX ,
           fontScale=1,  
           thickness = 2,
           color=(0, 255, 0)
           )
cv2.putText(img,  
           "Mars",
           (375, 318),  
           fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX ,
           fontScale=1,  
           thickness = 2,
           color=(255, 0, 0)
           )
cv2.putText(img,  
           "Jupiter",
           (550, 106),  
           fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX ,
           fontScale=1,  
           thickness = 2,
           color=(0, 255, 0)
           )
cv2.putText(img,  
           "Saturn",
           (750, 318),  
           fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX ,
           fontScale=1,  
           thickness = 2,
           color=(255, 0, 0)
           )
cv2.putText(img,  
           "Uranus",
           (950, 106),  
           fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX ,
           fontScale=1,  
           thickness = 2,
           color=(0, 255, 0)
           )
cv2.putText(img,  
           "Neptune",
           (1100, 318),  
           fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX ,
           fontScale=1,  
           thickness = 2,
           color=(255, 0, 0)
           )
cv2.imshow("Solar System", img)
cv2.waitKey(0)

