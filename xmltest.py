import xml.etree.ElementTree as ET




def get_sequence(root):
	"""
	This function extracts the DNA sequence from the LRG file
	returns a string of the sequence
	
	"""


	for fixed in root.findall('fixed_annotation'):
		sequence = fixed.find('sequence').text
		trans = fixed.get('transcript')
		return str(sequence)



def get_exons(root):

	all_exons =[]
	
	for exon in root.findall('fixed_annotation/transcript/exon'):
		exon_label = exon.attrib
		list_of_coord = exon.findall('coordinates')
	
		coordinates = list_of_coord[0].attrib
	
		all_exons.append([exon_label, coordinates])
		
	return all_exons


def display_exons(all_exons):
	for exon in all_exons:
		print (exon)

def main():


	tree = ET.parse('LRG_107.xml')

	root = tree.getroot()

	print(root)


	sequence = get_sequence(root)

	exons = get_exons(root)

	print (sequence)
	print (type(sequence))
	
	display_exons(exons)
	
	
if __name__ =='__main__':
	main()

