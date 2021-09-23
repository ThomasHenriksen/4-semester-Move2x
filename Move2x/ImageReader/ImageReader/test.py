
import ImageReader

path = 'ocr-sample2.png' 

list = ImageReader.listOfWords(path)


print(list)

ImageReader.cv2.waitKey(0)