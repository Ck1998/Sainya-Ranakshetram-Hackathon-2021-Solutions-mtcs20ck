This is short readme for the Tickle Pickle challenge.

Vulnerability - 
The server.py file suffers from the pickle code execution vulnerability. In this vulnerability attacker can create a custom payload containing malicious command and then can use this payload to execute remote code execution on the target.


The main directory contains two folders -
1. original_code - This directory contains the original code that was given as part of the challenge and is extracted from the rar file.
2. modified_and_secure_code - This directory contains modified client.py and server.py and is invulnerable to Pickle code execution.


Usage - 
In order to see the effects of the vulnerability follow these steps - 
1. run tickle_pickle_exploit.py to create a malicious users.json file
2. run original/server.py. You will see the command being executed.
3. In order to see the secure version, run server_secure.py to see the effects of modified code.

Securing the code: 
In order to secure the code against Pickle Code execution, encryption was used, in this case only symetric key encryption is used.

Assumptions for this scenario - 
There is a SHARED_SECRET_KEY, which is with the cleint and the server and the attacker is not aware of this key.

How is it secured - 
The client encrypts the data using the SHARED_KEY and stores it, server decrypts it using the SHARED_KEY. If the data is successfully decrypted then it processes it.
Since attacker does not have the SHARED_KEY, it can not encrypt the payload, and when the server runs that payload, it can not decrypt it and aborts the process.


Added Protection - 
The use of SHARED secret key is one of the wau to prevent pickle code execution, we can add another layer of security by using RSA and signing the data with the client's private key, server will have access to the client's public key and can verify whether the data is coming from the intended user.