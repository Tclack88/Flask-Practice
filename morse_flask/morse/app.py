from flask import Flask, render_template, request
from .morsefuncs import MorseTranslate, Filter


def create_app():

    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template('base.html')

    @app.route('/translate', methods=['POST'])
    def translate():
        original = Filter(request.values['original'])
        morse = MorseTranslate(original)
        print(morse)
        print(type(morse))
        return render_template('translate.html', original=original, morse=morse)

    return app
