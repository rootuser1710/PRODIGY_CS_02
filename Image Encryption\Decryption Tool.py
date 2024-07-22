from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    # Open the input image
    image = Image.open(input_image_path)
    image_array = np.array(image)

    # Encrypt the image by applying XOR with the key
    encrypted_array = image_array ^ key

    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image.save(output_image_path)

def decrypt_image(input_image_path, output_image_path, key):
    # Open the encrypted image
    image = Image.open(input_image_path)
    image_array = np.array(image)

    # Decrypt the image by applying XOR with the key
    decrypted_array = image_array ^ key

    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_array)
    decrypted_image.save(output_image_path)

# Example usage
input_image_path = 'C:\\Users\\lap\\Desktop\\input_image.png'
encrypted_image_path = 'encrypted_image.png' 
decrypted_image_path = 'decrypted_image.png'  
encryption_key = 897  # This key should be kept secret

# Encrypt the image
encrypt_image(input_image_path, encrypted_image_path, encryption_key)
print(f'Image encrypted and saved as {encrypted_image_path}')

# Decrypt the image
decrypt_image(encrypted_image_path, decrypted_image_path, encryption_key)
print(f'Image decrypted and saved as {decrypted_image_path}')
