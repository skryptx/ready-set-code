def encode(msg, shift):
    encode_list = []
    for char in msg:
        msg = ((ord(char)- 96) + shift) % 26
        encode_list.append(chr(msg+96))
    return ''.join(encode_list)

print(encode("piedpiper", 5))
