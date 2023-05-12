from detector import *
import os

def vision():
    videoPath = 0
    configPath = os.path.join("model_data", "/home/sreehari/Python/Smart_glasses/Smart Glasses/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt")
    modelPath = os.path.join("model_data", "/home/sreehari/Python/Smart_glasses/Smart Glasses/frozen_inference_graph.pb")
    classesPath = os.path.join("model_data", "/home/sreehari/Python/Smart_glasses/Smart Glasses/coco.names")

    detector = Detector(videoPath, configPath, modelPath, classesPath)
    obj = detector.onVideo()
    return obj
    
