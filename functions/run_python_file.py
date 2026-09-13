import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(
                os.path.join(working_dir_abs, file_path))
        common_path = os.path.commonpath([working_dir_abs, target_path])
        if not common_path == working_dir_abs:
            return (f'Error: Cannot execute "{file_path}" '
                    'as it is outside the permitted working directory')
        if not os.path.isfile(target_path):
            return (f'Error: "{file_path}" '
                    'does not exist or is not a regular file')
        if not file_path.endswith("py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_path]

        if args:
            command.extend(args)

        result = subprocess.run(
                command,
                cwd=working_dir_abs,
                capture_output=True,
                text=True,
                timeout=30
        )
        output: list[str] = []
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if result.stdout is None and result.stderr is None:
            output.append("No output produced")
        if result.stdout:
            output.append(f"STDOUT: {result.stdout}")
        if result.stderr:
            output.append(f"STDERR: {result.stderr}")
        return "\n".join(output)
    except Exception as e:
        return f'Error: executing Python file: {e}'
