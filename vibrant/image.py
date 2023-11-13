from typing_extensions import Self
from dataclasses import dataclass

@dataclass
class ImageData:
    data: 

class Image:
    def __init__(self) -> None: ...

    def load(self, image_source) -> Self: ...
    def clear() -> None: ... 
    def update(image_data ) -> None: ...
    def getWidth(): int
    def getHeight(): int
    def resize(targetWidth: int, targetHeight: int, ratio: int): None
    def getPixelCount(): int
    def getImageData(): ImageData
    def remove(): None
