import unittest
from xml_lrg_parser import get_exons, get_sequence, get_exon_sequence
import xml.etree.ElementTree as ET


tree = ET.parse ('test_files/LRG_test.xml')
root = tree.getroot()

tree_107 = ET.parse('test_files/LRG_107.xml')
root_107 = tree_107.getroot()

class TestXMLParser(unittest.TestCase):
		
	def test_sequence(self):
	
		self.assertEqual(get_sequence(root)  , "ATGCCCTG")
		

	def test_coordinates(self):
		
		exons = get_exons(root)
		self.assertEqual(exons[0][0]['label'], '1')
		self.assertEqual(exons[0][1]['strand'], '1')
		self.assertEqual(exons[0][1]['start'], '6019')
		self.assertEqual(exons[0][1]['end'], '7265')
		
	def test_exon_sequence(self):
		
		list_of_exons_107 = get_exons(root_107)
		sequence_107 = get_sequence(root_107)
		
		first_exon = list_of_exons_107[0]
		
		exon_data = get_exon_sequence(sequence_107, first_exon)
		
		exon_data = exon_data[3]
			
		self.assertEqual( exon_data  , "AAGGCCACGTGGGGGCGTGTCAGGAAGTGAGTCCAGGGCCCGCCTCCCGGGGAGTCGGCCTCGGATGTCCGGAGGCTCCTGGGCTGAGCCGGCGACAGAGCCCGGGAAGGCAGCGAGACGTGGGCGCCGGCCCAGCCCCCTCCCGCGTCCTTCAGCCCCAAGCCCCGAGCCCCTCTGACCCTTCCGCAGCCCTCCCTCCAGCCGCGCCCGGCCTCCGGCAGCTCCCTGTACGCCTCCCTCCCCCTGCCCGCCCCTCCCTCCCACAGCCGCCCATGACGCCCTCTCGGCACCTCTTCCCACTCTGCCACGCGTCCTTTTCCTGCACCTTCGCCCCGCGTACCTACTCCTGCCCCGCCCTGCCATTCCTCTCCCCTCCCTTCTCTCTGCGACCCCTCCCTGTTAGGCCCCAGCCTCTTCTCCCCTCACAGGTCTTCTCTGTCCTGGCCTCACCGCCTTATCCTATTCCTCTCCCTTGCCCTGTGTCTTGTCTCAGAGCCCCCTCGGGGTGGGAGTAGGTTGTGGAGCAGCACAACTGGGCTCACCCCAAAGCAGAACTTCTCAATCCATGAGGACAATGGGGAGGCCTTTAGGCCAGCCCACATGTGACAATGGAGGGCTGCGGCTTCCTTGCGGAGAGCACAAGTGAGCTCACTGCCCTGGACTCCAGGGAATCAGAGTTCTGGCCGCGGGGTGACCCAGCTCCTCTGCTACCATGAATAGGGCCCCTCTGAAGCGGTCCAGGATCCTGCACATGGCGCTGACCGGGGCCTCAGACCCCTCTGCAGAGGCAGAGGCCAACGGGGAGAAGCCCTTTCTGCTGCGGGCATTGCAGATCGCGCTGGTGGTCTCCCTCTACTGGGTCACCTCCATCTCCATGGTGTTCCTTAATAAGTACCTGCTGGACAGCCCCTCCCTGCGGCTGGACACCCCCATCTTCGTCACCTTCTACCAGTGCCTGGTGACCACGCTGCTGTGCAAAGGCCTCAGCGCTCTGGCCGCCTGCTGCCCTGGTGCCGTGGACTTCCCCAGCTTGCGCCTGGACCTCAGGGTGGCCCGCAGCGTCCTGCCCCTGTCGGTGGTCTTCATCGGCATGATCACCTTCAATAACCTCTGCCTCAAGTACGTCGGTGTGGCCTTCTACAATGTGGGCCGCTCACTCACCACCGTCTTCAACGTGCTGCTCTCCTACCTGCTGCTCAAGCAGACCACCTCCTTCTATGCCCTGCTCACCTGCGGTATCATCATCG")

	
		
if __name__ == '__main__':
    unittest.main()