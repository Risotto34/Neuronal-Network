import numpy as np
from PIL import Image

def image_to_matrix(image_path: str, threshold: float = 0.5, resize: tuple | None = None) -> np.ndarray:
    image = Image.open(image_path)

    image = image.convert("L")
    if resize is not None:
        image = image.resize(resize)

    matrix = np.array(image, dtype=np.float32)

    matrix = matrix / 255.0

    matrix = (matrix < threshold).astype(np.float32)

    return matrix
