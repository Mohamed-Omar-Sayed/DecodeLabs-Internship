import string 

def caesar(text, shift, alphabets):
     
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]
    
    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet=''.join(shifted_alphabets)
    table=str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)


plan_text = input("Enter the text to encrypt: ")

shift_value = int(input("Enter shift number: "))
encrypted_text = caesar(plan_text, shift_value, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation])

print("\n--- Result ---")
print("Encrypted text:", encrypted_text)
