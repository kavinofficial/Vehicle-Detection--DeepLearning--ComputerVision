Vehicle Detector
Overview
This project is a machine learning-based system for identifying vehicles in real-time. Designed for Indian road conditions, the model can detect various vehicle types commonly found in India, providing accurate identification using advanced computer vision techniques.

Features
Vehicle Detection: Identifies multiple types of vehicles in real-time.
Optimized for Indian Roads: Specifically designed to detect vehicles unique to India.
Deployment Ready: Trained model saved as a .pt file for seamless use.
Technologies Used
Frameworks: PyTorch
Detection Model: YOLOv8
Programming Language: Python
Tools: OpenCV for image processing
Prerequisites
Before running the project, ensure you have the following installed:

Python 3.8 or later
PyTorch
OpenCV
Setup Instructions
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/vehicle-detector.git  
cd vehicle-detector  
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt  
Place the trained model file (model.pt) in the weights folder.
Running the Application
To detect vehicles in a video or image:

bash
Copy code
python detect.py --source <path_to_video_or_image> --weights weights/model.pt  
Model Training
To train the model on your own dataset:

Prepare your dataset with labeled images.
Update the data.yaml file with your dataset path and classes.
Train the YOLO model:
bash
Copy code
python train.py --data data.yaml --weights yolov8.pt --epochs 50  
License
This project is licensed under the MIT License - see the LICENSE file for details.
