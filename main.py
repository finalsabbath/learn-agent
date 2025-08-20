import os,sys
from dotenv import load_dotenv
from google import genai
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from functions.call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
available_functions = genai.types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]
)
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

def generate_content(messages, verbose=False):
    response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=genai.types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt),
    
    )

    if verbose:
        print("User prompt: " + messages)
        print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
        print("Response tokens: " + str(response.usage_metadata.candidates_token_count))
        #print(response.candidates)
    return response

def handle_response(messages,response,verbose=False):

    if response.text:
        print(f'Response: {response.text}')
    else:
        print("No text response from model.")
    
    if not response.function_calls:
        print("No function calls found in the response.")
        return
    
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if not function_call_result.parts[0].function_response.response:
            raise ValueError("Function response is empty")
        else:
            print(f"Function call result: {function_call_result.parts[0].function_response.response}")
            new_message = genai.types.Content(
                role="user",
                parts=[genai.types.Part.from_text(text=str(function_call_result.parts[0].function_response.response))],
            )
            messages.append(new_message)
        response = generate_content(messages)
        print(f'Response: {response.text}')
    return messages, response

def main():
    print("Hello from learn-agent!")

    verbose = "--verbose" in sys.argv
    prompt = sys.argv[1]
    print(f"Prompt: {prompt}")
    messages = []
    messages.append(genai.types.Content(
        role="user",
        parts=[genai.types.Part.from_text(text=prompt)],
    ))
    if not prompt:
        print("Please provide a prompt as a command line argument.")
        sys.exit(1)
    
    response = generate_content(messages)
    messages,response = handle_response(messages,response,verbose)
    while response.function_calls:
        messages,response = handle_response(messages,response,verbose)

if __name__ == "__main__":
    main()
