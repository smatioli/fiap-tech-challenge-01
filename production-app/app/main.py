from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data - in a real application, this would typically be a database
items = []

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API!"})

if __name__ == '__main__':
    app.run(debug=True)
