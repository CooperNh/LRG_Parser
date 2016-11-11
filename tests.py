import unittest
from xml_lrg_parser import get_exons, get_sequence, get_exon_sequence, get_gene_data, count_transcripts
import xml.etree.ElementTree as ET


tree = ET.parse ('test_files/genomic_sequence_test.xml')
root = tree.getroot()

tree_107 = ET.parse('test_files/exon_sequence_test.xml')
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

		
	def test_gene_data(self):
		gene_data = get_gene_data(root_107)
		
		self.assertEqual(gene_data[0], 'NG_009875.1')
		self.assertEqual(gene_data[1], 'LRG_107')
		self.assertEqual(gene_data[2], '20197')
		self.assertEqual(gene_data[3], 'SLC35C1')
		
	def test_count_transcripts(self):
		 
		 count = count_transcripts(root_107)
		 count2 = count_transcripts(root)
		 
		 self.assertEqual(count,1)
		 self.assertNotEqual(count,2)
		 self.assertEqual(count2, 2)
		 
		 

		
		
		
		
	
		
if __name__ == '__main__':
    unittest.main()