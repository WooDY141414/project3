import unittest

from app import checkLoginAndPassword


class MyTestCase(unittest.TestCase):
    def test_login_invalid(self):
        result = checkLoginAndPassword('12312','true')
        self.assertEqual(result, 'Неверно')  # add assertion here

    def test_login_valid(self):
        result = checkLoginAndPassword('vladnaumkin1@gmail.com','16587')
        self.assertEqual(result, 'Неверно')  # add assertion here
if __name__ == '__main__':
    unittest.main()
