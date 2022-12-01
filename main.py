import sys
from PIL import Image

from ConvertToSeamless import convertToSeamless

if __name__ == "__main__":
    imgPath = sys.argv[1]
    originalImg = Image.open(imgPath)
    outputPath = imgPath.rsplit('.', 1)[0] + "_seamless.png"
    convertToSeamless(originalImg, outputPath)
