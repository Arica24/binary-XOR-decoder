"""Decode space-separated binary bytes with a repeated eight-bit XOR key."""


def parse_byte(bits):
    if len(bits) != 8 or set(bits) - {'0', '1'}:
        raise ValueError('Each byte and the key must contain exactly eight binary digits.')
    return int(bits, 2)


def decrypt(ciphertext, key_bits):
    key = parse_byte(key_bits.strip())
    chunks = ciphertext.split()
    if not chunks:
        raise ValueError('Enter at least one ciphertext byte.')
    values = [parse_byte(chunk) ^ key for chunk in chunks]
    # chr mirrors the original exercise: each byte maps to one code point.
    return ''.join(chr(value) for value in values)


def main():
    try:
        ciphertext = input('Enter ciphertext (space-separated eight-bit bytes): ')
        key = input('Enter eight-bit binary key (example: 10101010): ')
        print('\nDecrypted text:\n')
        print(decrypt(ciphertext, key))
    except ValueError as error:
        print('Input error:', error)
    except (EOFError, KeyboardInterrupt):
        print('\nFinished.')


if __name__ == '__main__':
    main()
