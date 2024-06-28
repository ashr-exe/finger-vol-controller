import cv2
import mediapipe
import pyautogui

webcam = cv2.VideoCapture(0)
my_hands = mediapipe.solutions.hands.Hands()
drawing_utils = mediapipe.solutions.drawing_utils

while True:
    boolean, image=webcam.read()
    frame_height, frame_width, f_depth = image.shape
    
    #-------Detect hands
    
    detect = my_hands.process(image)
    hands=detect.multi_hand_landmarks
    
    
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand)
            
    #---------Detect fingers
    
            landmarks = hand.landmark
            for idx, landmark in enumerate(landmarks):
                x= int(landmark.x * frame_width)
                y= int(landmark.y *frame_height)
                
                if idx == 8:
                    cv2.circle(img=image, center=(x, y), radius=8, color=(200, 100, 100), thickness=5)
                    x1, y1 = x, y
                
                if idx == 4:
                    cv2.circle(img=image, center=(x, y), radius=8, color=(200, 100, 100), thickness=5)
                    x2, y2 = x, y
            
        
    #-----------Distance
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
            distance = ((x1-x2)**2 + (y1-y2)**2)**(0.5)//2
            print(distance)
    
            if distance >50:
                pyautogui.press("volumeup")
            else:
                pyautogui.press("volumedown")
        
    
    cv2.imshow("the TITLE", image)
    key = cv2.waitKey(10)

    if key == 27:
        break

webcam.release()
cv2.destroAllWindows()
        
        