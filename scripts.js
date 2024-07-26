document.getElementById('encodeForm').onsubmit = async function(e) {
    e.preventDefault();
    const text = document.getElementById('encodeText').value;
    const key = document.getElementById('encodeKey').value;

    try {
        const response = await fetch('https://arfus.pythonanywhere.com/encode', {  // HTTPS URL
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text, key })
        });
        const result = await response.json();
        if (response.ok) {
            document.getElementById('encodedResult').textContent = 'Encoded Text: ' + result.encoded_text;
        } else {
            document.getElementById('encodedResult').textContent = 'Error: ' + result.error;
        }
    } catch (error) {
        document.getElementById('encodedResult').textContent = 'Error: ' + error;
    }
};

document.getElementById('decodeForm').onsubmit = async function(e) {
    e.preventDefault();
    const text = document.getElementById('decodeText').value;
    const key = document.getElementById('decodeKey').value;

    try {
        const response = await fetch('https://arfus.pythonanywhere.com/decode', {  // HTTPS URL
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text, key })
        });
        const result = await response.json();
        if (response.ok) {
            document.getElementById('decodedResult').textContent = 'Decoded Text: ' + result.decoded_text;
        } else {
            document.getElementById('decodedResult').textContent = 'Error: ' + result.error;
        }
    } catch (error) {
        document.getElementById('decodedResult').textContent = 'Error: ' + error;
    }
};
