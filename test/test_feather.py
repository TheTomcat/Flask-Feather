from flask import Flask, render_template_string
from flask_feather import Feather, icons
from os import path

app = Flask(__name__)
feather = Feather(app)

def test_simple():
    with app.app_context():
        icon = render_template_string("{{ feather.icon('user-plus') }}")
        assert '<svg ' in icon
        assert '</svg>' in icon
        
        
def test_attr():
    with app.app_context():
        assert 'width="20"' in render_template_string("{{ feather.icon('aperture', width=20) }}")

def test_mod_attr():
    with app.app_context():
        assert 'stroke-width="20"' in render_template_string("{{ feather.icon('aperture', stroke_width=20) }}")

def test_custom_import():
    app = Flask(__name__)
    feather = Feather(app, import_dir=path.join('test','customsvg'))
    assert getattr(icons, 'menu_close') is not None