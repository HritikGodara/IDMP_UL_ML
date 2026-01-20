# 🌿 AyurVision: AI-Based Medicinal Plant Identifier

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://huggingface.co/spaces/YOUR_USERNAME/Ayurveda-Plant-Identifier)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97-Hugging%20Face-yellow)](https://huggingface.co/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://opensource.org/licenses/Apache-2.0)

## 📖 Overview

**AyurVision** is a Computer Vision application designed to automate the identification of Indian medicinal plants and raw materials. 

In the Ayurvedic supply chain, the misidentification of raw drugs (*Sandigdha Dravya*) and adulteration are critical issues. This project leverages state-of-the-art **Vision Transformers (ViT)** to classify plant species with high precision, aiding researchers, practitioners, and traders in verifying authenticity.

The system takes an image input, processes it using a fine-tuned Deep Learning model, and outputs the **Scientific Name**, **Ayurvedic Properties**, and **Medicinal Uses**.

## ✨ Key Features

* **High Accuracy:** Utilizing the `google/vit-base-patch16-224` architecture, fine-tuned to achieve **~99% accuracy** on the validation set.
* **Real-Time Identification:** Instant classification of 40+ distinct medicinal plant species (e.g., *Ashwagandha, Tulsi, Neem, Amla*).
* **Ayurvedic Knowledge Base:** Integrated database providing immediate information on:
    * Scientific & Common Names
    * Therapeutic Uses
    * Ayurvedic Attributes (Dosha effects, Gunas)
* **User-Friendly Interface:** Built with **Streamlit** for an intuitive, drag-and-drop web experience.
* **Confidence Metrics:** Displays probability scores to alert users when the model is uncertain.

## 🛠️ Tech Stack

* **Deep Learning:** PyTorch, Hugging Face Transformers (ViT)
* **Image Processing:** PIL (Python Imaging Library), Torchvision
* **Web Framework:** Streamlit
* **Deployment:** Hugging Face Spaces
* **Dataset:** [Indian Medicinal Leaves Dataset (Kaggle)](https://www.kaggle.com/datasets/aryashah2k/indian-medicinal-leaves-dataset)

## 🚀 Live Demo

Check out the running application here:  
👉 **[Link](https://huggingface.co/spaces/Gotar0/IDMP_UL_ML)**

## 📂 Project Structure

```bash
├── IDMP_UL_ML/               # The trained ViT model files
│   ├── config.json
│   ├── pytorch_model.bin
│   └── preprocessor_config.json
├── app.py                    # Main Streamlit application script
├── plant_info.py             # Database of Ayurvedic properties
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## ⚙️ Installation & Local Usage
To run this project on your local machine:

### Clone the repository:

```bash

git clone [https://github.com/YOUR_USERNAME/AyurVision.git](https://github.com/YOUR_USERNAME/AyurVision.git)
cd AyurVision
```
### Install dependencies:

```bash

pip install -r requirements.txt
```
### Run the application:

```bash

streamlit run app.py
```
Access: Open your browser and go to http://localhost:8501.

## 📊 Model Performance
The model was trained on a dataset of ~6,000 images across 40+ classes.

Architecture: Vision Transformer (ViT-Base)

Training Epochs: 5

Test Accuracy: 99.7%

F1-Score: 0.99

Confusion Matrix analysis shows distinct separation between visually similar classes (e.g., Curry Leaves vs. Neem), validating the model's robustness.

## 🔮 Future Scope
Mobile App Integration: Porting the model to TensorFlow Lite for an offline Android app.

Raw Material Expansion: Expanding the dataset to include dried roots, barks, and resins (identifying raw drugs rather than just fresh leaves).

Adulterant Detection: Specifically training the model to flag common market adulterants.

## 🤝 Contributing
Contributions are welcome! If you have images of rare medicinal plants or ideas for feature improvements, please open an issue or submit a pull request.

## 📄 License
This project is licensed under the Apache 2.0 License.
