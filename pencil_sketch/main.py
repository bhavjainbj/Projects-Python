import cv2
import csv



image = cv2.cv2.imread("passport size photo-min.jpg")
grayImage = cv2.cv2.cvtColor(image, cv2.cv2.COLOR_BGR2GRAY)
grayImageinv = 255 - grayImage
grayImageinv = cv2.cv2.GaussianBlur(grayImageinv, (21,21),0)
output = cv2.cv2.divide(grayImage, 255-grayImageinv, scale=256.0)
cv2.cv2.namedWindow("image", cv2.cv2.WINDOW_AUTOSIZE)
cv2.cv2.namedWindow("pencilsketch", cv2.cv2.WINDOW_AUTOSIZE)
cv2.cv2.imshow("image", image)
cv2.cv2.imshow("pencilsketch", output)
cv2.cv2.waitKey(0)
cv2.cv2.destroyAllWindows()