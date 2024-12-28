import cv2
import numpy as np

from cv2.typing import MatLike


def compute_saliency(image: MatLike) -> MatLike:
    """Takes in an opencv image and outputs a saliency mask"""

    yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

    mean = np.mean(yuv, axis=(0, 1))
    std = np.std(yuv, axis=(0, 1))

    mask = (np.abs(yuv - mean) / std >= 4.5).any(axis=2)
    mask_u8 = mask.astype(np.uint8) * 255

    return mask_u8


def find_largest_contour(
    image: MatLike, threshold: int = 5000
) -> tuple[int, int] | None:
    """Takes in opencv mask and returns the largest contour location (x, y) found larger than the threshold"""

    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    largest_contour = sorted(contours, key=cv2.contourArea, reverse=True)[0]

    area = cv2.contourArea(largest_contour)

    if area > threshold:
        moments = cv2.moments(largest_contour)

        cx = int(moments["m10"] / moments["m00"])
        cy = int(moments["m01"] / moments["m00"])

        return (cx, cy)
    else:
        return None
