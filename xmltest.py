import xml.etree.ElementTree as ET




def get_sequence(root):
	"""
	This function extracts the DNA sequence from the LRG file
	returns a string of the sequence	
	"""
	for fixed in root.findall('fixed_annotation'):
		sequence = fixed.find('sequence').text
		trans = fixed.get('transcript')		
		for base in sequence:
			assert base in ['A', 'C', 'T', 'G' ], 'Invalid base - must contain ATGC only'
		return str(sequence)
		
		
def get_gene_data(root):
	for fixed in root.findall('fixed_annotation'):
		sequence_source = fixed.find('sequence_source').text
		lrg_id = fixed.find('id').text
		hgnc_id = fixed.find('hgnc_id').text
	
	return [sequence_source, lrg_id, hgnc_id]
	
	
def create_text_file(gene_data, all_data):
	
	file = open((gene_data[1] + ".txt"), 'w')
	
	file.write(gene_data[0]+"\n")
	file.write(gene_data[1]+"\n")
	file.write(gene_data[2]+"\n")
	file.write(" "+"\n")

	
	for exon in all_data:
	
		file.write(exon[0]+"\n")
		file.write(str(exon[1])+"\n")
		file.write(str(exon[2])+"\n")
		file.write(exon[3]+"\n")
		file.write(" "+"\n")
		
	
	
	
	
	
def get_exons(root):

	all_exons =[]
	
	for exon in root.findall('fixed_annotation/transcript/exon'):
		exon_label = exon.attrib
		list_of_coord = exon.findall('coordinates')
	
		coordinates = list_of_coord[0].attrib
	
		all_exons.append([exon_label, coordinates])
		
	return all_exons

	
		
def get_exon_sequence(sequence, exon_list):
	exon_label = exon_list[0]['label']
	exon_start = exon_list[1]['start']
	exon_end = exon_list[1]['end']
	
	exon_start = int(exon_start)
	exon_end = int(exon_end)
	exon_start = exon_start - 1
	exon_end = exon_end 
	
	exon_sequence = sequence [exon_start:exon_end]
	
	assert exon_end > exon_start, 'Exon end is greater than exon start'
	
	return [exon_label, exon_start + 1, exon_end, exon_sequence]
	
		
		
		
		
		
		
		

def main():

	try:
		tree = ET.parse('LRG_107.xml')
	
	except:
		print ('Error: please load an XML file')
		return None
		
	root = tree.getroot()

	sequence = get_sequence(root)

	exons = get_exons(root)
	
	gene_data = get_gene_data(root)
	
	all_exon_data =[]
	
	for exon in exons:
		
		exon_data = get_exon_sequence(sequence, exon)
		
		all_exon_data.append(exon_data)
		
		

	create_text_file(gene_data, all_exon_data)
	
	
	
	"""
	print (get_gene_data(root))
	print (sequence)
	print (type(sequence))
	
	for exon in exons:
		exon_data = (get_exon_sequence(sequence, exon))
		print ('Exon ', exon_data[0])
		print ('Start ', exon_data[1])	
		print ('End ', exon_data[2])
		print ('Sequence ', exon_data[3])			
		
		print (' ')
	
	"""
	
	
	
		
if __name__ =='__main__':
	main()


	
	
	
	
	