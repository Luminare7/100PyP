alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(in_direction, in_text, in_shift):
    text_listed = []
    text_listed = in_text.strip((" "))
    cipher_list = []
    cipher_text = ""
    what = ""
    v = 1
    if in_direction == "encode":
        v = 1
        what = "encoded"
    elif in_direction == "decode":
        v = -1
        what = "decoded"
    for letter in text_listed:
        for index in range(len(alphabet)):
            if alphabet[index] == letter:
                cipher_list.append(alphabet[(index + in_shift*v) % len(alphabet)])
                cipher_text += alphabet[(index + in_shift*v) % len(alphabet)]
    print("The " + what + f" message is: {cipher_text}")

