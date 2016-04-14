import os

from flask.ext.bower import Bower
from flask.ext.assets import Environment, Bundle


def load_assets(app):
    Bower(app)
    env = Environment(app)
    app.config['COMPASS_CONFIG'] = {'sourcemap': True}
    env.load_path = [
        os.path.join(os.path.dirname(__file__), 'bower_components'),
        os.path.join(os.path.dirname(__file__), 'styles'),
    ]
    # env.cache = False
    # env.manifest = False

    env.register(
        'js_all',
        Bundle(
            'jquery/dist/jquery.min.js',
            'bootstrap-sass/assets/javascripts/bootstrap.min.js',
            output='js_all.js'
        )
    )

    env.register(
        'css_all',
        Bundle(
            'all.scss',
            depends='*.scss',
            filters='compass',
            output='css_all.css'
        )
    )
