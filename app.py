'''import openai
from gtts import gTTS
from flask import Flask, request, render_template, send_file
import os

# Set your OpenAI API key
openai.api_key = 'sk-proj-jdHOaEdSdrTTqvH6zHxfT3BlbkFJXXNl093zQTmZr4CuqS8F'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    input_text = request.form['input_text']
    
    # Generate text using OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input_text}
        ],
        max_tokens=50
    )

    # Extract the generated text
    generated_text = response['choices'][0]['message']['content'].strip()

    # Convert text to speech using gTTS
    tts = gTTS(generated_text, lang='en')
    
    # Define the output file path
    static_folder = os.path.join(os.getcwd(), "static")
    os.makedirs(static_folder, exist_ok=True)
    speech_file_path = os.path.join(static_folder, "speech.mp3")
    
    # Save the audio response to a file
    tts.save(speech_file_path)
    
    return send_file(speech_file_path, as_attachment=True, download_name="speech.mp3")

if __name__ == '__main__':
    app.run(debug=True)
'''

import openai
from gtts import gTTS
from flask import Flask, request, render_template, send_file
import os

# Set your OpenAI API key
openai.api_key = 'sk-proj-jdHOaEdSdrTTqvH6zHxfT3BlbkFJXXNl093zQTmZr4CuqS8F'

# Create a Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    input_text = request.form['input_text']
    
    # Generate text using OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input_text}
        ],
        max_tokens=4096  # Setting to a high value within the API's limit
    )

    # Extract the generated text
    generated_text = response['choices'][0]['message']['content'].strip()

    # Convert text to speech using gTTS
    tts = gTTS(generated_text, lang='en')
    
    # Define the output file path
    static_folder = os.path.join(os.getcwd(), "static")
    os.makedirs(static_folder, exist_ok=True)
    speech_file_path = os.path.join(static_folder, "speech.mp3")
    
    # Save the audio response to a file
    tts.save(speech_file_path)
    
    return send_file(speech_file_path, as_attachment=True, download_name="speech.mp3")

if __name__ == '__main__':
    app.run(debug=True)
