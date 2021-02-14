import unittest
import test


class TestMain(unittest.TestCase):
    def setUp(self):
        print('\n setUp : AOP 개념 함수 \n')

    def test_add(self):
        '''코멘트 달 수 있음'''
        test_param = 10
        result = test.add(test_param)
        self.assertEqual(result, 15)

    # try/catch를 늘리는 것보다 나은 코드로 개선
    # def test_add2(self):
    #     test_param = 'asdasd'
    #     result = test.add(test_param)
    #     self.assertTrue(isinstance(result, TypeError))
    #
    # def test_add3(self):
    #     test_param = 'qwesdfgasd'
    #     result = test.add(test_param)
    #     self.assertIsInstance(result, TypeError)

    def test_add2(self):
        test_param = 'asdasd'
        result = test.add(test_param)
        self.assertEqual(result, 'number')

    def test_add3(self):
        test_param = 'qwesdfgasd'
        result = test.add(test_param)
        self.assertEqual(result, 'number')

    def test_add4(self):
        test_param = None
        result = test.add(test_param)
        self.assertEqual(result, 'number')

    def tearDown(self) -> None: print('\n 또 다른 AOP \n')
# main일때만 test
if __name__ == '__main__':
    unittest.main()

# console : python -m unitTest -v