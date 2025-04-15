from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.layers import DepthwiseConv2D

def classify_waste(img):
    np.set_printoptions(suppress=True)
    try:
        model = tf.keras.models.load_model('keras_model_fixed.h5', custom_objects={'DepthwiseConv2D': DepthwiseConv2D})
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None
    try:
        with open("labels.txt", "r") as f:
            class_names = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        st.error("Labels file not found. Please ensure 'labels.txt' exists.")
        return None, None

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = img.convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    return class_name, confidence_score

st.set_page_config(layout='wide')
st.title("♻ Waste Classification Management App")
st.markdown("Upload a waste image to identify its type and understand its environmental impact.")

input_img = st.file_uploader("Upload an image (JPG, PNG, JPEG)", type=['jpg', 'png', 'jpeg'])

def get_carbon_footprint_info(label):
    label_clean = ''.join([c for c in label if not c.isdigit()]).strip().lower()
    label_clean = label_clean.replace("_", "").replace("-", "").replace(" ", "")

    carbon_info = {
        "cardboard": (
            "📦 **Cardboard Waste**:\n"
            "• Virgin cardboard: emits approx. **0.5–0.9 kg CO₂/kg**.\n"
            "• Recycled cardboard: **0.2–0.4 kg CO₂/kg**.\n"
            "♻ Recycling reduces water, energy use, and deforestation."
        ),
        "plastic": (
            "🧴 **Plastic Waste**:\n"
            "• PET (bottles): **2.1–3.5 kg CO₂/kg**.\n"
            "• HDPE (containers): **1.7–2.8 kg CO₂/kg**.\n"
            "• General plastic avg: **3–6 kg CO₂/kg**.\n"
            "♻ Recycling plastic saves up to 30–60% emissions."
        ),
        "glass": (
            "🍾 **Glass Waste**:\n"
            "• New glass: **0.6–1.2 kg CO₂/kg** due to melting.\n"
            "• Recycled glass: **0.2–0.4 kg CO₂/kg**.\n"
            "♻ Glass is 100% recyclable without quality loss."
        ),
        "metal": (
            "🛠 **Metal Waste**:\n"
            "• Aluminum: **10–13 kg CO₂/kg (virgin)**, **0.6–1 kg (recycled)**.\n"
            "• Steel: **1.8–2.5 kg CO₂/kg**, **~60% less if recycled**.\n"
            "♻ Recycling metals saves significant energy and emissions."
        ),
        "paper": (
            "📄 **Paper Waste**:\n"
            "• Virgin paper: **1.8–2.5 kg CO₂/kg**.\n"
            "• Recycled paper: **0.9–1.5 kg CO₂/kg**.\n"
            "♻ Recycling paper reduces landfill methane & preserves forests."
        ),
        "trash": (
            "🗑 **Mixed General Trash**:\n"
            "• Emissions vary **widely**: depends on materials, landfill gases, and incineration.\n"
            "• Can exceed **5 kg CO₂/kg**, especially with food & plastic mixed.\n"
            "♻ Waste separation and composting reduce footprint significantly."
        ),
    }

    return carbon_info.get(label_clean, "⚠ Carbon footprint information not available for this waste type.")

if input_img is not None:
    if st.button("Classify"):
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            st.info("Uploaded Image")
            st.image(input_img, use_container_width=True)

        with col2:
            st.info("Classification Result")
            image_file = Image.open(input_img)

            with st.spinner("Classifying image..."):
                label, confidence_score = classify_waste(image_file)

            if label:
                label_clean = label.strip().lower()
                

                col4, col5 = st.columns(2)
                if "cardboard" in label_clean:
                    st.success("The image is classified as **Cardboard**.")
                    with col4:
                        st.image("sustainable_dev_goal/12.png", use_container_width=True)
                        st.image("sustainable_dev_goal/13.png", use_container_width=True)
                    with col5:
                        st.image("sustainable_dev_goal/14.png", use_container_width=True)
                        st.image("sustainable_dev_goal/15.png", use_container_width=True)

                elif "plastic" in label_clean:
                    st.success("The image is classified as **Plastic**.")
                    with col4:
                        st.image("sustainable_dev_goal/6.jpg", use_container_width=True)
                        st.image("sustainable_dev_goal/12.png", use_container_width=True)
                    with col5:
                        st.image("sustainable_dev_goal/14.png", use_container_width=True)
                        st.image("sustainable_dev_goal/15.png", use_container_width=True)

                elif "glass" in label_clean:
                    st.success("The image is classified as **Glass**.")
                    with col4:
                        st.image("sustainable_dev_goal/12.png", use_container_width=True)
                    with col5:
                        st.image("sustainable_dev_goal/14.png", use_container_width=True)

                elif "metal" in label_clean:
                    st.success("The image is classified as **Metal**.")
                    with col4:
                        st.image("sustainable_dev_goal/3.png", use_container_width=True)
                        st.image("sustainable_dev_goal/6.jpg", use_container_width=True)
                    with col5:
                        st.image("sustainable_dev_goal/12.png", use_container_width=True)
                        st.image("sustainable_dev_goal/14.png", use_container_width=True)

                elif "paper" in label_clean:
                    st.success("The image is classified as **Paper**.")
                    with col4:
                        st.image("sustainable_dev_goal/12.png", use_container_width=True)
                        st.image("sustainable_dev_goal/13.png", use_container_width=True)
                    with col5:
                        st.image("sustainable_dev_goal/15.png", use_container_width=True)

                elif "trash" in label_clean:
                    st.warning("⚠ The image is classified as **Trash**.")
                    with col4:
                        st.image("sustainable_dev_goal/7.png", use_container_width=True)
                    with col5:
                        st.image("sustainable_dev_goal/12.png", use_container_width=True)

                else:
                    st.warning("The image is classified but doesn't match any supported waste type for SDG display.")
            # st.write(f"**Prediction:** {label}")
            st.write(f"**Confidence Score:** {confidence_score:.2%}")
        with col3:
            st.info("Carbon Footprint Awareness")
            if label:
                info = get_carbon_footprint_info(label)
                for line in info.split('\n'):
                    st.success(line)

try:
    with open("labels.txt", "r") as f:
        all_labels = [line.strip() for line in f.readlines()]
    with st.expander("View all class labels the model can predict"):
        st.write(all_labels)
except FileNotFoundError:
    st.error("Labels file not found. Please ensure 'labels.txt' exists.")
except Exception as e:
    st.error(f"An error occurred while loading the labels: {e}")

st.markdown("---")
st.caption("SDG (Sustainable Development Goals) icons are displayed based on classified waste to raise environmental awareness.")
