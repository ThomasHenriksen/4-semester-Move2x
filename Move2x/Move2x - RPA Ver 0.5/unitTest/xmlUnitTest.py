import unittest
from script import xmlScript as xml

class xml_test_1(unittest.TestCase):
    def test_SaveOneElement(self):
        test = 'test'
        word = 'unit test'

        xml.createXml(test)
        xml.saveToXml(test, word)
        testWord = xml.readXml(test)
        
        self.assertEqual(word, testWord[0])
    def test_SaveOneElementFail(self):
        test = 'test'
        word = 'unit test'

        xml.createXml(test)
        xml.saveToXml(test, word)
        testWord = xml.readXml(test)

        self.assertNotEqual(test , testWord[0])
    def test_SaveListElement(self):
        test = 'ocr'
        customer = 10017
        time = '00:55'
        product = '3 pc black 1 fuse r (1213)'
        
        order = [customer, time, product]

        xml.createXml(test)
        xml.saveToXmlList(order)
        testWord = xml.readOrderXml(test)
        
        self.assertEqual(str(customer), testWord[0][0])
        self.assertEqual(time, testWord[0][1])
        self.assertEqual('3', testWord[0][2][0])
        self.assertEqual('black 1 fuse r (1213)', testWord[0][2][1])
    def test_SaveListElementFail(self):
        test = 'ocr'
        customer = 10017
        time = '00:55'
        product = '3 pc black 1 fuse r (1213)'
        
        order = [customer, time, product]

        xml.createXml(test)
        xml.saveToXmlList(order)
        testWord = xml.readOrderXml(test)
        
        self.assertNotEqual(customer, testWord[0][0])
        self.assertNotEqual(time +'1', testWord[0][1])
        self.assertNotEqual('4', testWord[0][2][0])
        self.assertNotEqual('black 2 fuse r (1213)', testWord[0][2][1])
if __name__ == '__main__':
    unittest.main()
