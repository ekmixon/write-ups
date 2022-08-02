import re
import requests
from base64 import b64encode, b64decode


def main():
    ciphertext = 'oWTWItwxAFINQBrozTSNqW2q4HucO6nFjT+SSFMt4mO94Dm4M+dxMSktiRv+88tVt827KTLQrbu6v2Vmki9OSw=='
    decoded_cipher = b64decode(ciphertext)
    reg=re.compile(r"can't decode byte (.+?) in position (.+?):")
    plaintext=''
    for _ in range(len(decoded_cipher) // 16):
        for pos in range(16):
            for i in range(256):
                data = decoded_cipher[:pos] + bytes([i]) + decoded_cipher[pos + 1:]
                if value := make_request(b64encode(data).decode(), reg, pos):
                    value=int(value,16)
                    res=chr(value^i^decoded_cipher[pos])
                    plaintext+=res
                    print(f'\rposition: {pos}       plaintext: {plaintext}', end='')
                    break
        decoded_cipher=decoded_cipher[16:]


def make_request(cookie, reg, position):
    url = 'http://95.85.51.183/'
    headers = {'Cookie': f'user_info={cookie}'}
    r = requests.get(url, headers=headers)
    match = re.findall(reg, r.text)
    if match and match[0][1]==str(position):
        return match[0][0]


if __name__ == '__main__':
    main()
