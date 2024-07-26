from flask import Flask, request, render_template, jsonify
import random
import string
import json
import os

app = Flask(__name__)

def generate_shuffled_alphabet(key: str) -> str:
    random.seed(key)
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    return ''.join(alphabet)

def ArfusCipherEncoder(text: str, key: str) -> str:
    shuffled_alphabet = generate_shuffled_alphabet(key)
    encoded_text = ''
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            encoded_char = shuffled_alphabet[ord(char) - ord('a')]
            if is_upper:
                encoded_char = encoded_char.upper()
            encoded_text += encoded_char
        else:
            encoded_text += char
    return encoded_text

def ArfusCipherDecoder(text: str, key: str) -> str:
    shuffled_alphabet = generate_shuffled_alphabet(key)
    decoded_text = ''
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decoded_char = chr(shuffled_alphabet.index(char) + ord('a'))
            if is_upper:
                decoded_char = decoded_char.upper()
            decoded_text += decoded_char
        else:
            decoded_text += char
    return decoded_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    data = request.json
    text = data['text']
    key = data['key']
    encoded_text = ArfusCipherEncoder(text, key)
    return jsonify({"encoded_text": encoded_text})

@app.route('/decode', methods=['POST'])
def decode():
    data = request.json
    text = data['text']
    key = data['key']
    decoded_text = ArfusCipherDecoder(text, key)
    return jsonify({"decoded_text": decoded_text})

if __name__ == '__main__':
    app.run(debug=True)
