import redis
import sirope
import flask

from model.comment import Comment
from model.post import Post
from model.counter import Counter
from blueprints.main_blueprint import main_blueprint
from blueprints.post_blueprint import post_blueprint
from blueprints.comment_blueprint import comment_blueprint

# Configuración de la aplicación Flask
app = flask.Flask(__name__)
app.secret_key = "una_clave_secreta_y_unica"

# Registro de los blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(comment_blueprint)


def create_app():
    """
    Crea la aplicación Flask y la instancia de Sirope.
    """
    fapp = flask.Flask(__name__)
    fapp.secret_key = "una_clave_secreta_y_unica"
    sirp = sirope.Sirope()
    return fapp, sirp


app, srp = create_app()


@app.route('/')
def index():
    """
    Ruta principal de la aplicación.

    Carga las publicaciones y comentarios almacenados en Sirope, actualiza el contador de visitas
    y renderiza el template 'index.html' con los datos necesarios.
    """
    try:
        c = 0
        counters = srp.load_all(Counter)
        for counter in counters:
            c += 1
        if c == 0:
            counter = Counter()
            srp.save(counter)
        else:
            counters = srp.load_all(Counter)
            for counter_instance in counters:
                counter_instance.masUno()
                counter = counter_instance
                srp.save(counter)

        posts = list(srp.load_all(Post))
        sorted_posts = sorted(posts, key=lambda post: post.tiempo, reverse=True)
        comments = list(srp.load_all(Comment))
        sust = {
            "posts": sorted_posts,
            "comments": comments,
            "counter": counter
        }

        return flask.render_template('index.html', **sust)
    except redis.exceptions.ConnectionError as error:
        return flask.render_template('errorBaseDatos.html')
    except Exception as e:
        return flask.render_template('errorInesperado.html')


@app.route('/create_post', methods=['POST'])
def create_post():
    """
    Ruta para crear una nueva publicación.

    Obtiene los datos del formulario y crea un objeto Post. Luego, guarda el objeto en Sirope y redirige a la página principal.
    """
    title = flask.request.form.get('titulo')
    content = flask.request.form.get('publicacion')

    post = Post(title, content)

    srp.save(post)

    return flask.redirect('/')


@app.route('/create_comment/<post_id>', methods=['POST'])
def create_comment(post_id):
    """
    Ruta para crear un nuevo comentario.

    Obtiene el contenido del comentario y el ID de la publicación asociada. Luego, crea un objeto Comment, lo guarda en Sirope
    y redirige a la página principal.
    """
    content = flask.request.form.get('content')
    comment = Comment(content, post_id)

    srp.save(comment)

    return flask.redirect('/')


if __name__ == '__main__':
    # Inicio del servidor Flask
    app.run(debug=True)
