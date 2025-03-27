import sys
import os
import fire

def get_root_folder(path):
  return os.path.dirname(path).split(os.sep)[0]

def process(modified-files):
  result = [get_root_folder(arg) for i, arg in enumerate(modified-files)]
  return result

if __name__ == "__main__":
  fire.Fire(process)
  
