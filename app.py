from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Work Tracker API Running 🚀"

@app.route('/log', methods=['POST'])
def log():
    data = request.json
    
    print("Received:", data)
    
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run()