from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>

<html>
    <head>
        <link rel="stylesheet"  href="styles.css"/>
    </head>
        <body>
        <form action="/hello" method="post">
           <label for="Rotate_by"> Rotate by:</label>   
            <input type="text" name="rot"/>
            <input type="textarea" name="text"/>
            <input type="submit"/>
        </form>
    </body>
</html>

"""


@app.route("/")
def index():
    return form

@app.route("/encrypt", methods=['post'])
def encrypt():
    Rotate_by = request.form['Rotate_by']
    return '<h1>encrypt,' + Rotate_by + '</h1>' 

app.run()