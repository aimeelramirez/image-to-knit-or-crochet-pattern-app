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

def extract_colors(image, pixel_size=10):
    # Pixelate image 
    img = image.resize((image.width // pixel_size, image.height // pixel_size), Image.NEAREST)
    
    # Collect unique colors
    colors = set()
    for y in range(img.height):
        for x in range(img.width):
            color = img.getpixel((x, y))
            colors.add(color)
    
    return colors

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
  # Pixelate the image
    pixel_size = int(request.form.get('pixel_size', 10))
    pixelated_img = pixelate_image(img, pixel_size)
    print(pixelated_img)
  # Extract colors
    colors = extract_colors(img, pixel_size)
    print("Extracted Colors:", colors)  # Debug line
  
  # Generate crochet pattern
    pattern = generate_crochet_pattern(pixelated_img)
    # return jsonify({'pattern': pattern})
    # Apply new data in post
    print(jsonify({'pattern': pattern,'img_px': pixelated_img, 'colors': list(colors)}))
    return jsonify({'pattern': pattern,'img_px': pixelated_img, 'colors': list(colors)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
