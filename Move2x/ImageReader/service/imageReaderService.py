import controller.orderController as order
import controller.imageReaderController as ImageReader

def OCR(path):
    listOfWords = ImageReader.listOfWords(path)
    orderlist = order.objOrder(listOfWords)
    return orderlist




        


