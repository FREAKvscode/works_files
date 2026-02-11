def caesar_encrypt(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result = result + chr((ord(char) - base + shift) % 26 + base)
        else:
            result = result + char
    return result

def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)

with open("secret.txt", "r", encoding="utf-8") as f:
    original_text = f.read()

encrypted_text = caesar_encrypt(original_text)

with open("encrypted.txt", "w", encoding="utf-8") as f:
    f.write(encrypted_text)

with open("encrypted.txt", "r", encoding="utf-8") as f:
    encrypted_text_read = f.read()

decrypted_text = caesar_decrypt(encrypted_text_read)

with open("decrypted.txt", "w", encoding="utf-8") as f:
    f.write(decrypted_text)

