# test_contrarift.py
"""
Tests for ContraRift module.
"""

import unittest
from contrarift import ContraRift

class TestContraRift(unittest.TestCase):
    """Test cases for ContraRift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ContraRift()
        self.assertIsInstance(instance, ContraRift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ContraRift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
