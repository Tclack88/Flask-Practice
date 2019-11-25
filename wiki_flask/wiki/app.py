from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from numpy.random import choice




def create_app():

    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template('base.html', title='Home') 


    @app.route('/generated', methods=['GET'])
    def RandomWiki():
        source = requests.get("https://en.wikipedia.org/wiki/Special:Random").text
        soup = BeautifulSoup(source,'html.parser')
        title = soup.find('title')
        paragraphs = soup.find_all('p',text=True)
                        # lessons learned. text=True. Ignores all the hyperlink
                        # and crap and just gives the text within the p-tag
        plist = []
        for i in paragraphs:
            if len(list(i.text)) > 0 and i.text != '\n':
                plist.append(i.text)
 
        if len(plist) < 1:
            return RandomWiki()
                        # So far, there seem to be 0 length or more. I assume
                        # that at least a 1 length paragraph is useful

 
        print(plist)

        contents = choice(plist)

        return render_template('generated.html', title=title.text, contents=contents)

    return app


