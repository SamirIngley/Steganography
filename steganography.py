from PIL import Image


def decode_image(file_location):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]
    
    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]
    
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    # To get RGB values for an image at X, Y:
    for i in range(x_size):
        for j in range(y_size):
            if int(bin(red_channel.getpixel((i, j)))[-1]) == 0:
                pixels[i, j] = (255, 255, 255)
            elif int(bin(red_channel.getpixel((i, j)))[-1]) == 1:
                pixels[i, j] = (0, 0, 0)
    decoded_image.save("images/decoded_image.png")



decode_image("images/encoded_sample.png")


def encode_image(text_to_encode):
    pass

## Encoding a secret message
# Now that we can decode secret messages, it’s only natural that we want to encode some too! Provided in the starter code are a pair of functions called `write_text()` and `encode_image()`. `write_text()` will take a string and convert it to a black and white image of the string. You may use it as a helper function in completing your implementation of `encode_image()`.

## Completing the Assignment
# ​
# You will need three things to complete this assignment:
# ​
# 1. `pip3 install Pillow`
# 2. Completed `steganography.py` code
# 3. Decoded image obtained from `sample.png`
# 4. A sample image with some encoded message in it from your `encode_image()` function
# ​
# Commit all three things to your GitHub repo.