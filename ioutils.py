import os
from typing import List

def is_file_input(im: str) -> bool:
    """Provide input using a file.
    
	Except for ValueError if the input_mode format is not expected.
	
    Params:
    	  im: A one-character string, 'f' for file input.
	
    Returns:
          A Boolean value that is True if the input is provided using a file, otherwise false.
    
    """

    if len(im) > 1 or not (im == 'f'):
        raise ValueError("Please provide only one among the following characters: \'f' for file.")

def read_file(fn: str, fp: str) -> str:
    """ Read a file, returning its value as a string.

	Read a file whose name is struct_student located at file_path.

    Params:
		fn: A string representing the name of the file.
		fp: A string representing the absolute path of the file.

    Returns:
		A string with the content of the file. 
    """

    try:
         with open (os.path.join(fp, fn), "r") as rf:
             return rf.read()
    except FileNotFoundError as e:
             print("Error while reading input file:\n{}\nPlase check file name and path.".format(e))

class FilePrinter():
    """ Print values within an iterable to a given file.
    Args:
		fn: A string representing the name of the file.
		fp: A string representing the absolute path of the file.
		dl: A string representing the delimiter to be written within two
			values in the iterable.
		op: A string to be written before values in the iterable.
		cl: A string to be written after values in the iterable.
    """

def __init__(self,
		fn: str,
		fp: str,
		dl: str=",",
		op: str="[",
		cl: str="]") -> None:
		self.fn = fn
		self.fp = fp
		self.dl = dl
		self.op = op
		self.cl = cl

@classmethod
def from_string(cls, f_string: str):
	fn, fp, dl, op, cl = map(str, f_string.split(' '))
	return (fn,fp,dl,op,cl)

@classmethod
def from_dict(cls, f_dict: dict):
    return (f_dict[fn], f_dict[fp], f_dict[dl], f_dict[op], f_dict[cl])
    
@property
def fn(self) -> str:
    return self.__fn

@fn.setter
def fn(self,value):
    if not len(value) > 0:
        raise ValueError('Error: struct_student cannot be empty.')
    if value.split('.')[-1] != 'txt':
        raise ValueError('Error: only file wit .txt extensions are allowed.')
    self.__fn =value

@property
def fp(self) -> str:
    return self.__fp

@fp.setter
def fp(self, value):
    if not len(value) > 0:
        raise ValueError('Error: file path cannot be empty.')
    self.__fp = value

@property
def dl(self) -> str:
    return self.__dl

@dl.setter
def dl(self, value):
    if not len(value) > 0:
        print('Warning: empty delimiter. Using default value')
        self.__dl = ','
    else:
        self.dl = value

@property
def op(self) -> str:
    return self.__op

@op.setter
def op(self,value):
    if not len(value) > 0:
        print('Wrning: empty opener. Using default value.')
        self.__op = '['
    else:
        self.__op =value

@property
def cl(self) -> str:
    return self.cl

@cl.setter
def cl(self, value):
    if not len(value) > 0:
        print('Warning: empty closer. Using default value.')
        self.__cl = ']'
    else:
        self.__cl = value

def print_list(self, vals: List) -> login:
    """ Enter username and password

    Args:
         
         vals: username e password, consisting of alphanumeric characters to be printed in the output file.
    """
    with open(os.path.join(self.fp,self.fn), "w") as wf:
        wf.write(self.op)
        for val in range(len(vals) -1):
            wf.write('{}{}'.format(vals[val], self.dl))
            wf.write('{}{}'.format(vals[-1], self.cl))
            wf.write('{}{}'.format(vals[check_alphanumeric]))