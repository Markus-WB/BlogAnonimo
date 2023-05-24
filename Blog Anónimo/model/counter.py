class Counter:
    
    # Constructor de la clase Counter.
    def __init__(self):

        self._counter = 1
        
    # Propiedad para obtener el valor del contador.
    @property    
    def counter(self):

        return self._counter

    # Método para incrementar el valor del contador en 0.5.
    def masUno(self):

        self._counter = self._counter + 0.5
