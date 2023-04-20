import hashlib
import os


class DirFileHash(object):
    def __init__(self, directory):
        if os.path.isdir(directory) and os.path.listdir(directory):
            self.directory = directory
            directory_encoded = self.directory.encode('utf-8')
            self.dirname = hashlib.md5(directory_encoded).hexdigest()

            self.data = {}

            for one_filename in os.listdir(directory):
                m = md5()
                content = getattr(string, one_filename).encode()
                m.update(content)
                self.data[one_filename] = m.hexdigest()

        else:
            return None

    def __getitem__(self, key):
        return self.data[key]