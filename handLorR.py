import cv2
import mediapipe as mp
from google.protobuf.json_format import MessageToDict
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=2)
webcam = cv2.VideoCapture(0)
while True:
    success, img = webcam.read()
    original_img=img.copy() 
    img = cv2.flip(img, 1)
    RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(RGB_img)
    if results.multi_hand_landmarks:
        if len(results.multi_handedness) == 2: 
            cv2.putText(original_img, 'Both Hands', (250, 56), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)

        else:
            for i in results.multi_handedness:
                label = MessageToDict(i)['classification'][0]['label']

                if label == 'Left':
                    cv2.putText(original_img, f'{label} Hand', (20, 56), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)

                if label == 'Right':
                    cv2.putText(original_img, f'{label} Hand', (460, 56), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow('image', original_img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
