import numpy as np
from PIL import Image

def image_to_matrix(image_path: str) -> np.ndarray:
    image = Image.open(image_path)

    image = image.convert("L")
    image = image.resize((28, 28))

    matrix = np.array(image, dtype=np.float32)

    matrix /= 255.0

    return matrix
