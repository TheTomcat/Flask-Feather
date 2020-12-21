from flask import Flask, render_template_string
from flask_feather import Feather

app = Flask(__name__)
feather = Feather(app)

@app.route('/')
def hello_world():
    return render_template_string("""<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Page Title</title>
</head>
<body>
    {{ feather.icon('user-plus') }}
    {{ feather.icon('user-minus', width=100, height=100) }}
    {{ feather.icon('aperture', stroke_width=0.1) }}
</body>
</html> 
    """)