import json

from fast_autocomplete import AutoComplete
from flask import escape, Flask

with open('words.json', 'r') as f:
    words = f.read()

words = json.loads(words)
autocomplete = AutoComplete(words=words)

app = Flask(__name__)

app.config.update(
    AUTOCOMPLETE=autocomplete
)

@app.route("/")
def root():
    return "OK"

@app.route("/complete/<text>")
def complete(text):
    text = escape(text)
    return str(app.config['AUTOCOMPLETE'].search(word=text))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")