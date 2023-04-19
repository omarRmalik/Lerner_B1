import hashlib

class DirFileHash(object):
    def __init__(self, directory):
        self.directory = directory
        directory_encoded = self.directory.encode('utf-8')
        self.dirname = hashlib.md5(directory_encoded).hexdigest()

        self.data = {}
        for file_path in self.directory:
            with open(file_path, 'rb') as infile:
                data = infile.read()
                self.data[file_path] = hashlib.md5(data).hexdigest()

    def __getitem__(self, key):
        return self.data[key]