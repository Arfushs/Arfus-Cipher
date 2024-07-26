# Arfus Cipher

Arfus Cipher is a web application for encoding and decoding text. This project includes an API built with Flask and a user interface built with JavaScript.

## Usage

### Encoding

To encode text, follow these steps:

1. Open the web application.
2. In the encoding form, enter the text you want to encode and the key.
3. Click the "Encode" button.
4. The encoded text will be displayed on the screen.

### Decoding

To decode text, follow these steps:

1. Open the web application.
2. In the decoding form, enter the text you want to decode and the key.
3. Click the "Decode" button.
4. The decoded text will be displayed on the screen.

## API

Our Flask API is hosted on PythonAnywhere. You can access the API at the following URL:

[Arfus Cipher API](https://arfus.pythonanywhere.com)

### Encode Endpoint

- **URL:** `https://arfus.pythonanywhere.com/encode`
- **Method:** `POST`
- **Headers:**
  - `Content-Type: application/json`
- **Body:**
  ```json
  {
    "text": "Hello, World!",
    "key": "mysecretkey"
  }
