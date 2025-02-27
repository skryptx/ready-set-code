def encode(msg, shift) -> str:
    encode_list = []
    for char in msg:
        if ord(char) not in range(97, 123):
            encode_list.append(char)
            continue
        offset = ((ord(char)- 97) + shift) % 26
        encode_list.append(chr(offset+97))
    return ''.join(encode_list)

def decode(msg, shift) -> str:
    encode_list = []
    for char in msg:
        if ord(char) not in range(97, 123):
            encode_list.append(char)
            continue
        offset = ((ord(char)- 96) - shift)%26
        if offset > 0:
            encode_list.append(chr(offset + 96))
        else:
            encode_list.append(chr(122 - offset))
    return ''.join(encode_list)

print(encode("hello world!", 9))
print(decode("qnuux fxaum!", 9))