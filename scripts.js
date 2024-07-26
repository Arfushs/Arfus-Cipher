document.getElementById('encodeForm').onsubmit = async function(e) {
    e.preventDefault();
    const text = document.getElementById('encodeText').value;
    const key = document.getElementById('encodeKey').value;

    const response = await fetch('http://arfus.pythonanywhere.com/encode', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, key })
    });
    const result = await response.json();
    document.getElementById('encodedResult').textContent = 'Encoded Text: ' + result.encoded_text;
};

document.getElementById('decodeForm').onsubmit = async function(e) {
    e.preventDefault();
    const text = document.getElementById('decodeText').value;
    const key = document.getElementById('decodeKey').value;

    const response = await fetch('http://arfus.pythonanywhere.com/decode', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, key })
    });
    const result = await response.json();
    document.getElementById('decodedResult').textContent = 'Decoded Text: ' + result.decoded_text;
};
