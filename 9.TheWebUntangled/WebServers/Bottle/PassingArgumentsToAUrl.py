from bottle import route, run, static_file

@route('/')
def home():
    return static_file('index.html', root='9.TheWebUntangled/WebServers/Bottle')

@route('/echo/<thing>')
def echo(thing):
    return "Say hello to my little friend: %s!" % thing

run (host='localhost', port=9999)