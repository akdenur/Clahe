import cv2 as cv
import os

def process_image(imgPath, output_folder, rel_path):
    img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)
    
    # Görüntü yüklenemezse işlemi atla
    if img is None:
        print(f"Warning: Could not load image {imgPath}")
        return

    # CLAHE işlemi
    claheObj = cv.createCLAHE(clipLimit=5, tileGridSize=(8, 8))
    claheImg = claheObj.apply(img)

    # Klasör yapısını koruyarak kaydetme
    rel_output_folder = os.path.join(output_folder, os.path.dirname(rel_path))
    if not os.path.exists(rel_output_folder):
        os.makedirs(rel_output_folder)

    output_image_path = os.path.join(rel_output_folder, os.path.basename(imgPath))
    cv.imwrite(output_image_path, claheImg)

def histogramEqual():
    root = os.getcwd()
    mura_path = os.path.join(root, 'MURA-v1.1')

    # Masaüstünde 'output_images' klasörüne kaydet
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    output_folder = os.path.join(desktop_path, 'output_images')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Tüm alt klasörlerdeki resimleri bul ve işle
    for subdir, _, files in os.walk(mura_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                imgPath = os.path.join(subdir, file)
                rel_path = os.path.relpath(imgPath, mura_path)
                process_image(imgPath, output_folder, rel_path)

if __name__ == '__main__':
    histogramEqual()
