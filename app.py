# app.py

from flask import Flask, render_template, request, jsonify
from transformers import pipeline

# Initialize Flask app and summarizer pipeline
app = Flask(__name__)
summarizer = pipeline("summarization")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form.get('text')
    if not text:
        return jsonify({'error': 'Please provide text to summarize'}), 400

    # Perform summarization
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return jsonify({'summary': summary[0]['summary_text']})

if __name__ == '__main__':
    app.run(debug=True)
