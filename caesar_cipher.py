# For those who do not have an idea what Caesar Cipher is!
# Caesar Cipher is a simple way to hide messages.
# Each letter in your text is shifted a certain number of steps forward in the alphabet.
# For example, with a shift of 3, ‘a’ becomes ‘d’, ‘b’ becomes ‘e’, and so on.
# It’s an old method used by Julius Caesar to send secret messages.


import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 160) 
print("Welcome to Caesar Cipher Program")
engine.say("Welcome to Caesar Cipher Program")
engine.runAndWait()


print('''
      
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           
''')



#1. Encryption
Alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(orignal_text, shift_amount):

  cipear_text = ""
  for letter in orignal_text :
    shifted_position = Alphabets.index(letter) + shift_amount
    shifted_position = shifted_position % len(Alphabets)
    cipear_text += Alphabets[shifted_position]

  print(f"The encrypted text is {cipear_text}")





#2. Decryption
Alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def decrypt(encrypted_text, shift_amount):

  cipear_text = ""

  for letter in encrypted_text :
    shifted_position = Alphabets.index(letter) - shift_amount
    shifted_position %= len(Alphabets)
    cipear_text += Alphabets[shifted_position]

  print(f"The decrypted text is {cipear_text}")


while True:


    user = input("Type'encode' to encrypt, type 'decode' to decrypt or 'exit' to quit: ").lower()

    if user == "encode":

      text = input("Enter the text to be encrypted: ")
      shift = int(input("Enter the shift number: "))
      encrypted_text = encrypt(orignal_text=text, shift_amount=shift)


    
    elif user == "decode":

      text = input("Enter the text to be decrypted: ")
      shift = int(input("Enter the shift number: "))
      decrypted_text = decrypt(encrypted_text=text, shift_amount=shift)

    

    elif user == "exit":
      print("Goodbye!")
      engine.say("Goodbye!")
      engine.runAndWait()
      break

    else:
      print("Invalid input. Please try again.")