import sys

class Tee:
  def __init__(self, *args):
    self.args = args

  def write(self, input_string):
    for one_file in self.args:
      try:
        one_file.write(input_string)
      except Exception as e:
        print(e)

  def writelines(self, lines):
    for one_file in self.args:
      try:
        one_file.writelines(lines)
      except Exception as e:
        print(e)

  def close(self):
    for one_file in self.args:
      one_file.close()

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.close()