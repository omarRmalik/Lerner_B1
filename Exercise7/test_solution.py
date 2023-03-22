import os
from solution import filefunc

def test_func_dict():
    def mock_func(path):
        return len(path)

    # Create a temporary directory and some files to test with
    os.makedirs("temp_dir")
    open("temp_dir/file1.txt", "w").close()
    open("temp_dir/file2.txt", "w").close()

    # Call filefunc with the temporary directory and mock function
    func_dict, excep_dict = filefunc("temp_dir", mock_func)

    # Assert that the function returned the correct values for each file
    assert func_dict == {"file1.txt": 18, "file2.txt": 18}

    # Assert that no exceptions were raised
    assert len(excep_dict) == 0

    # Clean up the temporary directory
    os.remove("temp_dir/file1.txt")
    os.remove("temp_dir/file2.txt")
    os.rmdir("temp_dir")

# Test the exceptions dictionary

def test_excep_dict():
    os.makedirs("temp_dir")
    open("temp_dir/file1.txt", "w").close()
    open("temp_dir/file2.txt", "w").close()

    # Call filefunc with the temporary directory and mock function
    func_dict, excep_dict = filefunc("temp_dir", abs)

    assert excep_dict == {"TypeError": "TypeError: bad operand type for abs(): '_io.TextIOWrapper'",
                          "TypeError": "TypeError: bad operand type for abs(): '_io.TextIOWrapper'"}
    assert len(func_dict) == 0

    # Clean up the temporary directory
    os.remove("temp_dir/file1.txt")
    os.remove("temp_dir/file2.txt")
    os.rmdir("temp_dir")


