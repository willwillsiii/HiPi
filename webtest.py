#!/usr/bin/python3
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class TextForm(FlaskForm):
    tts_text = StringField('Greeting', validators=[DataRequired()])
    submit = SubmitField('Send to HiPy!')


app = Flask(__name__)
app.config['token'] = '2gho^!2lciaj>H1n<&2bz(2$1fhz*2#$'

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
