from PIL import Image

def convertToSeamless(originalImg, outputPath):
    imgH, imgW = originalImg.size
    dim = imgW
    if imgW > imgH:
        dim = imgH
    tempImg = originalImg.crop((0, 0, dim, dim))
    seamlessImg = Image.new("RGB", (dim * 2, dim * 2), "white")
    seamlessImg.paste(tempImg, (0, 0))
    tempImgLR = tempImg.transpose(Image.FLIP_LEFT_RIGHT)
    seamlessImg.paste(tempImgLR, (dim, 0))
    tempImgTB = tempImg.transpose(Image.FLIP_TOP_BOTTOM)
    seamlessImg.paste(tempImgTB, (0, dim))
    tempImg = tempImgTB.transpose(Image.FLIP_LEFT_RIGHT)
    seamlessImg.paste(tempImg, (dim, dim))
    seamlessImg.save(outputPath)
