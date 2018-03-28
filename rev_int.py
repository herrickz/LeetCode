import unittest

def rev_int(x):
        """
        :type x: int
        :rtype: int
        """
        int_str = str(x)
        is_negative = False
        
        if(int_str[0] == '-'):
            is_negative = True
            int_str = int_str[1:]
        
        ret_str = ""
        
        for char in int_str[::-1]:
            ret_str += char
            
        if(is_negative):
            ret_str = "-" + ret_str
            
        overflow_pos = pow(2, 31)
        overflow_neg = -1 * overflow_pos
        
        ret_int = int(ret_str)
        
        # check for overflow values
        if ret_int > overflow_pos:
            return 0
        elif ret_int < overflow_neg:
            return 0
        
        return ret_int

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        input_val = 21
        expected = 12
        actual = rev_int(input_val)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()