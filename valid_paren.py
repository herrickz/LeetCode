import unittest

# https://leetcode.com/problems/valid-parentheses/description/

def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    begin_paren_list = ['(', '[', '{']

    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = []

    for char in s:
        if char in begin_paren_list:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            
            possible_match = stack.pop(len(stack)-1)
            
            if mapping[char] != possible_match:
                return False

    if len(stack) > 0:
        return False

    return True

class TestValidParen(unittest.TestCase):

    def test_is_valid(self):
        input_val = '['
        expected = False
        actual = is_valid(input_val)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()