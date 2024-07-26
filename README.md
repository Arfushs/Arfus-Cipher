# Arfus Cipher

Arfus Cipher, metinleri şifrelemek ve şifre çözmek için kullanılan bir web uygulamasıdır. Bu proje, Flask ile oluşturulmuş bir API'yi ve JavaScript ile oluşturulmuş bir kullanıcı arayüzünü içerir.

## Kullanım

### Encode İşlemi

Metni şifrelemek için aşağıdaki adımları izleyin:

1. Web uygulamasını açın.
2. Encode formunda şifrelemek istediğiniz metni ve anahtarı girin.
3. "Encode" butonuna tıklayın.
4. Şifrelenmiş metin ekranda görüntülenecektir.

### Decode İşlemi

Şifrelenmiş metni çözmek için aşağıdaki adımları izleyin:

1. Web uygulamasını açın.
2. Decode formunda şifresini çözmek istediğiniz metni ve anahtarı girin.
3. "Decode" butonuna tıklayın.
4. Çözülmüş metin ekranda görüntülenecektir.

## API

Flask API'miz PythonAnywhere üzerinde barındırılmaktadır. API'ye aşağıdaki URL üzerinden erişebilirsiniz:

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
