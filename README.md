# Python-check-arg
The `check_arg` function is a handy Python code snippet that checks if a specific argument exists in a list of arguments. It's a reusable piece of code that you can easily integrate into your projects.

## Function Signature

```python
def check_arg(arg_list: list, arg_str: str, return_arg: bool = False, bool_OUTPUT_ONLY: bool = False):
```

## Parameters

- `arg_list` (list): A list of arguments.
- `arg_str` (str): The argument to check for.
- `return_arg` (bool, optional): If True, returns the string after the argument if it exists. Defaults to False.
- `bool_OUTPUT_ONLY` (bool, optional): If True, only boolean values are returned. If False, specific error codes are returned in case of errors. Defaults to False.

## Returns

- `bool/str`: Returns True if the argument exists and `return_arg` is False. Returns the string after the argument if `return_arg` is True and the argument exists. Returns specific error codes in case of errors, unless `bool_OUTPUT_ONLY` is True.

## Error Codes

- '![IER:01]': Returned when the provided argument list is empty or contains only 'none' or ''.
- '![IER:02]': Returned when the argument to check for is an empty string.
- '![IER:03]': Returned when the argument is found in the argument list, but there is no string after the argument and `return_arg` is set to True.
- '![IER:04]': Returned when the argument is not found in the argument list.

Note: If the `bool_OUTPUT_ONLY` parameter is set to True, the function will return False instead of these error codes.

## Usage Examples

```python
# Example 1: Check if '-v' exists in the argument list
args = ['-v', '-f', 'file.txt']
print(check_arg(args, 'v'))  # Returns: True

# Example 2: Get the string after '-z' in the argument list
args = ['-v', '-f', '-z12']
print(check_arg(args, 'z', return_arg=True))  # Returns: '12'

# Example 3: Check for an argument that doesn't exist in the list
args = ['-v', '-f', 'file.txt']
print(check_arg(args, 'x'))  # Returns: '![IER:04]' or False if bool_OUTPUT_ONLY is True
```

Feel free to copy this code snippet and use it in your projects. If you find any issues or have any suggestions for improvements, please open an issue or submit a pull request.

