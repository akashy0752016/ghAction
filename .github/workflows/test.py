import os
import fire

def get_root_folder(path):
  return os.path.dirname(path).split(os.sep)[0]

def process(*args):
#  print(args)
  result = [get_root_folder(arg) for arg in args]
  result = list(set(result) - set(['.github']))
  print(result)
#  return result

if __name__ == "__main__":
  fire.Fire(process)
  
