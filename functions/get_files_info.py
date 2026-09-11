import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        common_path = os.path.commonpath([working_dir_abs, target_dir])

        if not common_path == working_dir_abs:
            return (f'Error: Cannot list "{directory}"'
                    'as it is outside the permitted working directory')
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        dir_content: list[str] = os.listdir(target_dir)
        files_info = ""
        for path in dir_content:
            complete_path = target_dir + "/" + path
            files_info += (
                f'- {path}: '
                f'file_size={os.path.getsize(complete_path)} bytes,'
                f'is_dir={os.path.isdir(complete_path)}\n'
            )

        return files_info
    except Exception as e:
        return f'Error listing dir contents: {e}'
