# Hand Gesture Volume Control
This project uses OpenCV, Mediapipe, and PyAutoGUI to control the system volume based on hand gestures detected via webcam. The script tracks hand landmarks and calculates the distance between the thumb and index finger to adjust the volume. When the distance is above a certain threshold, the volume increases, and when below, it decreases.

# Key Features:

    --> Hand Detection: Uses Mediapipe to detect and track hand landmarks.
    --> Gesture Recognition: Calculates the distance between thumb and index finger.
    --> Volume Control: Adjusts system volume based on finger distance.

# Requirements:

    1. OpenCV
    2. Mediapipe
    3. PyAutoGUI

# Usage:

    1. Clone the repository.
    2. Install the required libraries.
    3. Run the script to start controlling volume with hand gestures.
