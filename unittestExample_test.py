import unittest

# JS style
#const assert = require('assert');
#describe('Array', function() {
#  describe('#indexOf()', function() {
#    it('should return -1 when the value is not present', function() {
#      assert.equal(-1, [1,2,3].indexOf(4));
#    });
#  });
#});

class Examples(unittest.TestCase):

  def setUp(self):
    print('method the testing framework will automatically call for every single test we run')

  def testIndexOf(self):
    '''should return 1 when the value is present'''
    self.assertEqual(["foo", "bar", "baz"].index("bar"), 1)
  
  def testCount(self):
    '''should return 1 when number of baz is 1'''
    self.assertEqual(["foo", "bar", "baz"].count("bar"), 1)

  def tearDown(self):
    print('a tearDown() method that tidies up after the test method has been run')

if __name__ == '__main__':
  unittest.main()
