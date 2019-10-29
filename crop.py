from PIL import Image
import os

def crop (image_path, coords, saved_location):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    cropped_image.show()

if __name__ == '__main__':
    pdf_list = []
    for file in os.listdir(os.getcwd()):
        if file.endswith(".pdf"):
            pdf_list.append(file)
