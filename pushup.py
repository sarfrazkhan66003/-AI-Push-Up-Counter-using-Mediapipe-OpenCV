import cv2
import mediapipe as mp
import numpy as np

# Initialize mediapipe pose
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def calculate_angle(a, b, c):
    """Calculate angle between three points"""
    a = np.array(a)  # First point
    b = np.array(b)  # Mid point
    c = np.array(c)  # End point

    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle
    return angle

# Start webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # use CAP_DSHOW for Windows

if not cap.isOpened():
    print("❌ Could not open webcam")
    exit()

counter = 0
stage = None  # up / down

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Failed to grab frame")
            break

        # Mirror the frame
        frame = cv2.flip(frame, 1)
        height, width, _ = frame.shape

        # Convert image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)
        image.flags.writeable = True
        frame = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:
            landmarks = results.pose_landmarks.landmark

            # Get coordinates (LEFT arm)
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x * width,
                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y * height]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x * width,
                     landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y * height]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x * width,
                     landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y * height]

            # Calculate angle
            angle = calculate_angle(shoulder, elbow, wrist)

            # Display angle
            cv2.putText(frame, f'Elbow Angle: {int(angle)}°', (30, 70),
                        cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)

            # Push-up counter logic
            if angle > 160:
                stage = "up"
            if angle < 90 and stage == "up":
                stage = "down"
                counter += 1

            # Show counter
            cv2.putText(frame, f'Push-ups: {counter}', (width//2 - 150, 70),
                        cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)

            # Draw landmarks
            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=4, circle_radius=6),
                mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=2, circle_radius=4)
            )

        except:
            pass

        # Show window
        cv2.imshow("Push-Up Tracker", frame)

        # Quit with Q
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
