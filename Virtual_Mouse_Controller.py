import cv2
import numpy as np
import Hand_Tracking_Module as htm
import time
import autopy

##########################
Cam_w, Cam_h = 640, 480
Scr_w, Scr_h = autopy.screen.size()
frame_r = 160  # Frame Reduction
smooth = 9
pTime = 0
prevloc_X, prevloc_Y = 0, 0
currloc_X, currloc_Y = 0, 0
#########################
cap = cv2.VideoCapture(0)
cap.set(3, Cam_w)
cap.set(4, Cam_h)
detector = htm.handDetector(maxHands=1)

while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    img = cv2.flip(img, 1)
    cv2.rectangle(img, (frame_r, frame_r), (Cam_w - frame_r, Cam_h - frame_r),
                  (0, 0, 255), 2)
    img = detector.findHands(img)
    landmark_list, bbox = detector.findPosition(img)
    # 2. Get the tip of the index and middle fingers
    if len(landmark_list) != 0:
        x1, y1 = landmark_list[8][1:]  # Index Finger
        x2, y2 = landmark_list[12][1:]  # Middle Finger
        # print(x1, y1, x2, y2)
        # 3. Check which fingers are up
        fingers = detector.fingersUp()
        # print(fingers)
        # 4. Only Index Finger : Moving Mode
        if fingers[1] == 1 and fingers[2] == 0:
            # 5. Convert Coordinates
            # -----------------Interpolation--------------------
            x3 = np.interp(x1, (frame_r, Cam_w - frame_r), (0, Scr_w))
            y3 = np.interp(y1, (frame_r, Cam_h - frame_r), (0, Scr_h))
            # 6. Smoothen Values
            currloc_X = prevloc_X + (x3 - prevloc_X) / smooth
            currloc_Y = prevloc_Y + (y3 - prevloc_Y) / smooth
            # 7. Move Mouse
            autopy.mouse.move(currloc_X, currloc_Y)
            cv2.circle(img, (x1, y1), 5, (0, 0, 255), cv2.FILLED)
            prevloc_X, prevloc_Y = currloc_X, currloc_Y

        # 8. Both Index and middle fingers are up : Clicking Mode
        if fingers[1] == 1 and fingers[2] == 1:
            # 9. Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            # print(length)
            # 10. Click mouse if distance short
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]),
                           7, (255, 255, 255), cv2.FILLED)
                autopy.mouse.click()

    # 11. Frame Rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS : {int(fps)}', (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Display
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
