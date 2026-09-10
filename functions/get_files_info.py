import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        common_path = os.path.commonpath([working_dir_abs, target_dir])

        if not os.path.isdir(directory):
            return f'Error: "{directory}" is not a directory'
        if not common_path == working_dir_abs:
            return (f'Error: Cannot list "{directory}"'
                    'as it is outside the permitted working directory')

        return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        print(f'Error: {e}')
