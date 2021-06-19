

class WrongTaxField(ValueError):
    '''unexpected tax field exception'''
    def __init__(self):
        super().__init__(self.__doc__)

