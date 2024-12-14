from base.exercise_base import ExerciseBase
from utils.calculations import calculate_angle, is_arm_raised
from utils.mediapipe_setup import mp_pose
import cv2

class ArmStretchExercise(ExerciseBase):
    def __init__(self, name):
        super().__init__(name)

    def process_frame(self, frame, landmarks):
        shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                 landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
        wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                 landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

        angle = calculate_angle(shoulder, elbow, wrist)

        if is_arm_raised(shoulder, elbow, wrist):
            feedback = "Arm raised!"
            color = (0, 255, 0)  # أخضر
        else:
            feedback = "Raise your arm!"
            color = (0, 0, 255)  # أحمر

        # كتابة الملاحظات على الصورة
        cv2.putText(frame, feedback, (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
