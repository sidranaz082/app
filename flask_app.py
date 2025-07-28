from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

# Helper function for consistent responses
def make_response(status, message, data=None):
    return jsonify({
        "status": status,
        "message": message,
        "data": data
    })

# Route to show the HTML form
@app.route('/')
def home():
    return render_template('form.html')

# Route for keyword extraction
@app.route('/keywords', methods=['POST'])
def extract_keywords():
    data = request.get_json()

    # Validate input
    if not data or 'text' not in data or not data['text'].strip():
        return make_response("error", "Text field is required", None), 400

    # Extract keywords using TextBlob noun phrases
    text = data['text']
    blob = TextBlob(text)
    keywords = list(blob.noun_phrases)[:3]  # top 3

    return make_response("success", "Keywords extracted successfully", {"keywords": keywords}), 200


if __name__ == '__main__':
    app.run(debug=True)
