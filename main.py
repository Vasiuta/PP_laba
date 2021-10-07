from flask import Flask
import gevent.pywsgi

app = Flask(__name__)

@app.route('/api/v1/hello-world-4')
def hello():
  return "Hello World! 4", 200

if __name__ == "__main__":
  app_server = gevent.pywsgi.WSGIServer(('0.0.0.0', 3000), app)
  app_server.serve_forever()