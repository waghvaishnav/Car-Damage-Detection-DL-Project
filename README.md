# 🚗 Car Damage Detection using Deep Learning

An end-to-end deep learning project that detects and classifies vehicle damage using ResNet50 (Transfer Learning). The system is trained on vehicle images and deployed as a production-ready application using Docker and AWS EC2 for real-time inference.

![Image](https://github.com/waghvaishnav/Car-Damage-Detection-DL-Project/blob/8833a4a827718f90c4557093c2076762d7c9a1bd/Screenshot%202026-04-18%20222056.png)### Model Details

## 📌 Project Overview

Manual inspection of vehicle damage is time-consuming and error-prone.  
This project automates the process using a CNN-based image classification model that identifies different types of car damage.

The model is trained on labeled vehicle images and fine-tuned using **ResNet50 (Transfer Learning)** to achieve high accuracy.

## Problem Statement 
Build a POC for detecting car damage based on uploaded car images. The model should 
classify car damage into six possible categories with an accuracy of at least 75%. The 
categories are: 
1. Front Normal 
2. Front Breakage 
3. Front Crushed 
4. Rear Normal 
5. Rear Breakage 
6. Rear Crushed
---

## 🚀 Features

- 🔍 Deep Learning-based image classification  
- 🧠 Transfer Learning using ResNet50  
- 📊 Data augmentation and fine-tuning  
- 🐳 Dockerized application for portability  
- ☁️ Deployed on AWS EC2 for real-time inference  
- ⚡ Fast prediction pipeline  

---

## 🏗️ Tech Stack

- **Programming Language:** Python  
- **Deep Learning Framework:** PyTorch  
- **Model:** ResNet50 (Transfer Learning)  
- **Libraries:** NumPy, Pandas, OpenCV, Matplotlib  
- **Deployment:** FastAPI / Streamlit, Docker, AWS EC2  

---

## 🧠 Model Architecture

- Base Model: ResNet50 (pretrained on ImageNet)  
- Custom classification head added  
- Fine-tuned last layers for domain-specific learning  
- Regularization: Dropout  
- Optimizer: Adam  

---

## 📊 Performance

- ✅ Validation Accuracy: ~80%  
- 📉 Improved generalization using augmentation  
- ⚖️ Balanced precision and recall across classes  

---

## ☁️ Deployment

- Deployed on AWS EC2 instance  
- Model served for real-time predictions  
- Docker used for environment consistency  
