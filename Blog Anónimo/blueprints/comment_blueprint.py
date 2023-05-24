import flask
from model.comment import Comment
from blueprints.main_blueprint import srp

# Creación del blueprint para comentarios
comment_blueprint = flask.Blueprint('comment', __name__)

@comment_blueprint.route('/create_comment/<post_id>', methods=['POST'])

# Función para crear un comentario en una publicación específica.
def create_comment(post_id):
    
    # Obtención del contenido del comentario desde el formulario de la solicitud
    content = flask.request.form.get('content')

    # Creación de un objeto Comment con el contenido y el ID de la publicación
    comment = Comment(content, post_id)

    # Guardar el objeto Comment en la base de datos utilizando Sirope
    srp.save(comment)

    # Redirección a la página de inicio
    return flask.redirect('/')

