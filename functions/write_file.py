from google import genai
import os

schema_write_file = genai.types.FunctionDeclaration(
    name="write_file",
    description="Writes to an existing file overwriting any existing content.  Creates file and/or directories if if they do not already exist.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The file path of the file to write to, relative to the working directory.",
            ),
            "content": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The content to write to the file. If the file already exists, it will be overwritten.",
            ),
        },
    ),
)

def write_file(working_directory, file_path, content):
    wd_path = os.path.abspath(working_directory)
    try:
        fqdn = os.path.abspath(os.path.join(working_directory, file_path))
        if not fqdn.startswith(wd_path):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(fqdn):
            os.makedirs(os.path.dirname(fqdn), exist_ok=True)
        with open(fqdn, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {str(e)}'