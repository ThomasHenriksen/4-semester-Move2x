def orders(customerNo, part, color, product, productNo):
    customerNO  = customerNo
    parts = part
    colors = color
    products = product
    productNos = productNo
    order = (customerNO, parts, colors, products,productNos )
    return order

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
         if(b != 'CUSTOMER' and b != 'PRODUCT' and b != 'pes'and b != 'pc' and b != '|' and b != 'pe' and b != 'ORDER' and b != 'TICKET' and b != '=' and b != 'TIME' and b != 'STAMP' and b != 'HH:MM' and b != 'FROM' and b != 'START' and b != '+—' ):
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
    
    
        
    
    return orderlist