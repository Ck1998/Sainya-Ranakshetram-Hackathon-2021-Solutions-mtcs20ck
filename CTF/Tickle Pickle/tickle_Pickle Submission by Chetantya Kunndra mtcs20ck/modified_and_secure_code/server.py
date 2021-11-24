import os
import pickle
import base64
from Crypto.Cipher import AES

# SHARED Secret key between client and server, this is under the assumption that attacker 
# does not know this shared secret key

SHARED_SECRET = b"AS!2~`asdJSAD_!!$#&($1!2431_)*)("
UNPAD = lambda s : s[:-ord(s[len(s)-1:])]


def decrypt_data(enc_obj):
    enc_obj = base64.b64decode(enc_obj)
    iv = enc_obj[:16]
    cipher = AES.new(SHARED_SECRET, AES.MODE_CBC, iv)
    return UNPAD(cipher.decrypt( enc_obj[16:]))


def reverse_fun():
      with open("users.json","rb") as f:
          enc_data = f.read()
      
      try:
            data = decrypt_data(enc_data)
      except Exception as e:
            return f"Inconsistent users.json file. Aborting!! {e}"
      else:
            d = pickle.loads(data)
            return d


if __name__ == '__main__':
      print(reverse_fun())
