import controller.orderController as order
import controller.imageReaderController as ImageReader


class dymoModel(object):
    """description of class gets information from OCR/imageReader and store it"""
    label_val = b.customerNo
    label_product =  b.product + ' ' + b.productNo

