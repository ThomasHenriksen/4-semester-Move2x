import ImageReader as OCR

path = 'order2.jpg' 
list = OCR.OcrOrder(path)
#OCR.saveToDatabase(list)
OCR.printOrder(list)