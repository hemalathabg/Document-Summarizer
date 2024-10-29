# Document-Summarizer
Document Summarizer is a web application designed to help users quickly summarize long documents or text passages. This tool utilizes a pre-trained NLP model from Hugging Face's Transformers library to generate concise summaries, making it useful for students, researchers, and professionals who want a brief overview of lengthy content.
Features
Summarization: Generates a summary of the input text, capturing the main points in a concise format.
Web Interface: Simple and responsive web form for easy text input and summary display.
Interactive: Summaries are generated instantly and displayed within the same page.
Extensible: Potential for additional features like file uploads, length controls, and multi-language support.
Tech Stack
Backend: Flask (Python)
NLP Model: Hugging Face Transformers library with a pre-trained summarization model
Frontend: HTML, CSS (Bootstrap), JavaScript
Additional Libraries: PyTorch (for model inference)
Project Structure
php
Copy code
document_summarizer/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # HTML template for the front end
├── static/
│   └── style.css          # Custom CSS styling
├── requirements.txt       # Dependencies file
└── README.md              # Project readme
Getting Started
Prerequisites
Python 3.6 or later
Virtual environment (recommended)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/hemalathabg/document_summarizer.git
cd document_summarizer
Set up the virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
Access the application: Open your web browser and go to http://127.0.0.1:5000.

Usage
Enter the text you want to summarize in the text area.
Click the Summarize button to get a concise summary.
The generated summary will appear below the form.

Future Enhancements:-
File Upload Support: Allow users to upload .txt or .pdf files for summarization.
Adjustable Summary Length: Enable users to control the length of the generated summary.
Multi-language Support: Add support for summarization in multiple languages.
