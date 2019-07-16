from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/echo')
def echo():
    thing = request.args.get('thing')
    place = request.args.get('place')
    return render_template('flask3.html',thing=thing, place=place)

@app.route('/echoimproved')
def echo_improved():
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['place'] = request.args.get('place')
    return render_template('flask3.html',**kwargs)

app.run(port = 9999, debug = True)