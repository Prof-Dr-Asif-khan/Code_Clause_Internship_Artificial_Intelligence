
# Real-time Object Detection System
#### CodeClause Internship Project

## 📝 Description
A real-time object detection system built with Python and OpenCV, capable of detecting and classifying multiple objects through webcam feed or images. The system utilizes the SSD MobileNet model pre-trained on the COCO dataset, enabling detection of 80 different object classes with high accuracy.

## 🎯 Features
- Real-time object detection using webcam
- Support for image-based detection
- Detection of 80 different object classes
- Non-Maximum Suppression (NMS) for accurate bounding boxes
- Configurable confidence thresholds
- High-performance processing with OpenCV DNN module

## 🖼️ Sample Output Images
Here are some sample outputs from the object detection system:

| Detection Example  | Image |
|---------------------|-------|
| Cat                 | ![Cat](https://github.com/user-attachments/assets/96ed61ee-a072-4a70-96e4-47323ece1ee8) |
| Car                 | ![Car](https://github.com/user-attachments/assets/b8873b69-943c-4c16-837a-af9b191de5f6) |
| Motorcycle          | ![Motorcycle](https://github.com/user-attachments/assets/b575cff6-0563-4545-a1ca-416a1f6dd483) |
| Hat and Dog         | ![Hat and Dog](https://github.com/user-attachments/assets/e1ed0cb8-8bc0-4be7-879f-a8da2c1c1957) |
| Dog                 | ![Dog](https://github.com/user-attachments/assets/6b8a337b-be88-4c0e-ad79-a2c2006bfc97) |
| Person              | ![Person](https://github.com/user-attachments/assets/4fbc9e25-8563-42b8-aaa6-b72e1ceacdaf) |
| Cellphone           | ![Cellphone](https://github.com/user-attachments/assets/10029b91-7e18-4e55-bed7-b066f5b6c134) |
| Brush               | ![Brush](https://github.com/user-attachments/assets/15151b5d-ec6b-4d0b-93ab-e1bf17ced618) |
| Videos              | ![Videos](https://github.com/user-attachments/assets/55d8f1d0-379b-4a89-a4c6-9fa473bbc975) |

*Each image represents an object detected by the system in real time.*




## 🛠️ Technologies Used
- Python 3.8+
- OpenCV (cv2)
- NumPy
- SSD MobileNet v3 model
- COCO dataset classes

## 📁 Project Structure
```
object-detection/
├── config_files/
│   ├── coco.names           # Class names from COCO dataset
│   ├── frozen_inference_graph.pb    # Model weights
│   └── ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt  # Model config
├── source/
│   ├── main_webcam.py       # Real-time detection script
│   └── main_image.py        # Image detection script
├── images/                  # Sample images for testing
├── .gitignore
└── README.md
```

## 🚀 Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/object-detection.git
cd object-detection
```

2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install opencv-python
pip install numpy
```

4. Download model files
- Download the SSD MobileNet model files from the official OpenCV repository
- Place them in the `config_files` directory:
  - frozen_inference_graph.pb
  - ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt

## 💻 Usage

### For Webcam Detection:
```bash
python source/main_webcam.py
```
- Press 'q' to quit the application

### For Image Detection:
```bash
python source/main_image.py
```

## ⚙️ Configuration
You can modify detection parameters in the scripts:
- `thres`: Confidence threshold for detection (default: 0.45)
- `nms_threshold`: Non-maximum suppression threshold (default: 0.5)
- Input size: 320x320 (can be modified in the script)

## 🎥 Model Details
- **Architecture**: SSD (Single Shot MultiBox Detector) with MobileNet v3 backbone
- **Dataset**: Trained on COCO dataset
- **Input Size**: 320x320 pixels
- **Output**: Object class, confidence score, and bounding box coordinates

## 📊 Performance
- Real-time detection at ~30 FPS on modern CPUs
- Higher frame rates possible with GPU support
- Accuracy varies based on:
  - Object size
  - Lighting conditions
  - Camera quality
  - Distance from object

## 🤝 Contributing
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details

## 🙏 Acknowledgments
- OpenCV team for the DNN module
- COCO dataset contributors
- CodeClause for the internship opportunity

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## 📞 Contact

Mumtaz Ali - [engrmumtazali01@gmail.com](mailto:engrmumtazali01@gmail.com)

<p align="center">
  <a href="mailto:engrmumtazali01@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  <a href="https://www.linkedin.com/in/mumtaz-ali"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://www.instagram.com/its_maliyzi"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"/></a>
  <a href="https://x.com/mumtazali1223/status/1846913595021328672?s=51"><img src="https://img.shields.io/badge/X-1DA1F2?style=for-the-badge&logo=x&logoColor=white"/></a>
  <a href="https://discord.gg/DZgwHzEb"><img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white"/></a>
  <a href="https://wa.me/923476338292" target="_blank"><img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white"/></a>
</p>

<p align="center">Made with ❤️ by Mumtaz Ali</p>
