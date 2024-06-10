import cv2
img =cv2.imread("solar-system.jpg")
cv2.imshow("output1",img)

cv2.putText(img,
            "sun",
            (20,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255))

cv2.putText(img,
            "mercury",
            (40,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255))


cv2.putText(img,
            "venus",
            (70,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255))


cv2.putText(img,
            "earth",
            (100,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255))



cv2.putText(img,
            "mars",
            (140,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255))


cv2.putText(img,
            "jupiter",
            (180,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255))


cv2.putText(img,
            "satrun",
            (240,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255))


cv2.putText(img,
            "uranus",
            (360,320),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255))


cv2.putText(img,
            "neptune",
            (400,320),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255))

cv2.imwrite('Solar_sysstemwithname.jpg',img)
            
cv2.waitKey(0)