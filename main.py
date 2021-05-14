import cv2

trained_face_data = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml")

img = cv2.imread('ch.jpg')

gray_scaled_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_coordinates = 

cv2.imshow('THOR', gray_scaled_img)
cv2.waitKey()


print("Code compiled succefully")


