from bottle import route, run, static_file

@route('/') 
def main():
    return static_file('index.html',root='./9.TheWebUntangled/WebServers/Bottle')

run(host='localhost',port=9999)