import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(
                os.path.join(working_dir_abs, file_path))
        common_path = os.path.commonpath([working_dir_abs, target_path])
        if not common_path == working_dir_abs:
            return (f'Error: Cannot write to "{file_path}"'
                    'as it is outside the permitted working directory')
        if os.path.isdir(target_path):
            return (f'Error: Cannot write to "{file_path}"'
                    'as it is a directory')
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        with open(target_path, "w") as f:
            f.write(content)
            return (f'Successfully wrote to "{file_path}"'
                    f'({len(content)} characters written)')
    except Exception as e:
        return f'Error: writing file content: {e}'


schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes the provided content to the speci=fied file "
                       "withing the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write, "
                    "relative to the working directory"
                },
                "content": {
                    "type": "string",
                    "description": "Text contents to be written to the file"
                },
            },
            "required": ["file_path", "content"]
        },
    },
}
