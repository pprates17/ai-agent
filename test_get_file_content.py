from functions.get_file_content import get_file_content


def test() -> None:
    print("Result for: lorem.txt")
    result = get_file_content("calculator", "lorem.txt")
    print(result)
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    print("")

    print("Result for: main.py")
    result = get_file_content("calculator", "main.py")
    print(result)
    print(f"main.py length: {len(result)}")
    print(f"main.py truncated: {'truncated' in result}")
    print("")

    print("Result for: pkg/calculator.py")
    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)
    print(f"pkg/calculator.py length: {len(result)}")
    print(f"pkg/calculator.py truncated: {'truncated' in result}")
    print("")

    print("Result for: /bin/cat")
    result = get_file_content("calculator", "/bin/cat")
    print(result)
    print(f"/bin/cat length: {len(result)}")
    print(f"/bin/cat truncated: {'truncated' in result}")
    print("")

    print("Result for: pkg/does_not_exist.py")
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)
    print(f"pkg/does_not_exist.py length: {len(result)}")
    print(f"pkg/does_not_exist.py truncated: {'truncated' in result}")
    print("")


if __name__ == "__main__":
    test()
