import cv2
import random
trained_face_data = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml")

img = cv2.imread('ch.png')

gray_scaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_coordinates = trained_face_data.detectMultiScale(gray_scaled_img)
print(face_coordinates)

for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h),(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)), random.randint(3, 6))

cv2.imshow('THOR', img)
cv2.waitKey()


print("Code compiled succefully")
