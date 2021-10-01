import sys 
sys.path.append('..\ImageReader')
from service import imageReaderService as service
list = service.OCR(path)
