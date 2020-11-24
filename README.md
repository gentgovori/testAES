# aesFlask
Security project using FLASK 

<b>Setting up your enviroment</b>

- Install python 3.9.0
- Install PIP
- Install virtualenv

In order to run the app.py file you need to set up your enviroment yourself. 

<b>To get access to an implementation of AES-256 we need to :</b>
- Install pycryptodome

Usually AES needs padding but with AES-256 we don't have to do any padding. We set the AES-MODE to <b>GCM</b>

We have 2 functions that we use to encrypt and decrypt
- encrypt()
- decrypt()

<b> encrypt()</b>
- Nonce: A random nonce (arbitrary value) must be a random and unique value for each time our encryption function is used with the same key. Think of it as a random salt for a   cipher. The library supplies us with a secure nonce.

- Scrypt: Scrypt is used to generate a secure private key from the password. This will make it harder for an attacker to brute-force our encryption.
- Salt: A new random salt is used for each run of our encryption. This makes it impossible for an attacker to use precomputed hashes in an attempt to crack the cipher. (see rainbow table)
- Scrypt parameters:
N is the cost factor. It must be a power of two, and the higher it is the more secure the key, but the more resources it requires to run.
R is the block size.
P is the parallelization factor, useful for running on multiple cores.
- Base64: We encode all of our bytes-type data into base64 a convenient string representation
- Tag: The tag is used to authenticate the data when using AES in GCM mode. This ensures no one can change our data without us knowing about it when we decrypt.
<code>
    
# code

    # generate salt
    salt = get_random_bytes(AES.block_size)

    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)
</code>

<b> decrypt()</b>

The decrypt function needs the same salt, nonce, tag, and password for it to convert cipher text to plaintext 
