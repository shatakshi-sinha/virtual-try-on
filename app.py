from flask import Flask, request, jsonify
import torch
from models.generator import Generator
from utils.image_utils import generate_image, overlay_clothing

app = Flask(__name__)

# Load trained GAN generator
generator = Generator()
generator.load_state_dict(torch.load("models/generator.pth"))
generator.eval()

@app.route('/generate_image', methods=['POST'])
def generate_image_api():
    generated_image = generate_image(generator)
    return jsonify({"status": "Image generated successfully"})

@app.route('/virtual_tryon', methods=['POST'])
def virtual_tryon():
    user_image = request.files['user_image']
    clothing_image = request.files['clothing_image']
    output_image = overlay_clothing(user_image, clothing_image)
    return jsonify({"status": "Try-on completed successfully"})

if __name__ == "__main__":
    app.run(debug=True)
