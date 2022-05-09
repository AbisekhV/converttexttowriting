import pywhatkit as kit 
import cv2

kit.text_to_handwriting("Siddhartha",save_to="handwriting.png")
img=cv2.imread("handwriting.png")

cv2.imshow("Text to handwriting ", img)
cv2.waitKey(0)

cv2.destroyAllWindows()