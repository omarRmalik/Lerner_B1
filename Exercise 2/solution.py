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
  elif len(args) >= 1:
    non_none_args =[one_arg for one_arg in args
                    if one_arg is not None]
    if len(non_none_args) == 1:
      return myrange(x = 0, y = non_none_args[0], increment = 1)
    elif len(non_none_args) == 2 and non_none_args[0] < non_none_args[1]:
      return myrange(x=non_none_args[0], y=non_none_args[1], increment=1)
    elif len(non_none_args) == 3:
      return myrange(x = non_none_args[0], y = non_none_args[1], increment = non_none_args[2])
    else:
      return [ ]

# myrange that returns a generator

def myrange3(y, x=0, increment=1):
  current_val = x
  yield x
  while current_val < (y - increment):
    current_val = current_val + increment
    yield current_val