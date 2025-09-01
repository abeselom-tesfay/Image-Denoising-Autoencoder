## Image Denoising Autoencoder

### Project Overview
This project implements an advanced image denoising system using a convolutional autoencoder with residual blocks. The model is trained on the CIFAR-10 dataset to remove noise from images, producing cleaner outputs while preserving essential details. The system evaluates performance using PSNR (Peak Signal-to-Noise Ratio) and SSIM (Structural Similarity Index) metrics.

### Features
- Advanced autoencoder architecture with residual connections for improved performance.
- Training with Gaussian and Salt & Pepper noise on CIFAR-10 dataset.
- Quantitative evaluation with PSNR and SSIM.
- Visualization of noisy input, denoised output, and original images.
- Model saved in `.keras` format for reuse.
- Streamlit deployment-ready for interactive demonstration.

