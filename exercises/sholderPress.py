import math

class ShoulderPress:
    def __init__(self):
        self.counter = 0  # Number of repetitions
        self.direction = 0  # 0: Down, 1: Up

    def calculate_angle(self, shoulder, elbow, wrist):
        # Calculate the angle between the shoulder, elbow, and wrist joints
        radians = math.atan2(wrist[1] - elbow[1], wrist[0] - elbow[0]) - math.atan2(shoulder[1] - elbow[1], shoulder[0] - elbow[0])
        angle = abs(radians * 180.0 / math.pi)
        return angle

    def evaluate_press(self, angle):
        # Logic for counting repetitions based on angles
        if angle < 90 and self.direction == 0:  # When the arms are down
            self.direction = 1
        elif angle > 160 and self.direction == 1:  # When the arms are lifted up
            self.counter += 1
            self.direction = 0
        return self.counter

    def provide_feedback(self, angle):
        # Providing feedback based on the angle of the movement
        if angle < 90:
            return "Lift your arms higher!"
        elif angle > 160:
            return "Lower your arms a bit!"
        else:
            return "Great form!"