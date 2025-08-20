import os
from google import genai
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

available_functions = [
    "get_files_info",
    "get_file_content",
    "write_file",
    "run_python_file",
]

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    working_directory = os.path.abspath(os.path.join(os.getcwd(), "calculator"))

    function_name = function_call_part.name
    if function_name not in available_functions:
        return genai.types.Content(
            role="tool",
            parts=[
                genai.types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ])
    function_args = function_call_part.args
    function_args["working_directory"] = working_directory
    function_args = {k: v for k, v in function_args.items() if v is not None}

    if function_name == "get_files_info":
        function_result = get_files_info(**function_args)
    elif function_name == "get_file_content":
        function_result = get_file_content(**function_args)
    elif function_name == "write_file":
        function_result = write_file(**function_args)
    elif function_name == "run_python_file":
        function_result = run_python_file(**function_args)
    return genai.types.Content(
        role="tool",
        parts=[
            genai.types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )

