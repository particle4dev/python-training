import unittest
from module.fibonacci import fib, ifib

class fibonacci_test(unittest.TestCase):

  def test(self):
    ''' define a fibonacci module '''
    self.assertEqual(fib(7), 13)
    self.assertEqual(ifib(42), 267914296)

if __name__ == '__main__':
  unittest.main()
