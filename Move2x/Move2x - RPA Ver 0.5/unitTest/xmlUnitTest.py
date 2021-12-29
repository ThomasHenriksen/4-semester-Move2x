import unittest
from script import xmlScript as xml

class xml_test_1(unittest.TestCase):
    def test_SaveOneElement(self):
        test = 'ocr'
        
        customer = 10017
        time = '00:55'
        product = '3 pc black 1 fuse r (1213)'
        order = [time,customer, product]

        xml.createXml(test)
        xml.saveOrder(order)
        testWord = xml.getOrder()
        
        self.assertEqual('10017', testWord[0][1])
    def test_SaveOneElementFail(self):
        test = 'ocr'
        
        customer = 10017
        time = '00:55'
        product = '3 pc black 1 fuse r (1213)'
        order = [time,customer, product]

        xml.createXml(test)
        xml.saveOrder(order)
        testWord = xml.getOrder()

        self.assertNotEqual('10018' , testWord[0][1])
    def test_SaveListElement(self):
        test = 'ocr'
        customer = 10017
        time = '00:55'
        product = ['3 pc black 1 fuse r (1213)']
        
        order = [customer, time, product]

        xml.createXml(test)
        xml.saveOrder(order)
        testWord = xml.getOrder()
        print(testWord[0][3])
        self.assertEqual('10017', testWord[0][2])
        self.assertEqual('00:55', testWord[0][1])
        self.assertEqual('3', testWord[0][3])
        self.assertEqual('Black 1 fuse R (1213)', testWord[0][4])

    def test_SaveListElementFail(self):
        test = 'ocr'
        customer = 10017
        time = '00:55'
        product = ['3 pc black 1 fuse r (1213)']
        
        order = [customer, time, product]

        xml.createXml(test)
        xml.saveOrder(order)
        testWord = xml.getOrder()
        
        self.assertNotEqual('10018', testWord[0][2])
        self.assertNotEqual('00:50', testWord[0][1])
        self.assertNotEqual('2', testWord[0][3])
        self.assertNotEqual('Black 1 fuse L (1213)', testWord[0][4])
if __name__ == '__main__':
    unittest.main()
