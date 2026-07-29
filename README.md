# 🖼️ Image Recognition using MobileNetV2

An AI-powered image classification web application built with **TensorFlow**, **MobileNetV2**, and **Streamlit**. Upload an image, and the model predicts the object present in the image with the **Top 5 most probable classes**.

---

## 🚀 Live Demo

🔗 **Live App:** https://image-recognition-system.streamlit.app/

---

## 📌 Features

- 📤 Upload JPG, JPEG, or PNG images
- 🤖 Uses the pretrained MobileNetV2 model
- 🎯 Displays Top 5 predicted classes with confidence scores
- ⚡ Fast predictions using TensorFlow
- 🎨 Simple and user-friendly Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- TensorFlow
- MobileNetV2
- NumPy
- Pillow

---

## 📂 Project Structure

```text
Image-Recognition/
│
├── Images/
│   └── sample_image.jpg
│
├── Notebook/
│   └── Image_recognition.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Image-Recognition.git
```

Move into the project folder:

```bash
cd Image-Recognition
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 🖼️ How It Works

1. Upload an image.
2. The image is resized to **224 × 224** pixels.
3. The image is preprocessed using MobileNetV2 preprocessing.
4. The pretrained MobileNetV2 model predicts the object.
5. The application displays the **Top 5 predictions** along with their confidence scores.

---

## 📊 Model

- **Model:** MobileNetV2
- **Framework:** TensorFlow / Keras
- **Dataset:** ImageNet (Pretrained Weights)
- **Input Size:** 224 × 224 RGB Images

---

## 📸 Sample Output

| Rank | Prediction | Confidence |
|------|------------|------------|
| 1 | Labrador Retriever | 97.82% |
| 2 | Golden Retriever | 1.45% |
| 3 | Chesapeake Bay Retriever | 0.39% |
| 4 | Flat-coated Retriever | 0.18% |
| 5 | Kuvasz | 0.09% |

---

## 📦 Requirements

- Python 3.10+
- Streamlit
- TensorFlow
- NumPy
- Pillow

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 👩‍💻 Author

**Nivedita Rani**

GitHub: https://github.com/niveditarani254

---

⭐ If you found this project helpful, consider giving it a star!
