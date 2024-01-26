
#!/usr/bin/env python3

from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    # Check if request has locale parameter and if it's supported
    requested_locale = request.args.get('locale')
    if requested_locale in app.config['LANGUAGES']:
        return requested_locale
    # Default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(debug=True)
