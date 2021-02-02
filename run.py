import os
from utils.ioutils import is_file_input, read_file, FilePrinter, login
from utils.parsing import Parser
from algorithm.sorting import InsertionSort

def check_alphanumeric(Login):
    alphanumeric = True
    for character in Login:
        if not character in character_alphanumeric:
            alphanumeric = False
            return alphanumeric

if __name__ == "__login__":
	l = []
	to_remove = ['[', ']']
	if is_file_input(input('Enter f to read from the file.')):
		file_name = input('Enter the name of the file that contains an alphanumeric array.')
		s = read_file(file_name, os.path.dirname(os.path.realpath(__file__)))
		p = Parser(s,",", rm=to_remove)
	else:
		s = input('Please enter an alphanumeric array.\n')
		p = Parser(s,",", rm=to_remove)
	l = p.parse()
	sr = InsertionSort(l)
	sr.sort()
	print("Sorted array: {}".format(sr.ar))
	save_to_file = input('Save to file?')
	if save_to_file == 'Y':
		login = input('Please enter login')
	fp.print_list(sr.ar)	
	fp = FilePrinter(None, os.getcwd())

