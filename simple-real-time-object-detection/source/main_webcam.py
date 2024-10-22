import cv2
import numpy as np
from pathlib import Path

def setup_detector():
    """Setup the object detector with model and classes"""
    # Get paths relative to script location
    base_path = Path(__file__).parent.parent / 'config_files'
    
    # Load class names
    with open(base_path / 'coco.names', 'rt') as f:
        class_names = f.read().rstrip('\n').split('\n')
    
    # Initialize the model
    net = cv2.dnn_DetectionModel(
        str(base_path / 'frozen_inference_graph.pb'),
        str(base_path / 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt')
    )
    
    # Configure model parameters
    net.setInputSize(320, 320)
    net.setInputScale(1.0 / 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)
    
    return net, class_names

def detect_objects():
    """Run real-time object detection using webcam"""
    # Initialize camera
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 150)
    
    # Setup detector
    net, class_names = setup_detector()
    
    try:
        while True:
            # Read frame
            success, frame = cap.read()
            if not success:
                print("Failed to read from camera")
                break
            
            # Detect objects
            class_ids, scores, boxes = net.detect(frame, confThreshold=0.45)
            
            # Draw detections
            if len(class_ids) > 0:
                # Apply NMS
                indices = cv2.dnn.NMSBoxes(
                    boxes.tolist(), 
                    scores.flatten().tolist(), 
                    0.45, 
                    0.5
                )
                
                # Draw boxes for detected objects
                for i in indices:
                    box = boxes[i]
                    x, y, w, h = box
                    
                    # Draw rectangle
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    
                    # Add label
                    label = class_names[class_ids[i] - 1]
                    cv2.putText(frame, label, (x + 10, y + 30),
                              cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            
            # Show frame
            cv2.imshow("Object Detection", frame)
            
            # Break loop on 'q' press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    finally:
        # Cleanup
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_objects()