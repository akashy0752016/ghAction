import sys
from pathlib import path

def get_root_folder(path):
  return Path(path).anchor

def process(args):
  result = [get_root_folder(arg) for i, arg in enumerate(args)]
  return result

if __name__ == "__main__":
  arguments = sys.argv[1:]
  result = process(arguments)

  for item in result:
    print(item)
  
