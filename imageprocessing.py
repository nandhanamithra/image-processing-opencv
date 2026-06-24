import cv2
import numpy as np
image= cv2.imread(r"C:\flutter_projects\INTERNSHIP\lvl 2\class\image processing\image.jpg")

greyimage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])
sobel_y=np.array([
    [-1,-2,-1],
    [0,0,0],
    [1,2,1]
])
sobelx=cv2.filter2D(greyimage,-1,sobel_x) 
sobely=cv2.filter2D(greyimage,-1,sobel_y)
gradient_magnitude=np.sqrt(sobelx**2+sobely**2)

gradient_magnitude = gradient_magnitude / gradient_magnitude.max() * 255 #normalizingg
cv2.imwrite('edges.png', gradient_magnitude) #Saving the final edge-detected output as edges.png

cv2.imshow("Original image",image)
cv2.imshow("Grey image",greyimage)

print("\nSobel-X Output")
print(sobelx)
print("\nSobel-Y Output")
print(sobely)

print("\nFinal Edge-Detected Output")
print(gradient_magnitude)

cv2.waitKey(0)
cv2.destroyAllWindows()