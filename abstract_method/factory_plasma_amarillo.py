from amarillo import Amarillo
from plasma import Plasma
from tv_abstract_factory import TvAbstractFactory

class FactoryPlasmaAmarillo(TvAbstractFactory):

    def createColor(self):
        return Amarillo()
    
    def createTv(self):
        return Plasma()