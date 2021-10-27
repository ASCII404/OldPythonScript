from tkinter import *
from tkinter import messagebox, Entry
import time

start = time.time()
key_size: int = 26

root = Tk()
root.geometry('340x130')
root.title('CaesarEncryption')
root.resizable(False, False)
root.iconbitmap('calculus.ico')

encrypt_message = StringVar()
encrypt_key = IntVar()
encrypt_key.set(1)

encryption_result = StringVar()

Text_Encryption_Entry: Entry = Entry(root, textvariable=encrypt_message, width=25)
Text_Encryption_Entry.place(relx=.12, rely=.04)

Result_Entry: Entry = Entry(root, textvariable=encryption_result, width=25)
Result_Entry.place(relx=.16, rely=.65)

Key_Encryption_Entry: Entry = Entry(root, textvariable=encrypt_key, width=6)
Key_Encryption_Entry.place(relx=.69, rely=.04)

text_to_encrypt: str = encrypt_message.get()
encryption_key: int


def get_key_input():
    global encryption_key
    try:
        encryption_key = encrypt_key.get()
        valid_key = True
        if encryption_key > 26:
            messagebox.showerror("Value too large!", "The max value is 26!")
            valid_key = False

        elif encryption_key == 0:
            messagebox.showerror("Null value!", "This won't do anything!")
            valid_key = False

        elif encryption_key < 0:
            messagebox.showerror("Incorrect value!", "The value can only be a positive number!")
            valid_key = False
    except ValueError:
        messagebox.showerror("Value error!", "The value can only be a number!")
        valid_key = False

    return valid_key


def get_message_input():
    global text_to_encrypt

    valid_text = True
    text_to_encrypt = encrypt_message.get()
    is_char = re.match('\D', text_to_encrypt)

    if not text_to_encrypt:
        messagebox.showerror("Type error!", "No input, please enter your text!")
        valid_text = False
    elif not is_char:
        messagebox.showerror("Type error!", "You can't enter digits!")
        valid_text = False

    return valid_text


def encrypt():
    result: str = ''
    if get_key_input() == True and get_message_input() == True:
        for i in range(len(text_to_encrypt)):
            char = text_to_encrypt[i]
            if char.isupper():
                result += chr((ord(char) + encryption_key - 65) % key_size + 65)
            elif char.islower():
                result += chr((ord(char) + encryption_key - 97) % key_size + 97)
            elif char == ' ':
                result += ' '
        encryption_result.set(result)


def decrypt():
    result: str = ''
    if get_key_input() == True and get_message_input() == True:
        for i in range(len(text_to_encrypt)):
            char = text_to_encrypt[i]
            if char.isupper():
                result += chr((ord(char) - encryption_key - 65) % key_size + 65)
            elif char.islower():
                result += chr((ord(char) - encryption_key - 97) % key_size + 97)
            elif char == ' ':
                result += ' '
        encryption_result.set(result)


def brute_force():
    result: str = ''
    encrypt_key.set(1)
    for i in range(1, 26):
        key_for_encryption = i
        if get_message_input() == True:
            for i in range(len(text_to_encrypt)):
                char = text_to_encrypt[i]
                if char.isupper():
                    result += chr((ord(char) - encryption_key - 65) % key_size + 65)
                elif char.islower():
                    result += chr((ord(char) - encryption_key - 97) % key_size + 97)
                elif char == ' ':
                    result += ' '
            result += ' '
    encryption_result.set(result)


TextLabel = Label(root, text="Text", fg="red")
TextLabel.place(relx=.02, rely=.04)

ResultLabel = Label(root, text="Result", fg="blue")
ResultLabel.place(relx=.02, rely=.65)

KeyLabel = Label(root, text="Key", fg="red")
KeyLabel.place(relx=.6, rely=.04)

EncryptButton = Button(text="Encrypt", command=encrypt)
EncryptButton.place(relx=0.16, rely=.33)

DecryptButton = Button(text="Decrypt", command=decrypt)
DecryptButton.place(relx=0.34, rely=.33)

Brute_ForceButton = Button(text="Brute Force", command=brute_force)
Brute_ForceButton.place(relx=0.54, rely=.33)

end = time.time()
print(end-start, 'seconds' )
mainloop()
