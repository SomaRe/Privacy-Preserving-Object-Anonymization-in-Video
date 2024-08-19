# 🚗 Privacy-Preserving Object Anonymization in Video 🔍

Welcome to the **Privacy-Preserving Object Anonymization in Video** project! This repository contains the code and resources for a system designed to protect privacy in online media content by detecting and anonymizing license plates in videos. This approach can be extended to other objects as well, ensuring that sensitive information is hidden without compromising the visual quality of the content.

## 🌟 Project Overview

With the increasing prevalence of video content featuring cars, the visibility of license plates has become a significant privacy concern. This project addresses these concerns by developing a solution that:

- **Detects** license plates in both images and videos using state-of-the-art object detection models.
- **Anonymizes** detected license plates with techniques that maintain the visual appeal of the content, going beyond simple blurring.

### Key Features:

1. **License Plate Detection**
    - We fine-tuned YOLOv5 models to accurately detect license plates across various datasets, such as those from Kaggle and CCPD.
    - This ensures robust performance in diverse conditions, including varying lighting and camera angles.

2. **Consistency in Video Detection**
    - Implemented **Seq-NMS** to enhance detection consistency across video frames, reducing false positives and missed detections.
    - This technique ensures that the anonymization process is smooth and reliable throughout the video.

3. **Privacy-Preserving Modification**
    - Experimented with advanced techniques like inpainting and diffusion to replace real license plates with synthetic ones.
    - This approach preserves privacy while maintaining the video's visual integrity, avoiding the distractions caused by traditional blurring.

## 🚀 Getting Started

### Prerequisites

To get started, you'll need:

- Python 3.8 or later
- PyTorch
- OpenCV
- YOLOv5
- Seq-NMS
- Other dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/SomaRe/Privacy-Preserving-Object-Anonymization-in-Video.git
    cd Privacy-Preserving-Object-Anonymization-in-Video
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. **License Plate Detection**:
   - Run the script in jupyter notebooks to detect license plates in an image or video:


2. **Anonymization**:
   - Anonymize detected license plates using inpainting or diffusion techniques:<p style="color: tomato"><i>Needs more work and will be updated</i></p>

## 📈 Results

The system was able to:

- Achieve high accuracy in detecting license plates, even in challenging conditions.
- Provide seamless anonymization that preserves the overall aesthetics of the video content.

## 🔮 Future Work

- **Stable Diffusion Model**: One of the limitations we faced was writing a neural network from scratch for inpainting. We plan to integrate and fine-tune a Stable Diffusion model for better inpainting results in future versions.
- **Extended Object Anonymization**: Extend the system to handle other sensitive objects, such as faces, company logos, and other identifiable marks.

Stay tuned for updates as we continue to enhance the model and its capabilities!


## 📄 License

This project is licensed under the MIT License.

## 📢 Acknowledgements

- This project was inspired by the growing need for privacy protection in media content.
- We used the YOLOv5 framework and datasets from Kaggle and CCPD to build and fine-tune the detection models.
- Special thanks to the open-source community for providing tools and resources that made this project possible.

## 🔗 Connect

Let's connect and collaborate! Feel free to reach out if you're interested in computer vision, privacy protection, or media technology.

- **LinkedIn**: [Your LinkedIn Profile](https://www.linkedin.com/in/shivatejsoma)
- **GitHub**: [Your GitHub Profile](https://github.com/SomaRe)
