import os
import pickle
def fun(name,password):
    s = {"username":name,"password":password}
    safecode = pickle.dumps(s)
    with open("users.json","wb") as f:
        f.write(safecode)
    return safecode

if __name__ == '__main__':
    u = input("Username : ")
    p = input("Password : ")
    yo_fun = fun(u,p)