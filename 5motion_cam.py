import cv2
cap = cv2.VideoCapture(0)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))
ret, framel = cap.read()
ret, frame2 = cap.read()
if not ret:
    print("Failed to read from webcam.")
    cap.release()
    exit()
print(framel.shape)
while cap.isOpened():
    diff = cv2.absdiff(framel, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
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
    cv2.imshow('Motion Detection', framel)
    framel = frame2
    ret, frame2 = cap.read()
    if not ret:
        break
    if cv2.waitKey(1) == 27:  
        break
cap.release()
out.release()
cv2.destroyAllWindows()