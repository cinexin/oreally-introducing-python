# 9.1 Install flask...
# 9.2 Build a skeleton website...
# 9.3 Add a home() function to handle requests for the home page
# Set it up to return the string "'It's alive!"
'''
9.4 Create a Jinja2 template file called home.html
9.5 Modify your server's home()
'''
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/ping')
def ping():
    return "It's alive!"

@app.route('/')
def home():
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['height'] = request.args.get('height')
    kwargs['color'] = request.args.get('color')
    return render_template('home.html',**kwargs)


with app.app_context():
    app.run(port=5000, debug=True)
