import os
import pickle
def reverse_fun():
      with open("users.json","rb") as f:
          data = f.read()
      
      d = pickle.loads(data)
      return d

if __name__ == '__main__':
      print(reverse_fun())