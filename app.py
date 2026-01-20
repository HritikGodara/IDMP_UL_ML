import streamlit as st
from transformers import pipeline
from PIL import Image
from plant_info import plant_data

# 1. Page Configuration
st.set_page_config(
    page_title="AyurVision AI",
    page_icon="🌿",
    layout="centered"
)

# 2. Load Model (Cached so it doesn't reload on every click)
@st.cache_resource
def load_model():
    # Replace './IDMP_UL_ML' with the actual path to your unzipped model folder
    # If running locally, ensure the folder exists.
    return pipeline('image-classification', model='.', device=-1)

# Display Header
st.title("🌿 AyurVision: Medicinal Plant Identifier")
st.write("Upload a raw material or plant image to identify its Ayurvedic properties.")

# 3. File Uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Show a loading spinner while processing
    with st.spinner('Analyzing plant features...'):
        try:
            # Load model and predict
            pipe = load_model()
            results = pipe(image)
            
            # Get top prediction
            top_prediction = results[0]
            label = top_prediction['label']
            confidence = top_prediction['score']

            # --- DISPLAY RESULTS ---
            st.divider()
            
            # Check confidence threshold
            if confidence < 0.40:
                st.error(f"⚠️ Low Confidence ({confidence*100:.1f}%). The model is unsure. This might not be a medicinal plant in our database.")
            else:
                st.success(f"**Identified:** {label} ({confidence*100:.1f}% Match)")
                
                # Fetch Info
                info = plant_data.get(label, plant_data["Default"])
                
                # Create Columns for neat display
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("### 🔬 Scientific Data")
                    st.write(f"**Name:** {info.get('Scientific Name')}")
                    st.write(f"**Uses:** {info.get('Uses')}")
                
                with col2:
                    st.markdown("### 🕉️ Ayurvedic Profile")
                    st.write(f"**Properties:** {info.get('Ayurvedic')}")
                
                # Show top 3 probabilities chart
                st.divider()
                st.subheader("Confidence Breakdown")
                chart_data = {res['label']: res['score'] for res in results[:3]}
                st.bar_chart(chart_data)

        except Exception as e:
            st.error(f"Error loading model: {e}")
            st.info("Make sure the 'IDMP_UL_ML' folder is in the same directory as this script.")