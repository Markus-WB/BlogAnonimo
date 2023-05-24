import flask
from model.post import Post
from blueprints.main_blueprint import srp

# Creación del blueprint para publicaciones
post_blueprint = flask.Blueprint('post', __name__)

@post_blueprint.route('/create_post', methods=['POST'])

# Función para crear una nueva publicación.
def create_post():

    # Obtención del título y contenido de la publicación desde el formulario de la solicitud
    title = flask.request.form.get('titulo')
    content = flask.request.form.get('publicacion')

    # Creación de un objeto Post con el título y contenido
    post = Post(title, content)

    # Guardar el objeto Post en la base de datos utilizando Sirope
    srp.save(post)

    # Redirección a la página de inicio
    return flask.redirect('/')
