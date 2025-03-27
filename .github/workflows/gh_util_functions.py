import os
import fire

def get_root_folder(*path):
  result = [os.path.dirname(arg).split(os.sep)[0] for arg in path]
  result = list(set(result))
  print(result)

if __name__ == "__main__":
  fire.Fire()
  
