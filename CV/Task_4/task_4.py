import numpy
import cv2
photo = numpy.zeros((600,600,3))
photo1 = numpy.zeros((600,600,3))
photo[:,:]=[255,255,255]
photo1[:,:]=[0,0,0]

# Image 1

#Create 2
photo[50:55,350:550] = [0,255,0]
photo[50:250,550:555] = [0,255,0]
photo[250:255,350:555] = [0,255,0]
photo[250:450,350:355] = [0,255,0]
photo[450:455,350:555] = [0,255,0]

#create 5
photo[50:55,50:250] = [0,255,0]
photo[50:250,50:55] = [0,255,0]
photo[250:255,50:250] = [0,255,0]
photo[250:450,250:255] = [0,255,0]
photo[450:455,50:250] = [0,255,0]

cv2.imshow("Image1",photo)
cv2.waitKey()
cv2.destroyAllWindows()

# Image 2

#Create 4
photo1[50:250,50:55] = [255,0,0]
photo1[250:255,50:250] = [255,0,0]
photo1[150:350,150:155] = [255,0,0]
#create 1
photo1[50:350,450:455] = [255,0,0]

cv2.imshow("Image2",photo1)
cv2.waitKey()
cv2.destroyAllWindows()

#Swapping Image
swap1 = photo[0:600,0:300]
swap2 = photo1[0:600,300:600]

s1 = numpy.copy(swap1)
s2 = numpy.copy(swap2)

photo[0:600,0:300] = s2
photo1[0:600,300:600] = s1
cv2.imshow("Image2",photo)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("Image2",photo1)
cv2.waitKey()
cv2.destroyAllWindows()

#Take Two Image and Make it into one
newImage = numpy.zeros((600,1200,3))
newImage[0:600,0:600] = photo[:]
newImage[0:600,600:1200] = photo1[:]

cv2.imshow("CollageImage",newImage)
cv2.waitKey()
cv2.destroyAllWindows()