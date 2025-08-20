import os
from google import genai

schema_get_files_info = genai.types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "directory": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory=os.getcwd(), directory="."):
    if directory != ".":
        fqdn = os.path.join(working_directory, directory)
        if not os.path.isdir(fqdn):
            err = f'Error: "{directory}" is not a directory'
            return {err}
        if directory not in os.listdir(working_directory):
            err = f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            return {err}
    else:
        fqdn = working_directory

    contents = os.listdir(fqdn)
    output_string = ""
    for file in contents:
        file_string = f"- {file}: file_size={os.path.getsize(os.path.join(fqdn, file))} bytes, is_dir={os.path.isdir(os.path.join(fqdn, file))}"
        output_string += f"{file_string}\n"
    return output_string.strip()



if __name__ == "__main__":
    import sys
    working_directory = os.getcwd()
    directory = sys.argv[1] if len(sys.argv) > 1 else "."
    print(get_files_info(working_directory, directory))

