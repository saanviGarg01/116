import cv2

img = cv2.imread("trre.jpeg")
cv2.imshow("output1", img)



text="haapy world enviorment day"
cv2.putText(img,
            text,
            (20,220),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(0,0,255))

cv2.imshow("output2",img)

cv2.waitKey(0)


