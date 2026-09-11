import os
from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(
                os.path.join(working_dir_abs, file_path))
        common_path = os.path.commonpath([working_dir_abs, target_path])
        if not common_path == working_dir_abs:
            return (f'Error: Cannot read "{file_path}" '
                    'as it is outside the permitted working directory')
        print(f"Target: {target_path}")
        if not os.path.isfile(target_path):
            return ('Error: File not found '
                    f'or is not a regular file: "{file_path}"')
        with open(target_path, "r") as f:
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                file_content += (f'[...File "{file_path}"'
                                 f'truncated at {MAX_CHARS} characters]')
            return file_content
    except Exception as e:
        return f'Error reading file content: {e}'
