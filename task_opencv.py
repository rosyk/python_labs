from math import sqrt
from ctypes import cast, POINTER
import cv2
import mediapipe as mp
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def distance(xa, ya, xb, yb):
    dstnc = sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
    if dstnc < 20:
        return 20
    if dstnc > 130:
        return 130
    return dstnc


def volume_level():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.GetMute()
    volume.GetMasterVolumeLevel()
    volume.GetVolumeRange()
    return volume


def hand_volume_control():
    cap = cv2.VideoCapture(0)
    hands = mp.solutions.hands.Hands(static_image_mode=False,
                                     max_num_hands=1,
                                     min_tracking_confidence=0.5,
                                     min_detection_confidence=0.5)
    mp_draw = mp.solutions.drawing_utils

    point_x, point_y = 0, 0
    thumb_x, thumb_y = 0, 0
    pinky_x, pinky_y = 0, 0
    pinky_mcp_x, pinky_mcp_y = 0, 0

    volume = volume_level()

    while True:
        _, img = cap.read()
        result = hands.process(img)
        if result.multi_hand_landmarks:
            for id, lm in enumerate(result.multi_hand_landmarks[0].landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(img, (cx, cy), 3, (255, 0, 255))
                if id == 8:
                    point_x, point_y = cx, cy
                if id == 4:
                    thumb_x, thumb_y = cx, cy
                if id == 20:
                    pinky_x, pinky_y = cx, cy
                if id == 17:
                    pinky_mcp_x, pinky_mcp_y = cx, cy

            mp_draw.draw_landmarks(img, result.multi_hand_landmarks[0], mp.solutions.hands.HAND_CONNECTIONS)

            if distance(pinky_x, pinky_y, pinky_mcp_x, pinky_mcp_y) < 70:
                volume_lvl = (distance(point_x, point_y, thumb_x, thumb_y) - 20) / 1.3 / 100
                volume.SetMasterVolumeLevelScalar(volume_lvl, None)

        cv2.imshow('hand volume control', img)
        cv2.waitKey(1)


if __name__ == '__main__':
    hand_volume_control()
