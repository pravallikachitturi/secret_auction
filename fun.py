
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("type encode to encrypt , type decode to decrypt:\n ")
text=input("type your messsage:\n")
shift=int(input("type your shift number:\n"))
def encrypt(original_text, shift_amount):
    cipher = ""
    for letter in original_text:
        shifted_position=alphabet.index(letter)+shift_amount
        shifted_position %= len(alphabet)
        cipher+=alphabet[shifted_position]


    print(f"here is the ciphertext: {cipher}")
def decrypt(original_text,shift_amount):
    decrypted_text = " "
    for letter in original_text:
        shifted_position= alphabet.index(letter)-shift_amount
        shifted_position %= len(alphabet)
        decrypted_text+=alphabet[shifted_position]
        print(f"here is the original_text: {decrypted_text}")
decrypt(text,shift)

encrypt(text,shift)

def caesar(original_text, shift_amount,en_de):
    decrypted_text = " "
    if en_de=="decode":
        shift_amount*=-1
    for letter in original_text:
        if letter not in alphabet:
            decrypted_text+=letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            decrypted_text += alphabet[shifted_position]
    print(f"here is the original_text: {decrypted_text} result: {shift_amount}")


should_continue=True
while should_continue:

    caesar(text, shift, direction)
    restart=input("type 'yes' to continue or type 'no'\n").lower()
    if restart=="no":
        should_continue=False
        print("bye")








