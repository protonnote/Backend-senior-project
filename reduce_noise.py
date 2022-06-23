import cv2

image = cv2.imread('D:/Project/api_python/upload/image_2_at-57-95.jpg')

alpha = 1.1 # Contrast control (1.0-3.0)
beta = 15 # Brightness control (0-100)

adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

cv2.imshow('original', image)
cv2.imshow('adjusted', adjusted)
cv2.waitKey()

cv2.destroyAllWindows()