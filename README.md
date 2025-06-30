
# 🖼️ Image Encryption Tool using Pixel Manipulation

This is a simple yet powerful image encryption and decryption tool built using **Python and Pillow (PIL)**. Developed as **Task 2** for my **Cybersecurity Internship**, it demonstrates fundamental cryptographic operations through image pixel manipulation.

---

## 🔐 Features

- Load and process PNG/JPG images
- **Encrypt images** using:
  - Addition operation
  - XOR-based pixel manipulation
  - RGB channel swapping
- **Decrypt** images using the reverse operation
- Command-line interface for fast usage
- Easy to extend with more complex algorithms

---

## 🛠️ Technologies Used

- Python 3
- Pillow (PIL)

---

## 📁 Project Structure

```
image-encryption-tool/
├── image_encryptor.py
├── README.md
├── input/
│   └── your_image.png
├── output/
│   └── encrypted.png
│   └── decrypted.png
```

---

## ▶️ How to Use

1. Install Pillow if not installed:
```bash
pip install pillow
```

2. Place your image in the `input/` folder and rename it to `your_image.png` or change the path in the script.

3. Run the script:
```bash
python image_encryptor.py
```

This will:
- Encrypt the image using XOR (or 'add' / 'reverse')
- Save encrypted image in `output/encrypted.png`
- Then decrypt it and save as `output/decrypted.png`

---

## 🔧 Supported Encryption Methods

| Method    | Description                                  |
|-----------|----------------------------------------------|
| `add`     | Adds a constant to each RGB channel (mod 256)|
| `xor`     | XORs each pixel with a key (bitwise logic)   |
| `reverse` | Swaps Red and Blue channels                  |

---

## 🙋 Developed By

**Letchagan A**  
Cybersecurity Intern  
[GitHub](https://github.com/letchagan)

---

## 📜 License

This project is open-source under the MIT License.
