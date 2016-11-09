import xml.etree.ElementTree as ET

tree = ET.parse('LRG_241_FIG4.xml')

root = tree.getroot()

print(root)


def get_sequence(root):



	for fixed in root.findall('fixed_annotation'):
		sequence = fixed.find('sequence').text
		trans = fixed.get('transcript')
		return sequence



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

sequence = get_sequence(root)

exons = get_exons(root)

print (sequence)
print (exons)
display_exons(exons)


"""
#print sequence
for fixed in root.findall('fixed_annotation'):
	sequence = fixed.find('sequence').text
	trans = fixed.get('transcript')
	print (sequence) 
	

for exon in root.findall('fixed_annotation/transcript/exon'):
	print (exon.attrib)
	for coordinates in root.findall ('fixed_annotation/transcript/exon/coordinates'):
		print (coordinates.attrib)

	exons = fixed.findall('coordinates')
	
	for coordinates in exons:
		print (coordinates.attrib, coordinates.tag)
	
	
#print each exon with exon information	
for exon in root.findall('fixed_annotation/transcript/exon'):
	print (exon.attrib)
	list_of_coord = exon.findall('coordinates')
	
	print (list_of_coord[0].attrib)
	
"""	
