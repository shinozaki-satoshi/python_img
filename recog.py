import cv2

img =cv2.imread("recog_data/illust.png")

cascade_file_face="face.xml"
cascade_face=cv2.CascadeClassifier(cascade_file_face)

#画像を白黒に変換
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_list=cascade_face.detectMultiScale(img_gray,minSize=(10,10))

for (x,y,w,h) in face_list:
    color =(0,0,225)
    pen_w=2
    cv2.rectangle(img,(x,y),(x+w,y+h),color,thickness=pen_w)

cv2.imwrite("data/out3.jpg",img)
