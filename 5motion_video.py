import cv2
cap = cv2.VideoCapture(r"C:\Users\vegu2\Desktop\IVA\EX5\istockphoto-1995820194-640_adpp_is.mp4") 
# frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height =int(cap.get( cv2.CAP_PROP_FRAME_HEIGHT))
fource = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output.mp4", fource, 5.0, (720,720))
ret, framel = cap.read()
ret, frame2 = cap.read() 
print(framel.shape)
while cap.isOpened():
  diff = cv2.absdiff(framel, frame2)
  gray= cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray, (5,5), 0)
  _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
  dilated = cv2.dilate(thresh, None, iterations=3)
  contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)
    if cv2.contourArea(contour) < 2000:
      continue
    cv2.rectangle(framel, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(framel, "Status: Movement", (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
    1, (0, 0, 255), 3)
  out.write(framel)
  cv2.imshow('',framel)
  framel = frame2
  ret, frame2 = cap.read()
  if cv2.waitKey(40)==27:
    break
cv2.destroyAllWindows()
cap.release()
out.release()
