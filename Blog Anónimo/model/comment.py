import uuid
from datetime import datetime

# Constructor de la clase Comment.
class Comment:
    def __init__(self, content, post_id):

        # Generación de un ID único para el comentario
        self._comment_id = str(uuid.uuid4())
        self._content = content
        self._tiempo = datetime.now()
        self._post_id = post_id

    # Propiedad para obtener el ID del comentario.
    @property
    def comment_id(self):
  
        return self._comment_id

    # Propiedad para obtener el tiempo de creación del comentario.
    @property
    def tiempo(self):

        return self._tiempo
    
    # Propiedad para obtener el contenido del comentario.
    @property
    def content(self):

        return self._content
    
    # Propiedad para obtener el ID de la publicación asociada al comentario.
    @property
    def post_id(self):
 
        return self._post_id

    # Método para representar el objeto Comment como una cadena de texto.
    def __str__(self):

        return f"Name: {self._content} {self._post_id}"
