import unittest
import test

class TestCase(unittest.TestCase):
    
    def test_add(self):
        result = test.add(3 , 6)
        act =  9 
        self.assertEqual(result , act , f'ไม่ผ่านค่าควรได้คือ {act} แต่ได้ {result}')
    def test_minus(self):
        result = test.minus(3, 6)
        act = -3
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %d แต่ได้ %d' % (act, result))
    def test_mul(self):
        result = test.multipy(3, 6)
        act = 18
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %d แต่ได้ %d' % (act, result))
    def test_div(self):
        result = test.divi(10, 2)
        act = 5
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %d แต่ได้ %d' % (act, result))



if __name__ == '__main__':
    unittest.main()
    
