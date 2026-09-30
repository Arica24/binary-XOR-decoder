# Binary XOR Decoder

A Python learning project adapted from my Week 2 university cryptography challenge. The task was to decrypt space-separated binary ciphertext with the supplied key `10101010` and explain the process.

## Run

Requires Python.

```bash
python3 decoder.py
```

On Windows, use `python decoder.py` if needed. Paste the ciphertext when prompted, then enter the binary key.

Example using the first four bytes from the supplied challenge:

```text
Ciphertext: 11100011 11000100 10001010 11011110
Key: 10101010
Result: In t
```

The complete challenge input is not bundled; paste it from your exercise. The short example verifies the same process.

## Process explained

1. `input()` reads the ciphertext.
2. `.split()` separates it into binary byte strings using whitespace.
3. Each byte and the key are validated as exactly eight binary digits.
4. `int(bits, 2)` reads binary text as a number. The key `10101010` is decimal 170.
5. `^` performs XOR. Equal bits produce 0; different bits produce 1.
6. `chr()` converts each recovered number to a character.
7. `''.join()` combines the characters into the message.

For the first byte:

```text
11100011 XOR 10101010 = 01001001
```

`01001001` is decimal 73, and `chr(73)` is `I`.

XOR reverses itself: applying the same key again recovers the original byte.

## Notebook

Open `Week_2_XOR_Challenge.ipynb` in Jupyter or Carnets to see the explanation and run the four-byte demonstration. The notebook uses only standard Python. The revised notebook has not been tested in the Carnets app.

## Important distinction

The exercise described its method as a one-time pad, but it applies the same eight-bit key to every byte. This implementation is **repeated single-byte XOR**, not a secure one-time pad. A true one-time pad needs a uniformly random secret key as long as the message, used only once.

`chr()` maps numbers to Unicode characters; for this exercise's ASCII plaintext, those character values match ASCII. This simple decoder does not decode general UTF-8 text.

## Skills

Python input handling, binary numbers, XOR, list comprehensions, functions, validation and explaining a cryptographic process.

## Attribution

Challenge specification and ciphertext excerpt: university Week 2 cryptography exercise. Original solution and explanation: Arica Bhuiyan. 

