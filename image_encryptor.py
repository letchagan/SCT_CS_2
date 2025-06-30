from PIL import Image
import os

def encrypt_image(path, output_path, method='add', key=50):
    image = Image.open(path)
    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            if method == 'add':
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
            elif method == 'xor':
                r = r ^ key
                g = g ^ key
                b = b ^ key
            elif method == 'reverse':
                r, g, b = b, g, r
            pixels[x, y] = (r, g, b)

    image.save(output_path)
    print(f"[✔] Encrypted image saved as {output_path}")


def decrypt_image(path, output_path, method='add', key=50):
    image = Image.open(path)
    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            if method == 'add':
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
            elif method == 'xor':
                r = r ^ key
                g = g ^ key
                b = b ^ key
            elif method == 'reverse':
                r, g, b = b, g, r
            pixels[x, y] = (r, g, b)

    image.save(output_path)
    print(f"[✔] Decrypted image saved as {output_path}")

# Example usage
if __name__ == "__main__":
    input_path = "input/image.jpeg"
    encrypt_image(input_path, "output/encrypted.jpeg", method='xor', key=123)
    decrypt_image("output/encrypted.jpeg", "output/decrypted.jpeg", method='xor', key=123)
