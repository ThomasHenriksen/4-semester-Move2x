import order
import ImageReader

path = 'order2.jpg' 
listOfWords = ImageReader.listOfWords(path)
orderlist = order.objOrder(listOfWords)
print(orderlist)



ImageReader.cv2.waitKey(0)