from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

# Helper function
def make_response(status, message, data=None):
    return jsonify({
        "status": status,
        "message": message,
        "data": data
    })

# Root route to load the form
@app.route('/')
def home():
    return render_template('form.html')

# Keyword extraction API
@app.route('/keywords', methods=['POST'])
def extract_keywords():
    data = request.get_json()

    if not data or 'text' not in data or not data['text'].strip():
        return make_response("error", "Text field is required", None), 400

    text = data['text']
    blob = TextBlob(text)
    nouns = list(blob.noun_phrases)[:3]  # Top 3 keywords

    return make_response("success", "Top keywords extracted", {"keywords": nouns}), 200

if __name__ == '__main__':
    app.run(debug=True)
