# myrange2 that returns a list

def myrange(x, y, increment):
  output = []
  current_val = x
  output.append(current_val)
  while current_val < (y - increment):
    current_val = (current_val + increment)
    output.append(current_val)
  return output

def myrange2(*args):
  if not args:
    raise ValueError('No arguments provided!')
  elif len(args) == 1:
    return myrange(0, y=args[0], increment=1)
  elif len(args) == 2 and args[0] < args[1]:
    return myrange(x=args[0], y=args[1], increment=1)
  elif len(args) == 2 and args[0] > args [1]:
    return []
  else:
    first, second, third = args
    return myrange(x = first, y = second, increment = third)

# myrange that returns a generator

def myrange3(y, x=0, increment=1):
  current_val = x
  yield x
  while current_val < (y - increment):
    current_val = current_val + increment
    yield current_val