import os
import pickle
import base64
from Crypto.Cipher import AES

# SHARED Secret key between client and server, this is under the assumption that attacker 
# does not know this shared secret key
 
SHARED_SECRET = b"AS!2~`asdJSAD_!!$#&($1!2431_)*)("
PAD = lambda s: s + (16 - len(s) % 16) * bytes(chr(16 - len(s) % 16).encode())


def encrypt_data(dump):
    dump = PAD(dump)
    iv = os.urandom(AES.block_size)
    cipher = AES.new(SHARED_SECRET, AES.MODE_CBC, iv )
    return base64.b64encode( iv + cipher.encrypt( dump ) ) 

    
def make_secure(dict_dump):
    enc_dump = encrypt_data(dict_dump)
    with open("users.json","w+b") as f:
        f.write(enc_dump)


def fun(name,password):
    s = {"username":name,"password":password}
    safecode = pickle.dumps(s)
    make_secure(dict_dump=safecode)


if __name__ == '__main__':
    u = input("Username : ")
    p = input("Password : ")
    fun(u,p)
