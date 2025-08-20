from google import genai
import os
import subprocess

schema_run_python_file = genai.types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The file path of the python file to run, relative to the working directory. Any additional arguments will be passed to the script.",
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args=[]):
    wd_path = os.path.abspath(working_directory)
    fqdn = os.path.abspath(os.path.join(working_directory, file_path))
    if not fqdn.startswith(wd_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(fqdn):
        err = f'Error: File "{file_path}" not found.'
        return err
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        subprocess_args = ["python", fqdn] + args
        result = subprocess.run(subprocess_args, capture_output=True, text=True, cwd=working_directory, timeout=30)
        return_string = ""
        if result.returncode != 0:
            return_string+= f'Error: Process exited with code {result.returncode}.\n'
        output_stdout = f'STDOUT: {result.stdout.strip()}'
        output_stderr = f'STDERR: {result.stderr.strip()}'
        return_string += output_stdout + output_stderr
        return return_string
    except Exception as e:
        return f'Error: executing Python file: {str(e)}'