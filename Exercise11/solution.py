import hashlib
from pathlib import Path

class DirFileHash(object):
  def __init__(self, directory):
    self.dirname = hashlib.md5(directory.encode('utf-8')).hexdigest()
    self.directory = directory
    self.data = { }
    for file_path in self.directory:
      if file_path.is_file():
        with open(file_path, 'rb') as infile:
          data = infile.read()
          self.data[file_path] = hashlib.md5(data).hexdigest()

  def __getitem__(self, key):
        return self.data[key]