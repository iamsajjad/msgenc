from PIL import Image

def decode_message_from_red_channel(image_path):
    # Open the steganography image and convert it to RGB
    stego_img = Image.open(image_path).convert('RGB')
    width, height = stego_img.size

    # Extract the least significant bit of the red channel to decode the binary message
    binary_message = ''
    i =  0
    while True:
        x, y = i % width, i // width
        r, _, _ = stego_img.getpixel((x, y))
        binary_message += str(r &  1)
        i +=  1
        # Break the loop if the last character is null, indicating the end of the message
        if len(binary_message) %  8 ==  0 and chr(int(binary_message[-8:],  2)) == '\x00':
            break

    # Convert the binary message to its original text format
    message = ''
    for i in range(0, len(binary_message),  8):
        message += chr(int(binary_message[i:i+8],  2))

    # Return the decoded message
    return message

# Usage example:
decoded_message = decode_message_from_red_channel('encoded_image.png')
print(decoded_message)
