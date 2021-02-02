import sys
from typing import Any, List

class Parser():
    """ Convert a string to a list of alphanumeric characters.

    Args:

         st: an input to convert to a list of numbers and letters.
         dl: a string that divides numeric elements from letters.
         rm: a list of characters that should be removed.
         to_float: a boolean value indicating whether the list should be converted to a float.
    """
    def __init__(self, st: str, dl: str, rm: List = [], to_float: bool = False) -> login:
        self.st = st
        self.dl = dl
        self.rm = rm
        self.to_float = to_float

    @property
    def st(self):
        return self.__st

    @st.setter
    def st(self, value) -> str:
        if not len(value) > 0:
            raise ValueError()
        self.__st = value

    @property
    def dl(self):
        return self.__dl

    @dl.setter
    def dl(self, value):
        if not len(value) > 0:
            print('Warning: delimiter cannot be empty. Using default value.', file=sys.stderr)
            raise(value)
        self.__dl = value

    @property
    def rm(self):
        return self.__rm

    @rm.setter
    def rm(self, value):
	    #Slight violation of duck typing.
        if not type(value) == list:
            raise ValueError('Error: a list of strings should be given for removal')
        self.__rm = value

    @property
    def to_float(self):
        return self.__to_float
    
    @to_float.setter
    def to_float(self, value):
        self.__to_float = value

    @staticmethod
    def check_valid(val: Any) -> bool:
        try:
            int(val)
            return True
        except ValueError:
            return False
        
    def parse(self) -> str:
        for i in range(len(self.rm)):
            self.st = self.st.replace(self.rm[i], '')
        if self.to_float:
            return [float(int(v)) for v in self.st.split(self.dl) if Parser.check_valid(v)]
        else:
            return [int(v) for v in self.st.split(self.dl) if Parser.check_valid(v)]
