from PIL import Image
import struct

def encode_message_into_red_channel(image_path, message):
    # Open the image and ensure it's in RGB mode
    img = Image.open(image_path).convert("RGB")
    width, height = img.size

    # Convert the message to binary and pad it
    binary_message = ''.join(format(ord(i), '08b') for i in message)
    # Add a termination sequence (e.g.,  8 zeros)
    binary_message += '00000000'

    # Ensure the binary message can fit into the image
    assert len(binary_message) <= width * height *  8, "Message too long for the image."

    # Get pixel data from the image
    pixels = img.load()

    # Initialize a counter for the binary message
    msg_index =  0

    # Loop through each pixel in the image
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            
            # Only change the red channel if there's still part of the message left
            if msg_index < len(binary_message):
                # Modify the least significant bit of the red channel
                r = (r & ~1) | int(binary_message[msg_index])
                msg_index +=  1

            # Set the pixel with the modified red channel
            pixels[x, y] = (r, g, b)

    # Save the image with the encoded message
    img.save('encoded_image.png')

# Usage example:
encode_message_into_red_channel('image.png', 'This is my encoded massage 1234567890')
