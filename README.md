# Notes -- creating a flask app

1. make an `__init__.py`:

    ```python
    from .app import create_app()

    APP = create_app()
    ```
2. make an `app.py`

    ```python
    from flask import Flask, render_template, request,  #etc....
    #(import other supporting functions)

    def create_app():
    
            app = Flask(__name__)

            @app.route('/')
            def root(): # the default page loaded when app starts
                    return render_template('base.html')

            @app.route('/function')
            def function():
                    blah
                    blah
                    arg1 = ...
                    arg2 = ...
                    return render_template('newpage.html', arg1=arg1, arg2=arg2)

    ```

3. make a `templates` directory and in it the corresponding html
(in the above example, it will be `base.html` and `newpage.html`)

4. Connect your definitions in "create\_app" with the HTML
Some notes:
- pass app.route to a function:
```python
@app.route('/func') <-- refers to the definition about to follow
def func():
        arg1 = ...
        .
        .
        .
        return render_template('newpage.html', arg1=arg1)
        (this allows arg1 to be called in the `newpage.html`
```
- def to HTML: in the HTML doc, calling arg1 is as simple as {{ arg1 }}
        eg:
        ```html
        <body>
                <h1> check it out: {% raw %}{{ arg1 }}{% endraw %} </h1>
        </body>
        ```
- HTML to def: in HTML specify 'name' field:
        ```html
        <form>
                <input type='text' name='thing_being_moved' value="unimportant text">
        </form>
        ```
and in the def of "create\_app" call it with ... get or post:
```python
@app.route(/func, methods=['GET'])
def func():
        incoming_value = request.values['thing_being_moved']
        more
        stuff
        return render_template(most likely)
```
