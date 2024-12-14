import math
import mediapipe as mp

class Stretching:
    def __init__(self):
        # إعداد Mediapipe
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()
        self.mp_drawing = mp.solutions.drawing_utils

    def calculate_angle(self, point1, point2, point3):
        """حساب الزاوية بين ثلاث نقاط"""
        x1, y1 = point1
        x2, y2 = point2
        x3, y3 = point3

        angle = math.degrees(
            math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2)
        )
        return abs(angle) if angle >= 0 else abs(angle + 360)

    def check_stretching(self, landmarks):
        """التحقق إذا كانت الحركة صحيحة لتمرين التمدد"""
        # استخراج الإحداثيات
        left_shoulder = [landmarks[11].x, landmarks[11].y]
        left_elbow = [landmarks[13].x, landmarks[13].y]
        left_wrist = [landmarks[15].x, landmarks[15].y]

        # حساب الزاوية
        angle = self.calculate_angle(left_shoulder, left_elbow, left_wrist)

        # التحقق من الوضعية الصحيحة
        if 160 <= angle <= 180:
            return True, angle
        return False, angle

    def process_frame(self, frame):
        """معالجة الإطار للتحقق من تمرين التمدد"""
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = self.pose.process(frame_rgb)

        if results.pose_landmarks:
            self.mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS
            )

            # التحقق من تمرين التمدد
            is_correct, angle = self.check_stretching(results.pose_landmarks.landmark)
            return frame, is_correct, angle

        return frame, False, None
