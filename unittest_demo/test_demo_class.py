# -*- coding: utf-8 -*-

import unittest
from demo import minusex, addex, calculate
import config

'''
1.定义一个以test开头的函数作为测试用例【必须以test开头】
2.执行测试用例前都会先调用Setup函数【每个测试用例调用一次】或者setupClass函数【所有测试用例仅调用一次】
3.执行完测试用例后都会调用tearDown函数【多次】和tearDownClass函数【仅一次】
'''


class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("this setupclass() method only called once.\n")

    @classmethod
    def tearDownClass(cls):
        print("this teardownclass() method only called once too.\n")

    def setUp(self):
        print("do something before test : prepare environment.\n")

    def tearDown(self):
        print("do something after test : clean up.\n")

    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3, addex(1, 2))
        self.assertNotEqual(3, addex(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, minusex(3, 2))
        # self.assertNotEqual(1, minusex(3, 2))

    def test_calculate(self):
        try:
            calculate(1, 2)
            config.gValue = 0
        except Exception as e:
            config.gValue = 1
            print('Config.gValue=', config.gValue)
            print(repr(e))

    # Config.gValue 动态赋值不起作用(???)
    @unittest.skipIf(config.gValue == 0, "条件成立下才跳过")
    def test_minus_with_skip(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, minusex(3, 2))
        self.assertNotEqual(1, minusex(3, 2))

    def test_add_ex(self):
        self.assertNotEqual(1, 1, msg="error msg")

    def test_my_function(self):
        i = 0
        sum = 0
        while i <= 100:
            sum = sum + i
            i = i + 1
        return i

if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)
