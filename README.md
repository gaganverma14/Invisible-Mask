Invisible Mask – AI-Resistant Image Protection

Invisible Mask is a privacy-focused image protection project that adds **imperceptible noise at the pixel, frequency, and bit levels** to images.  
The protected images look visually identical to humans but become **harder for AI/ML models to analyze, learn from, or reuse for training**.

This project is designed to work with **modern Python versions** and does **not rely on heavy deep-learning frameworks**, making it lightweight, fast, and future-proof.


Key Features

- ✅ Visually identical output for humans
- ✅ Invisible noise at:
  - Sub-pixel level  
  - Frequency (FFT) domain  
  - Least-significant-bit (LSB) level
- ✅ Degrades AI feature extraction and training
- ✅ Adjustable protection strength
- ✅ Simple Streamlit web interface
- ✅ Works on latest stable Python versions
- ❌ No PyTorch / TensorFlow dependency


How It Works (Concept)

AI vision models rely heavily on:
- Frequency-domain patterns
- Phase consistency
- Channel correlations
- Stable pixel statistics

Invisible Mask targets these weaknesses by:

1. Adding sub-pixel Gaussian noise 
   - Invisible to the human eye  
   - Breaks pixel-level consistency  

2. Injecting controlled frequency-domain phase & magnitude noise  
   - Preserves low-frequency visual structure  
   - Corrupts mid/high-frequency features used by AI  

3. Channel decorrelation
   - Disrupts RGB feature alignment  

4. Bit-level (LSB) perturbation
   - Confuses model training  
   - Remains imperceptible to humans  

The result is an image that looks normal but behaves differently for AI systems.


Installation & Setup: 

1️⃣ Clone the repository

git clone https://github.com/gaganverma14/invisible-mask.git
cd invisible-mask

2️⃣ Install dependencies
python -m pip install -r requirements.txt

3️⃣ Run the application
python -m streamlit run app.py
