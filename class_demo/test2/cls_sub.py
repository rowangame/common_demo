
from cls_base import CBase

class CSub(CBase):
    """
    __init__ method
    """
    def __init__(self):
        """
        __init__ inner annotations
        """
        super(CSub, self).__init__()
        print("CSub.__init__")

    def __new__(cls, *args, **kwargs):
        print("CSub.__new__\n")
        return super().__new__(cls)
    
    def __del__(self):
        print("CSub.__del__\n")
        super(CSub, self).__del__()
    
    """
    sub class extends cbase
    """
    def testThis(self):
        print("testThis\n")