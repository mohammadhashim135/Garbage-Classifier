# **Waste Classification Management** ♻️  
**An AI-powered Real-Time Waste Detector using Streamlit & TensorFlow**

---

## **Overview**  
**Waste Classification Management** is a smart web application built with **Streamlit**, allowing users to classify waste in real time using a trained **Keras deep learning model**. Whether it's biodegradable or non-biodegradable, this app helps promote sustainable waste segregation with the power of machine learning and computer vision.

---

## **Features** 🚀  
✅ **Real-time Waste Detection** – Upload an image or capture live to detect the type of waste.  
✅ **Built with Deep Learning** – Uses a trained Keras model for high accuracy waste classification.  
✅ **Clean Streamlit Interface** – Simple and intuitive UI for ease of use.  
✅ **Instant Feedback** – Get classification results immediately upon uploading.  
✅ **Lightweight Deployment** – Easily deployable on [Streamlit Cloud](https://streamlit.io/cloud).

---

## 📸 Screenshot


![Image](https://github.com/user-attachments/assets/7dbd1ce9-5a04-4731-b567-3ac13cf45c33)


![classification](https://github.com/user-attachments/assets/2195ab21-ce2f-4cde-ae43-026b3eec82c4)



## **Tech Stack** 🛠  
- **Frontend & Deployment:** Streamlit  
- **Backend:** Python  
- **Deep Learning:** TensorFlow / Keras  
- **Libraries:** NumPy, PIL, TensorFlow, Streamlit  
- **Model File:** `keras_model.h5` (excluded from GitHub for size/security)

---

## **Installation & Setup** 🏗  

### 1. Clone the repository:

```bash
git clone https://github.com/mohammadhashim135/Waste-Classification-Management.git
cd your-repo-name
```
### **2. Create a Virtual Environment**
```bash
python -m venv .venv
# Activate it
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

### **3. Install Dependencies**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```


### **4. Start the Application**
```bash
streamlit run app.py

```
---

## **Usage Guide** 📝

🔹 **Click Browse Files or Use Camera to upload an image of the waste.**
🔹 **The model predicts whether the waste is Biodegradable or Non-Biodegradable.**
🔹 **View the prediction and take action accordingly.**
🔹 **You can re-upload to classify more waste.**

---

## **Project Structure** 📂
```bash
your_project/
│
├── app.py                      # Main Streamlit app file
├── keras_model_fixed.h5       # Pre-trained model for waste classification
├── labels.txt                 # Class labels for the model
├── sustainable_dev_goal/      # Folder containing SDG icons
│   ├── 12.png
│   ├── 13.png
│   ├── ...
└── requirements.txt           # Python package dependencies



```
---







---
## **Contributing** 🤝
Contributions are welcome! If you’d like to improve LetMeCut, feel free to fork the repo and submit a pull request.

### **Steps to Contribute:**
**Fork the repository**
### **1. Create a new branch:**
```bash
git checkout -b feature-branch
```

### **2. Make your changes and commit:**

```bash
git commit -m "Added new feature"
```
### **3. Push to the branch:**
```bash
git push origin feature-branch
```
### **Open a Pull Request**
---
## **License** 📜
This project is licensed under the MIT License.

💡 Developed with ❤️ by [Mohammad Hashim](https://github.com/mohammadhashim135/Waste-Classification-Management.git)

