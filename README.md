# Vision Assist

## Introduction

The main intent of this project is to help blind people who are not able to recognize objects in front of them. This project helps blind people to detect objects and provide alert messages. Blind or visually impaired people feel miserable and helpless when they need help with their daily simple jobs. Many of them are afraid of going out unless it's necessary. Smart Glasses for the Blind is a portable device that will make blind and visually impaired people's lives much easier, as it will help them in recognizing objects, colors, and even texts. The system is based on IoT and contains a camera, Bluetooth headset, and sensors connected to a Raspberry Pi. The software part uses OpenCV framework and Python programming language, along with deep learning techniques for object detection.

## Features

- Object detection and recognition
- Text recognition
- Date and time information
- Jokes and small talk
- Support for multiple languages
- Small and portable

## Getting Started

### Prerequisites

- Python 3.10
- speech_recognition
- gTTS
- os
- datetime
- MessageToDict
- numpy
- cv2
- time
- playsound
- requests
- json
- urlopen
- Dialogflow API key
- OpenWeatherMap API key

### Installing

1. Clone this repository:

2. Install required dependencies:

3. Obtain the Dialogflow API key and OpenWeatherMap API key and set them in the appropriate environment variables or configuration file.

### Usage

1. Connect the camera and Bluetooth headset to the Raspberry Pi.
2. Run the main file:- Python.py
3. Speak a command and wait for the response from the Smart Glasses.

## Architecture

![Architecture 1](/Screenshots/Architecture-1.png)
![Architecture 2](/Screenshots/Architecture-2.png)

## Limitations

- Limited response time
- Lack of proper object detection model
- Lack of personalized model

## Future Work

- Build a personalized object detection model
- Improve the response time
- Enhance the object detection model for better accuracy

## Acknowledgments

- Thanks to OpenCV, Dialogflow, and OpenWeatherMap for providing their APIs.
- Thanks to the community for the support and feedback.
  
