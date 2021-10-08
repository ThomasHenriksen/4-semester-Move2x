from model import order as orders
def catchWordsToMakeOrder(list):
    orderl = ''
    orderList = []
    i = 0
    index = 0
    while i < len(list):
         b = list[i]
         b = b.replace('.', '')
         b = b.replace('(', '')
         b = b.replace(')', '')
         print(list[i])
         if(b != 'CUSTOMER' and b != 'PRODUCT' and b != 'pes' and b != 'pc' and b != '|' and b != 'pe' and b != 'ORDER' and b != 'TICKET' and b != '=' and b != 'TIME' and b != 'STAMP' and b != 'HH:MM' and b != 'FROM' and b != 'START' and b != '+—'):
              if(b.isnumeric()):
                  if(int(b) > 10000):
                       if(index == 0):
                            orderl += b + ' ' 
                       else:
                            orderList.append(orderl)
                            orderl = ''
                            orderl += b + ' ' 
                       index += 1
                  else:
                         orderl += b + ' ' 
              else:
                  orderl += b + ' ' 
         i += 1
    orderList.append(orderl)
    return orderList
 

def objOrder(orderList):
    orderlist = catchWordsToMakeOrder(orderList)
    objOrderList = []
    ifFuseIsInOrder = 'fuse'
    for b in orderlist:
        words = b.split()
        if ifFuseIsInOrder in b:
            od = orders.order(words[0], words[1], words[2], words[3] + ' ' + words[4] + ' ' + words[5], words[6])
            objOrderList.append(od)
        elif len(words) > 5:
            od = orders.order(words[0], words[1], words[2], words[3], words[4])
            objOrderList.append(od)
            od = orders.order(words[0], words[5], words[6], words[7], words[8])
            objOrderList.append(od)
        else:
            od = orders.order(words[0], words[1], words[2], words[3], words[4])
            objOrderList.append(od)
       
        
    
    return objOrderList