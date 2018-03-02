#!/usr/bin/python3
from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from tts_player import play_tts
from pygame import mixer

class TextForm(FlaskForm):
    tts_text = StringField('Greeting', validators=[DataRequired()])
    submit = SubmitField('Send to HiPy!')


app = Flask(__name__)
app.config['SECRET_KEY'] = '2gho^!2Lciaj>Hyn<&2bz(2$1Fhz*2#$'

@app.route('/', methods=['GET', 'POST'])
def index():
    tts_form = TextForm()
    print(tts_form.tts_text.data)
    if tts_form.validate_on_submit():
        flash('Sent!')
        print(tts_form.tts_text.data)
        mixer.init()
        play_tts(tts_form.tts_text.data, mixer)
        # comment the next line to prevent reloading and clearing of form
        #return redirect(url_for('index'))
    return render_template('index.html', form=tts_form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
