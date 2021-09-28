import sys as ir
import sys as dp
ir.path.append('..\ImageReader')
from service import imageReaderService as service
path = 'order2.jpg' 
list = service.OCR(path)

for b in list:
    print(b.customerNO)