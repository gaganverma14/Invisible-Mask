import streamlit as st
import numpy as np
from PIL import Image
from image_mask import invisible_mask

st.set_page_config(page_title="Invisible Mask")
st.title("Invisible Mask")

uploaded = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

strength = st.slider(
    "Protection Strength",
    0.0, 1.0, 0.5
)

if uploaded:
    img = Image.open(uploaded).convert("RGB")
    img_np = np.array(img)

    st.image(img, caption="Original", use_container_width=True)

    protected = invisible_mask(img_np, strength)

    st.image(
        protected,
        caption="Protected Image",
        use_container_width=True
    )

    Image.fromarray(protected).save("protected.png")

    st.download_button(
        "Download Protected Image",
        open("protected.png", "rb"),
        "protected.png"
    )
