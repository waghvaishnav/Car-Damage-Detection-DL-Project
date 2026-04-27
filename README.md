# Car-Damage-Detection-Deep Learning-Project

# 🚗 Car Damage Detection using Deep Learning

An end-to-end deep learning project that detects and classifies vehicle damage using ResNet50 (Transfer Learning). The system is trained on vehicle images and deployed as a production-ready application using Docker and AWS EC2 for real-time inference.

![Image](https://github.com/waghvaishnav/Car-Damage-Detection-DL-Project/blob/8833a4a827718f90c4557093c2076762d7c9a1bd/Screenshot%202026-04-18%20222056.png)### Model Details

📌 Project Overview

Manual inspection of vehicle damage is time-consuming and error-prone. This project automates the process using a CNN-based image classification model that identifies different types of car damage.

The model is trained on labeled vehicle images and fine-tuned using ResNet50 to achieve high accuracy in damage classification.

1. Used ResNet50 for transfer learning
2. Model was trained on Car images with 6 target classes
   1. Front Normal
   1. Front Crushed
   1. Front Breakage
   1. Rear Normal
   1. Rear Crushed
   1. Rear Breakage
9. The accuracy on the validation set was around 80%

🚀 Features
🔍 Deep Learning-based image classification
🧠 Transfer Learning using ResNet50
📊 Data augmentation and fine-tuning
🐳 Dockerized application for portability
☁️ Deployed on AWS EC2 for real-time inference
⚡ Fast prediction pipeline

🏗️ Tech Stack
Programming Language: Python
Deep Learning Framework: PyTorch
Model: ResNet50 (Transfer Learning)
Libraries: NumPy, Pandas, OpenCV, Matplotlib
Deployment: FastAPI / Streamlit (if used), Docker, AWS EC2

🧠 Model Architecture
Base Model: ResNet50 (pretrained on ImageNet)
Custom classification head added
Fine-tuned last layers for domain-specific learning
Regularization: Dropout
Optimization: Adam optimizer + learning rate tuning

📊 Performance
✅ Validation Accuracy: ~80%
📉 Improved generalization using augmentation
⚖️ Balanced precision and recall across classes

☁️ Deployment
Deployed on AWS EC2 instance
Model served for real-time predictions
Docker container ensures environment consistency
