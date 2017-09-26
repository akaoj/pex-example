import os

import flask
import jinja2

# Because the files will be packaged in the pex, they're not where you would
# think they are
TEMPLATES_FOLDER = os.path.join(os.path.dirname(__file__), 'templates')


def main():
    app = flask.Flask(__name__)

    @app.route('/')
    def get():
        firstname = flask.request.args.get('firstname')
        lastname = flask.request.args.get('lastname')

        template = ""

        with open(os.path.join(TEMPLATES_FOLDER, 'hello_world.j2'), 'r') as f:
            template = jinja2.Environment().from_string(f.read()).render(
                firstname=firstname,
                lastname=lastname
            )

        return template

    app.run()
