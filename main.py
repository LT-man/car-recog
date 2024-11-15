import cv2
car = "cars.xml"
video = cv2.VideoCapture("video1.avi")
video2 = cv2.VideoCapture("cars+cycle.avi")

model = cv2.CascadeClassifier(car)
while True:
    ret,bg = video2.read()
    gray = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
    cars = model.detectMultiScale(gray, 1.1, 1)
    for x, y, w, h in cars:
        cv2.rectangle(bg, (x,y), (x+w, y+h), (230, 25, 189), 2)
    cv2.imshow("screen", bg)
    k = cv2.waitKey(20)
    if k == 27:
        break