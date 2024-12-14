import cv2
from utils.mediapipe_setup import pose

class ExerciseBase:
    def __init__(self, name):
        self.name = name

    def process_frame(self, frame, landmarks):
        pass

    def start(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print(f"Error: Unable to access the camera for {self.name}.")
            return

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to grab frame from the camera.")
                break

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(rgb_frame)

            if results.pose_landmarks:
                landmarks = results.pose_landmarks.landmark
                self.process_frame(frame, landmarks)

            # كتابة اسم التمرين أعلى الشاشة
            cv2.putText(frame, f"Exercise: {self.name}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            cv2.imshow(f"{self.name} Analysis", frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
