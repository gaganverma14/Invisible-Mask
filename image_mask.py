import numpy as np
import cv2

def invisible_mask(img, strength=0.5):
    """
    Stronger AI-confusing invisible noise
    img: uint8 RGB image
    strength: 0.0 – 1.0
    """

    img = img.astype(np.float32) / 255.0
    h, w, _ = img.shape

    sigma = 0.004 + 0.02 * strength
    noise = np.random.normal(0, sigma, img.shape)
    img_noisy = np.clip(img + noise, 0, 1)

    freq_img = np.zeros_like(img_noisy)

    for c in range(3):
        f = np.fft.fft2(img_noisy[:, :, c])
        fshift = np.fft.fftshift(f)

        y, x = np.ogrid[:h, :w]
        cy, cx = h // 2, w // 2
        dist = np.sqrt((y - cy)**2 + (x - cx)**2)

        low = min(h, w) * 0.04
        high = min(h, w) * (0.35 + 0.25 * strength)
        band = (dist > low) & (dist < high)

        phase_noise = np.random.normal(
            0, 0.12 * strength, fshift.shape
        )
        mag_noise = np.random.normal(
            0, 0.08 * strength, fshift.shape
        )

        fshift[band] *= (1 + mag_noise[band])
        fshift[band] *= np.exp(1j * phase_noise[band])

        f_ishift = np.fft.ifftshift(fshift)
        freq_img[:, :, c] = np.real(np.fft.ifft2(f_ishift))

    freq_img = np.clip(freq_img, 0, 1)

   
    freq_img[:, :, 1] += 0.015 * strength * freq_img[:, :, 0]
    freq_img[:, :, 2] -= 0.02 * strength * freq_img[:, :, 1]

    freq_img = np.clip(freq_img, 0, 1)

    bit_noise = np.random.randint(
        -4, 5, freq_img.shape
    ) * strength

    final = np.clip(freq_img * 255 + bit_noise, 0, 255)

    return final.astype(np.uint8)
