from PIL import Image
import pyocr
import cv2

tools = pyocr.get_available_tools()
tool = tools[0]
print(tool.get_name())

img = Image.open("test/images/ocr_test1.png")
txt = tool.image_to_string(
    img,
    lang='jpn+eng',
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)
print(txt)

img = Image.open("test/images/ocr_test2.png")
txt = tool.image_to_string(
    img,
    lang='jpn+eng',
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)
print(txt)
