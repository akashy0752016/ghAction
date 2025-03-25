import sys

def process(args):
  result = [f"Argument {i}: {arg}" for i, arg in enumerate(args)]
  return result

if __name__ == "__main__":
  arguments = sys.argv[1:]
  result = process(arguments)

  for item in result:
    print(item)
  
