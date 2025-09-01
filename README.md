# -AI-Push-Up-Counter-using-Mediapipe-OpenCV

This project is an AI-powered Push-Up Counter built with Python, Mediapipe, and OpenCV.
It uses pose estimation, joint angle calculation, and simple counting logic to automatically detect and count push-ups in real time using a webcam.

📸 Demo
<img width="803" height="631" alt="image" src="https://github.com/user-attachments/assets/f7740d82-f33b-4f87-9678-67d081b249c8" />

🔑 Key Features
✅ Real-time pose detection using Mediapipe
✅ Calculates elbow joint angle using Numpy & trigonometry
✅ Counts push-ups automatically based on arm movement
✅ Displays feedback (elbow angle & rep count) on screen
✅ Tracks left arm (can be extended to both arms)

🧠 Algorithm
1.Pose Estimation (Mediapipe)
    a.Detects 33 body landmarks (shoulders, elbows, wrists, hips, etc.).
    b.Extracts shoulder, elbow, and wrist coordinates.
2.Angle Calculation
    The elbow angle is calculated using:
      θ=arctan2(cy​−by​,cx​−bx​)−arctan2(ay​−by​,ax​−bx​)

    Where:
      a = Shoulder
      b = Elbow
      c = Wrist

3.Push-Up Logic
      a.If angle > 160° → Position = "Up"
      b.If angle < 90° and previous position = "Up" → +1 push-up

🖥️ Usage
  Press Q to quit the application.
  Counter and elbow angle will be displayed on the screen.
  Make sure you are visible in the webcam with good lighting.

🌍 Applications
  🏋️ Fitness Tracking – Automated push-up counter for workouts.
  🩺 Physiotherapy – Helps monitor patients’ exercise movements.
  📱 Mobile Apps – Can be integrated into fitness apps for real-time tracking.
  🤖 AI + IoT – Can connect with wearables or smart gym equipment.

🚀 Future Enhancements
  🔹 Track both arms for higher accuracy
  🔹 Add voice feedback (e.g., “Go Lower!”, “Good Job!”)
  🔹 Detect body posture (hips & shoulders) to ensure proper form
  🔹 Save workout history in CSV/Database

🙌 Acknowledgements
  Mediapipe by Google
  OpenCV for real-time computer vision
  Inspired by the idea of AI-powered personal fitness assistants

🔥 “AI is not replacing trainers, it’s empowering them with data.”
