from alarma_libro import AlarmaLibro

class Bibloteca():
    def devuelveLibro(self,libro, alarma):
        if libro.estado == "MALO":
            alarma.notifyObservers()