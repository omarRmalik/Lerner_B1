import hashlib
import os

class DirFileHash(object):
    def __init__(self, dirname):
        self.dirname = dirname
        self.data = {}
        if not os.path.exists(dirname):
            return None
        else:
            for one_filename in os.listdir(dirname):
                file_path = os.path.join(dirname, one_filename)
                with open(file_path, 'rb') as infile:
                    digest = hashlib.md5(infile.read())
                    self.data[one_filename] = digest.hexdigest()

    def __getitem__(self, key):
        return self.data.get(key, None)