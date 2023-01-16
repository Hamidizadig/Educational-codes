# import unittest
# class MyTest(unittest.TestCase):
#     def test_sum(self):
#     self.assertEqual(23,23)



import unittest
import p3

class MyTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(p3.sum(10,13),23)
        self.assertEqual(p3.sum(2,0),2)
        self.assertEqual(p3.sum(-2,8),6)
        self.assertEqual(p3.sum(0,0),0)
        # self.assertNoEqual(p3.sum(20,12),25)
        
    def test_mul(self):
        self.assertEqual(p3.mul(1,20),20)
        self.assertEqual(p3.mul(4,8),32)
        self.assertEqual(p3.mul(4,0),0)
        self.assertEqual(p3.mul(25,-2),-50)        
        
    def test_div(self):
        self.assertEqual(p3.div(8,2),4)
        self.assertEqual(p3.div(25,2),12.5)
        self.assertEqual(p3.div(6,-3),-2)
        self.assertRaises(ZeroDivisionError,p3.div,12,0)

if __name__=='__main__':
    unittest.main()
# python -m unittest test_p3.py