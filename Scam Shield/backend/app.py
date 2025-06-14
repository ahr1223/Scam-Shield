from flask import Flask, request, jsonify
from detector import is_scam_message


app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect():
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    result = is_scam_message(text)
    return jsonify({'is_scam': result})

if __name__ == '__main__':
    app.run(debug=True)
