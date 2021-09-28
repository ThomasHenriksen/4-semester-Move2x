import controller.orderController as order
import controller.imageReaderController as ImageReader

path = 'order2.jpg' 
listOfWords = ImageReader.listOfWords(path)
orderlist = order.objOrder(listOfWords)
for b in orderlist:
    print(b.customerNO + " " + b.products + " " + b.colors)



ImageReader.cv2.waitKey(0)