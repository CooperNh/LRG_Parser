import unittest
from xmltest import get_exons, get_sequence
import xml.etree.ElementTree as ET





class TestXMLParser(unittest.TestCase):

	def test_sequence(self):
	
		tree = ET.parse('LRG_test.xml')

		root = tree.getroot()
		
		self.assertEqual(get_sequence(root)  , "ATGCCCTG")
		

	def test_coordinates(self):
		tree = ET.parse ('LRG_test.xml')
		root = tree.getroot()
		exons = get_exons(root)
		self.assertEqual(exons[0][0]['label'], '1')
		self.assertEqual(exons[0][1]['strand'], '1')
		self.assertEqual(exons[0][1]['start'], '6019')
		self.assertEqual(exons[0][1]['end'], '7265')
		
		





	
		
if __name__ == '__main__':
    unittest.main()