# Flask Feather

[![Build Status](https://travis-ci.com/TheTomcat/Flask-Feather.svg?branch=main)](https://travis-ci.com/TheTomcat/Flask-Feather)
![GitHub](https://img.shields.io/github/license/TheTomcat/Flask-Feather)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flask-feather)

A simple Tag (`{% icon "name" %}`) to implement [Feather Icons](https://feathericons.com) in Flask. This is largely based of the library [django_feather](https://github.com/jnsdrtlf/django-feather) by [Jonas Drotleff](https://github.com/jnsdrtlf/).

## Install

Install `flask-feather` using `pip`.

```bash
pip install flask-feather
```  

## Quick Start

Firstly, initialise the extension within your Flask context

```python
from flask_feather import Feather
feather = Feather(app)
```

This extension also supports the [Flask application factory pattern](http://flask.pocoo.org/docs/latest/patterns/appfactories/) by allowing you to create a Feather object and then initialised it separately for an app:

```python
feather = Feather()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    feather.init_app(app)
```

## Usage

It's pretty simple to use this package. From within a jinja template:

```jinjatemplate
<p>{{ feather.icon('icon-name', width=32, height=32) }}</p>
```

The `icon` function takes the SVG source from the Feather project, applies additional attributes and return the SVG tag.

## Performance

`flask-feather` borrows the application structure from `django-feather` and does not read the `.svg`
files each time an icon is rendered. Instead, on installation, all the icons are written to a `.py` file.
All icons are rendered on the server side, avoiding the need to call `feather.replace()` after the page has loaded.

## License

Feather is licensed under the [MIT License](https://github.com/colebemis/feather/blob/master/LICENSE).

`flask-feather` is a derivative work of `django-feather`, both of which are licensed under the Apache License, Version 2.0:

```license
    Modifications Copyright 2020 Tom Vos <tjvos1@gmail.com>
    
    Original Django-feather Copyright 2020 Jonas Drotleff <j.drotleff@desk-lab.de>
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
       http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
```
