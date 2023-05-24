import flask
import sirope
import redis
from model.post import Post
from model.counter import Counter

# Creación del blueprint principal
main_blueprint = flask.Blueprint('main', __name__)

# Instancia de Sirope para interactuar con la base de datos
srp = sirope.Sirope()

@main_blueprint.route('/')

# Función para mostrar la página de inicio del sistema.
def index():

    try:
        # Conteo de los objetos Counter en la base de datos
        c = 0
        counters = srp.load_all(Counter)
        for counter in counters:
            c += 1

        # Si no hay ningún contador, se crea uno nuevo y se guarda en la base de datos
        if c == 0:
            counter = Counter()
            srp.save(counter)
        else:
            # Si hay contadores, se incrementa en uno el valor de cada uno y se guarda
            counters = srp.load_all(Counter)
            for counter_instance in counters:
                counter_instance.masUno()
                counter = counter_instance
                srp.save(counter)

        # Carga y ordenamiento de las publicaciones
        posts = list(srp.load_all(Post))
        sorted_posts = sorted(posts, key=lambda post: post.tiempo, reverse=True)

        # Datos a pasar a la plantilla para su renderización
        sust = {
            "posts": sorted_posts,
            "counter": counter
        }

        # Renderización de la plantilla index.html con los datos proporcionados
        return flask.render_template('index.html', **sust)
    except redis.exceptions.ConnectionError as error:
        # Manejo de errores de conexión con la base de datos Redis
        return flask.render_template('errorBaseDatos.html')
    except Exception as e:
        # Manejo de errores inesperados
        return flask.render_template('errorInesperado.html')
