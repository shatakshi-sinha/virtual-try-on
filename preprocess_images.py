from PIL import Image
import os

def preprocess_images(input_folder, output_folder, size=(256, 256)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for file_name in os.listdir(input_folder):
        img = Image.open(os.path.join(input_folder, file_name)).convert("RGB")
        img = img.resize(size)
        img.save(os.path.join(output_folder, file_name))

if __name__ == "__main__":
    preprocess_images("data/sample_images", "data/preprocessed_images")
