from azul import Azul
from lcd import LCD
from tv_abstract_factory import TvAbstractFactory

class FactoryLcdAzul(TvAbstractFactory):

    def createColor(self):
        return Azul()
    
    def createTv(self):
        return LCD()