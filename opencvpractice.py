import cv2

img = cv2.imread("galaxy.jpg",0)

resize_image = cv2.resize(img,(500,500))
cv2.imshow("Galaxy",resize_image)
cv2.imwrite("Galaxy_re.jpg", resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
