import uuid
from datetime import datetime

class Post:

    # Generación de un ID único para la publicación
    def __init__(self, title, content):
        
        self._post_id = str(uuid.uuid4())
        self._title = title
        self._content = content
        self._tiempo = datetime.now()

    # Propiedad para obtener el ID de la publicación
    @property
    def post_id(self):
   
        return self._post_id

    # Propiedad para obtener el título de la publicación
    @property
    def title(self):
        
        return self._title

    # Propiedad para obtener el tiempo de creación de la publicación
    @property
    def tiempo(self):

        return self._tiempo

    # Propiedad para obtener el contenido de la publicación
    @property
    def content(self):
        
        return self._content
