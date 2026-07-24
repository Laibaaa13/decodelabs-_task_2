def caesar_encrypt(text, shift):
    """Encrypt text using Caesar Cipher"""
    result = ""

    for char in text:
        if char.isupper():  # Uppercase letters
            # ASCII A=65, shift, modulo 26, back to char
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():  # Lowercase letters
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Preserve spaces, punctuation, numbers, etc.
            result += char

    return result


def caesar_decrypt(text, shift):
    """Decrypt text using Caesar Cipher (reverse shift)"""
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char

    return result


# ==================== MAIN PROGRAM (IPO Model) ====================

print("🔐 Welcome to Caesar Cipher Tool 🔐\n")

# INPUT
message = input("Enter the message to encrypt: ")
shift_key = int(input("Enter shift key: "))

# PROCESS
encrypted = caesar_encrypt(message, shift_key)
decrypted = caesar_decrypt(encrypted, shift_key)

# OUTPUT
print("\n" + "="*50)
print("✅ ENCRYPTED TEXT:", encrypted)
print("🔓 DECRYPTED TEXT:", decrypted)
print("="*50)

# Validation
print("\n✅ Verification:", decrypted == message)

