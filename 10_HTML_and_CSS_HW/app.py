from flask import Flask, request, send_from_directory
app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory('', 'hw.html')


@app.route('/<path:path>')
def send_static_file(path):
    return send_from_directory('', path)

if __name__ == "__main__":
  app.run(debug=True)

  