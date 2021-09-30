import controller.orderController as order
import controller.imageReaderController as ImageReader


class dymoModel(object):
    """description of class gets information from OCR/imageReader and store it"""
    label_val = '192405' #b.customerNo
    label_product =  'Lillebro ost 291911' #b.product + ' ' + b.productNo
    label_timestamp = 'tid' # Here we need the time stamp from the card might be something like b.timestamp from OCR

