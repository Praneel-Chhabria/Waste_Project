import streamlit as st
import json
from PIL import Image
import waste_classifier

st.set_page_config(
    page_title="Waste Classification System", 
    layout="wide"
)

st.title("Waste Classification System")
st.write("Upload an image of waste to determine the correct disposal category.")
st.markdown("---")

column_left, column_right = st.columns([1, 1])

with column_left:
    st.subheader("Image Input")
    uploaded_file = st.file_uploader("Select an image file", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Image ready for analysis", use_column_width=True)

with column_right:
    st.subheader("Analysis Output")
    
    if uploaded_file is None:
        st.info("System standby. Waiting for image upload.")
    else:
        if st.button("Classify Material", type="primary"):
            with st.spinner("Processing image data..."):
                backend_response = waste_classifier.classify_waste_image(image)
                
                try:
                    if isinstance(backend_response, dict):
                        result_data = backend_response
                    else:
                        result_data = json.loads(backend_response)
                    
                    detected_item = result_data.get("item", "Unknown")
                    waste_category = result_data.get("category", "Unknown")
                    ai_confidence = result_data.get("confidence", 0.0)
                    disposal_instruction = result_data.get("instruction", "No instructions available.")
                    
                    st.write("### Results")
                    st.write(f"**Identified Object:** {detected_item}")
                    st.write(f"**Classification:** {waste_category}")
                    
                    confidence_percentage = float(ai_confidence) * 100
                    st.write(f"**System Confidence:** {confidence_percentage:.1f}%")
                    
                    st.markdown("---")
                    st.write("**Disposal Action Required:**")
                    
                    if "Wet" in waste_category or "Organic" in waste_category:
                        st.success(disposal_instruction)
                    elif "Hazardous" in waste_category:
                        st.error(disposal_instruction)
                    else:
                        st.info(disposal_instruction)
                        
                except json.JSONDecodeError:
                    st.error("System Error: Failed to parse backend data.")

                    st.write("Raw Output:", backend_response)
