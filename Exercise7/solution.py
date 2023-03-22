import os

def filefunc(path, func):
    func_dict = {}
    excep_dict = {}

    try:
        for path, directories, filenames in os.walk(path):
            for one_file in filenames:
                full_path = os.path.join(path, one_file)
                func_dict[one_file] = func(full_path)

    except Exception as e:
        excep_dict[type(e).__name__] = str(e)

    return func_dict, excep_dict