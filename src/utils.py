import cv2
import numpy as np
from PIL import Image

def pil_to_bgr(image):
    """
    Convierte una imagen PIL a formato BGR (OpenCV).
    
    Args:
        image: Imagen PIL
    
    Returns:
        numpy array en formato BGR
    """
    img_array = np.array(image)
    img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    return img_bgr

def bgr_to_pil(image_bgr):
    """
    Convierte una imagen BGR (OpenCV) a formato PIL.
    
    Args:
        image_bgr: numpy array en formato BGR.
    
    Returns:
        Imagen PIL
    """
    img_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(img_rgb)
    return pil_image

def load_image(uploaded_file):
    """
    Cargar una imagen desde un archivo subido.
    
    Args:
        uploaded_file: Archivo subido por Streamlit
    
    Returns:
        Imagen PIL en formato RGB.
    """
    image = Image.open(uploaded_file).convert('RGB')
    return image
        