from flask import Flask, render_template, jsonify

# Create the application instance
app = Flask(__name__)
count = 100

# Create a URL route in our application for "/"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/decrement', methods=['POST'])
def decrement():
    global count
    if count > 0:
        count -= 1
    return jsonify(count=count)

# correr la aplicacion
if __name__ == "__main__":
    app.run(debug=True)