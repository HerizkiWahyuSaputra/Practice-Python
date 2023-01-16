import cv2

#processing input image
img = cv2.imread('maps_worldwide.jpg', 0)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

#processing learning data image
cv2.imwrite('new_img.jpg', img)

#processing output image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()