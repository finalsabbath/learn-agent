from google import genai
import os,config

schema_get_file_content = genai.types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content of a file limited to the first 10000 characters.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The file path to read from, relative to the working directory.",
            ),
        },
    ),
)

def get_file_content(working_directory,file_path):
    wd_path = os.path.abspath(working_directory)
    fqdn = os.path.abspath(os.path.join(working_directory, file_path))
    if not fqdn.startswith(wd_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(fqdn):
        err = f'Error: File not found or is not a regular file: "{file_path}"'
        return err
    try:
        with open(fqdn, "r") as f:
            file_content_string = f.read(config.MAX_CHARS)
            if len(file_content_string) == config.MAX_CHARS:
                file_content_string += f'...File "{file_path}" truncated at 10000 characters'
        
        return file_content_string
    except Exception as e:
        return f'Error: {str(e)}'