import cv2

print("=== Image Filter Lab ===")

# load image
img = cv2.imread("sample.jpg")

# grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur
blur = cv2.GaussianBlur(img, (5,5), 0)

# edge detection
edges = cv2.Canny(img, 100, 200)

# show images
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale", gray)
cv2.imshow("Blur", blur)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()