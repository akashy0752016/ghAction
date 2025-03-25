import sys
import os

def get_root_folder(path):
  return os.path.dirname(path).split(os.sep)[0]

def process(args):
  result = [get_root_folder(arg) for i, arg in enumerate(args)]
  return result

if __name__ == "__main__":
  arguments = sys.argv[1:]
  result = process(arguments)

  for item in set(result):
    print(item)
  
