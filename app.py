from flask import Flask, render_template,request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
# app = Flask(__name__, template_folder="templates")

debug = DebugToolbarExtension(app)

@app.route('/')
def prompt_form():
    prompts = story.prompts
    return render_template('prompt.html',prompts=prompts)

@app.route('/story')
def add_story():
    text = story.generate(request.args)
    return render_template('story.html',text=text)