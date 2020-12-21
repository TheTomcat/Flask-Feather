from flask import Flask, render_template_string
from flask_feather import Feather

app = Flask(__name__)
feather = Feather(app)

def test_simple():
    with app.app_context():
        assert render_template_string("{{ feather.icon('user-plus') }}") == '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><line x1="20" y1="8" x2="20" y2="14"/><line x1="23" y1="11" x2="17" y2="11"/></svg>'
def test_attr():
    with app.app_context():
        assert 'width="20"' in render_template_string("{{ feather.icon('aperture', width=20) }}")