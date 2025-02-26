def encode(msg, shift) -> str:
    encode_list = []
    for char in msg:
        offset = ((ord(char)- 96) + shift) % 26
        encode_list.append(chr(offset+96))
    return ''.join(encode_list)

def decode(msg, shift) -> str:
    encode_list = []
    for char in msg:
        offset = ((ord(char)- 96) - shift)%26
        if offset > 0:
            encode_list.append(chr(offset + 96))
        else:
            encode_list.append(chr(122 - offset))
    return ''.join(encode_list)

print(encode("piedpiper", 115))
print(decode("atpoatapc", 115))