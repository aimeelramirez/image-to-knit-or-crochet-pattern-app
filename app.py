from flask import Flask, request, jsonify
from PIL import Image
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
# Enable CORS for all routes

def pixelate_image(image, pixel_size):
    img = image.resize((image.width // pixel_size, image.height // pixel_size), Image.NEAREST)
    img = img.resize((img.width * pixel_size, img.height * pixel_size), Image.NEAREST)
    return img

def generate_crochet_pattern(pixelated_image):
    stitch_map = {
        (255, 255, 255): 'single crochet',  # white
        (0, 0, 0): 'double crochet',        # black
        (255, 0, 0): 'slip stitch',          # red
        (0, 255, 0): 'half double crochet',  # green
        (0, 0, 255): 'triple crochet',       # blue
      
    }

    pattern = []
    for y in range(pixelated_image.height):
        row = []
        for x in range(pixelated_image.width):
            color = pixelated_image.getpixel((x, y))
            stitch = stitch_map.get(color, 'unknown stitch')
            row.append(stitch)
        pattern.append(row)

    return pattern

@app.route('/process_image', methods=['POST'])
def process_image():
    file = request.files['image']
    img = Image.open(file.stream)
    pixel_size = int(request.form.get('pixel_size', 10))
    pixelated_img = pixelate_image(img, pixel_size)
    
    # Print pixel colors for debugging
    colors = set()
    for y in range(pixelated_img.height):
        for x in range(pixelated_img.width):
            color = pixelated_img.getpixel((x, y))
            colors.add(color)
    
    print("Colors in the pixelated image:", colors)  
    
    pattern = generate_crochet_pattern(pixelated_img)
    return jsonify({'pattern': pattern})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
