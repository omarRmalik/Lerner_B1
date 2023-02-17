# myrange2 that returns a list

def myrange2(x, y, increment):
  output = []
  current_val = x
  output.append(current_val)
  while current_val < (y - increment):
    current_val = (current_val + increment)
    output.append(current_val)
  return output

# myrange that returns a generator

def myrange3(x, y, increment):
  current_val = x
  yield x
  while current_val < (y - increment):
    current_val = current_val + increment
    yield current_val