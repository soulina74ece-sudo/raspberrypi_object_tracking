# raspberrypi_object_tracking
Real-time vision-based object tracking using Raspberry Pi, OpenCV, and a pan-tilt servo mechanism. Implements centroid-based detection, position tracking, and dead-zone control to minimize unnecessary servo commands.

# Raspberry Pi-Based Object Tracking System

A real-time embedded vision system for object detection and pan-tilt camera tracking using Raspberry Pi and OpenCV.

The system detects a colored object, calculates its centroid, and adjusts the camera orientation using two servo motors to keep the object within the camera's field of view.

## Key Features

- Real-time camera input and image processing
- Color-based object detection using OpenCV
- Centroid-based object localization
- Two-axis pan-tilt servo control
- Error-based tracking and movement correction
- Dead-zone control to prevent unnecessary servo movement commands
- Modular Python implementation

## System Architecture

Camera Input → Object Detection → Centroid Calculation → Error Computation → Dead-Zone Evaluation → Servo Control

## Hardware Requirements

- Raspberry Pi
- Compatible camera module
- Two servo motors
- Suitable servo power supply and wiring

## Software and Technologies

- Python
- OpenCV
- Raspberry Pi GPIO control
- Computer Vision
- Embedded Systems

## Project Structure

raspberry-pi-object-tracking/
├── camera.py
├── object_detection.py
├── servo_control.py
├── servo_control_y.py
├── main.py
├── README.md
├── requirements.txt
└── .gitignore


## Working Principle

1. **Image Acquisition:** The Raspberry Pi camera continuously captures image frames.
2. **Object Detection:** OpenCV processes each frame to detect the target blue object.
3. **Centroid Calculation:** The system calculates the object's centroid to determine its position in the frame.
4. **Error Computation:** The difference between the object centroid and the frame center determines the horizontal and vertical tracking errors.
5. **Dead-Zone Evaluation:** If the tracking error is within the defined dead zone, no new servo movement command is issued.
6. **Servo Actuation:** When the object moves outside the dead zone, the Raspberry Pi commands the pan and tilt servos to adjust the camera's orientation.
7. ## Project Demonstration

Watch the Raspberry Pi-based real-time object tracking system in action.

[▶️ Watch the Object Tracking Demonstration](https://drive.google.com/file/d/1Z0hf5qx9rzMDfSdWlR3JLHlFqldanJZ7/view?usp=sharing)

## Project Structure

- `camera.py` — Captures frames from the camera.
- `object_detection.py` — Detects the target object and calculates its centroid.
- `servo_control.py` — Controls horizontal pan movement.
- `servo_control_y.py` — Controls vertical tilt movement.
- `main.py` — Integrates detection, tracking, and servo control.


## Future Improvements

- Improve tracking stability under changing lighting conditions.
- Optimize tracking performance and servo command handling.
- Extend detection to support multiple object types.
- Evaluate tracking accuracy under different operating conditions.


## Acknowledgements

I would like to express my sincere gratitude to **Prof. Sarang Pendharkar** for his valuable guidance, technical insights, and encouragement throughout the development of this project. His mentorship has been instrumental in strengthening my understanding of embedded systems, computer vision, and hardware-based object tracking.

I am grateful for the opportunity to learn, experiment, and apply theoretical concepts to a practical engineering system under his guidance.
