from flask import Flask, render_template
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import pprint
import inspect
import sys
app = Flask(__name__)

@app.route("/foo")
def foo():
    return "foo"

@app.route("/")
def index():
    routes = [key for key in app.url_map._rules_by_endpoint if key != 'static']

    sources = [inspect.getsource(getattr(sys.modules[__name__], r)) for r in routes]
    highlights = [highlight(s, PythonLexer(), HtmlFormatter(noclasses=True)) for s in sources]

    return render_template('index.html', routes=highlights)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
