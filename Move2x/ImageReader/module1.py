import cv2 as cv
import pytesseract as tess
tess.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv.imread('tes.png')

def ocr_core(image):
    text = tess.image_to_string(image);
    return text

def get_grayscale(image):
    return cv.cv2.cvtColor(image, cv.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv.medianBlur(image, 5)

def thresholding(image):
    return cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

img = get_grayscale(img)
img = thresholding(img)
img = remove_noise(img)

print(ocr_core(img))