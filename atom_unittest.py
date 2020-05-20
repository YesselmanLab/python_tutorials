import atom
import unittest
import numpy as np

class AtomUnittest(unittest.TestCase):
    """Unit tests for the Atom Class"""
    def test_creation(self):
        """Testing the default and copy constructors"""
        target_string = "H1 1 2 3"
        first = atom.Atom("H1",np.array([1,2,3]))
        second = first.copy()
        self.assertTrue(target_string == str(first))
        self.assertTrue(target_string == str(second))
        
    def test_move(self):
        """Testing that Atom.move() functions properly """
        test_atom = atom.Atom("TEST", np.array([0,0,0]))
        test_atom.move([1,2,3])

        self.assertListEqual(list(test_atom.coords),[1,2,3])
        
        test_atom.move([-3,-3,-3])
        self.assertListEqual(list(test_atom.coords),[-2,-1,0])
    
    def test_repr_str_equivalent(self):
        """Testing that the __str__() and __repr__() methods produce equivalent, correct output"""
        target_string = "TEST -1000 0 1000"
        test_atom = atom.Atom("TEST",np.array([-1000,0,1000]))
        
        self.assertEqual(target_string,str(test_atom))
        self.assertEqual(str(test_atom),test_atom.__repr__())

if __name__ == '__main__':
    unittest.main()
