from base.exercise_base import ExerciseBase
from utils.calculations import calculate_angle
from utils.mediapipe_setup import mp_pose
import cv2 

class SquatsExercise(ExerciseBase):
    def __init__(self, name):
        super().__init__(name)

    def process_frame(self, frame, landmarks):
        hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
               landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
        knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
        ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                 landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

        angle = calculate_angle(hip, knee, ankle)

        if angle < 90:
            feedback = "Go lower!"
            color = (0, 0, 255)  # أحمر
        else:
            feedback = "Good form!"
            color = (0, 255, 0)  # أخضر

        # كتابة الملاحظات على الصورة
        cv2.putText(frame, feedback, (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
