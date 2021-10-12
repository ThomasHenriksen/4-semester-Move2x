import unittest
import ScreenShotBot
import SearchBot
import pyautogui as pg

class Test_test_1(unittest.TestCase):
    def test_A(self):
        ScreenShotBot.start
        SearchBot.start
        self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
