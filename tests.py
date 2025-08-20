from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
import os
import unittest

class TestGetFilesInfo(unittest.TestCase):
    # def testCWD(self):
    #     self.working_directory = "calculator"
    #     self.test_dir = "."
    #     result = get_files_info(self.working_directory, self.test_dir)
    #     print(result)
    #     self.assertIn("- pkg: file_size=", result)
    #     self.assertIn("is_dir=True", result)
    #     self.assertIn("- main.py: file_size=", result)
    #     self.assertIn("is_dir=False", result)

    # def testSubdirectory(self):
    #     self.working_directory = "calculator"
    #     self.test_dir = "pkg"
    #     result = get_files_info(self.working_directory, self.test_dir)
    #     print(result)
    #     self.assertIn("- calculator.py: file_size=", result)
    #     self.assertIn("is_dir=False", result)
    #     self.assertIn("- render.py: file_size=", result)
    #     self.assertIn("is_dir=False", result)
    
    # def testInvalidDirectory(self):
    #     self.working_directory = "calculator"
    #     self.test_dir = "nonexistent"
    #     result = get_files_info(self.working_directory, self.test_dir)
    #     print(result)
    #     self.assertIn('Error: "nonexistent" is not a directory', result)
    
    # def testOutsideWorkingDirectory(self):
    #     self.working_directory = "calculator"
    #     self.test_dir = "../"
    #     result = get_files_info(self.working_directory, self.test_dir)
    #     print(result)
    #     self.assertIn('Error: Cannot list "../" as it is outside the permitted working directory', result)
    def testTool(self):
        self.working_directory = "'directory'"
        self.test_dir = "."
        result = get_files_info(self.working_directory, self.test_dir)
        print(result)
        self.assertIn("- main.py: file_size=", result)
        self.assertIn("is_dir=False", result)


class testGetFileContent(unittest.TestCase):
#     def testGetFileContentMain(self):
#         self.working_directory = "calculator"
#         self.file_path = "main.py" 
#         result = get_file_content(self.working_directory, self.file_path)
#         print(result)
#         self.assertIn("def main():", result)
#     def testGetFileContentCalc(self):
#         self.working_directory = "calculator"
#         self.file_path = "pkg/calculator.py" 
#         result = get_file_content(self.working_directory, self.file_path)
#         print(result)
#         self.assertIn("def _apply_operator(self, operators, values)", result)
#     def testGetFileContentInvalidFile(self):
#         self.working_directory = "calculator"
#         self.invalid_file_path = "nonexistent.txt"
#         result = get_file_content(self.working_directory, self.invalid_file_path)
#         print(result)
#         self.assertIn(f'Error: File not found or is not a regular file: "{self.invalid_file_path}"', result)
#     def testGetFileContentOutsideWorkingDir(self):
#         self.working_directory = "calculator"
#         self.outside_file_path = "/bin/cat"
#         result = get_file_content(self.working_directory, self.outside_file_path)
#         print(result)
#         self.assertIn(f'Error:', result)
    def testTool(self):
        self.working_directory = "'directory'"
        self.file_path = "main.py" 
        result = get_file_content(self.working_directory, self.file_path)
        print(result)
        self.assertIn("def main():", result)

class TestWriteFile(unittest.TestCase):
#     def testWriteFile(self):
#         self.working_directory = "calculator"
#         self.file_path = "lorem.txt"
#         content = "wait, this isn't lorem ipsum"
#         result = write_file(self.working_directory, self.file_path, content)
#         print(result)
#         self.assertIn(f'Successfully wrote to "{self.file_path}"', result)
#     def testWriteFileSubdirectory(self):
#         self.working_directory = "calculator"
#         self.file_path = "pkg/morelorem.txt"
#         content = "lorem ipsum dolor sit amet"
#         result = write_file(self.working_directory, self.file_path, content)
#         print(result)
#         self.assertIn(f'Successfully wrote to "{self.file_path}"', result)
#     def testWriteFileInvalidPath(self):
#         self.working_directory = "calculator"
#         self.invalid_file_path = "/tmp/temp.txt"
#         content = "This should not be written"
#         result = write_file(self.working_directory, self.invalid_file_path, content)
#         print(result)
#         self.assertIn(f'outside the permitted working directory', result)
    def testTool(self):
        self.working_directory = "'directory'"
        self.file_path = "main.txt"
        content = "hello"
        result = write_file(self.working_directory, self.file_path, content)
        print(result)
        self.assertIn(f'Successfully wrote to "{self.file_path}"', result)

class TestRunPythonFile(unittest.TestCase):
#     def testRunPythonFile(self):
#         self.working_directory = "calculator"
#         self.file_path = "main.py"
#         result = run_python_file(self.working_directory, self.file_path)
#         print(result)
#         self.assertIn("STDOUT: Calculator App", result)
#     def testRunPythonFileTests(self):
#         self.working_directory = "calculator"
#         self.file_path = "tests.py"
#         result = run_python_file(self.working_directory, self.file_path)
#         print(result)
#         self.assertIn("STDOUT:", result)
#     def testRunPythonFileWithArgs(self):
#         self.working_directory = "calculator"
#         self.file_path = "main.py"
#         args = ["3 + 5"]
#         result = run_python_file(self.working_directory, self.file_path, args)
#         print(result)
#         self.assertIn("┌─────────┐", result)
#     def testRunPythonFileInvalidFile(self):
#         self.working_directory = "calculator"
#         self.invalid_file_path = "nonexistent.py"
#         result = run_python_file(self.working_directory, self.invalid_file_path)
#         print(result)
#         self.assertIn(f'Error: File "{self.invalid_file_path}" not found.', result)
#     def testRunPythonFileOutsideWorkingDir(self):
#         self.working_directory = "calculator"
#         self.outside_file_path = "../main.py"
#         result = run_python_file(self.working_directory, self.outside_file_path)
#         print(result)
#         self.assertIn(f'Error: Cannot execute "{self.outside_file_path}" as it is outside the permitted working directory', result)
    def testTool(self):
        self.working_directory = "'directory'"
        self.file_path = "main.py"
        result = run_python_file(self.working_directory, self.file_path)
        print(result)
        self.assertIn("STDOUT: Calculator App", result)

if __name__ == "__main__":
    unittest.main()