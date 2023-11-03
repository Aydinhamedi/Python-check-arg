def check_arg(arg_list: list, arg_str: str, return_arg: bool = False, bool_OUTPUT_ONLY: bool = False): #TODO USE check_arg
    """
    This function checks if a specific argument exists in a list of arguments.

    Parameters:
    arg_list (list): A list of arguments.
    arg_str (str): The argument to check for.
    return_arg (bool, optional): If True, returns the string after the argument if it exists. Defaults to False.

    Returns:
    bool/str: Returns True if the argument exists and return_arg is False. 
              Returns the string after the argument if return_arg is True and the argument exists.
              Returns specific error codes in case of errors.
              
    Error Codes:

        '![IER:01]': This error is returned when the provided argument list (arg_list) is empty or contains only 'none' or ''.
                     It indicates that there are no arguments to check against.

        '![IER:02]': This error is returned when the argument to check for (arg_str) is an empty string.
                    It indicates that there is no argument specified to look for in the argument list.

        '![IER:03]': This error is returned when the argument to check for (arg_str) is found in the argument list (arg_list), 
                     but there is no string after the argument and return_arg is set to True.
                     It indicates that the function was expected to return the string following the argument, but there was none.

        '![IER:04]': This error is returned when the argument to check for (arg_str) is not found in the argument list (arg_list).
                     It indicates that the specified argument does not exist in the provided argument list.

        Note: If the bool_OUTPUT_ONLY parameter is set to True, the function will return False instead of these error codes.
    """

    # Error handling
    if arg_list == [] or arg_list == ['none'] or arg_list == ['']:
        return False if bool_OUTPUT_ONLY else '![IER:01]'
    if arg_str == '':
        return False if bool_OUTPUT_ONLY else '![IER:02]'
    
    for item in arg_list:
        if item.startswith('-'):
            if item[1] == arg_str:
                if len(item) == 2 and return_arg:
                    return False if bool_OUTPUT_ONLY else '![IER:03]'
                return True if not return_arg else item[2:]
    
    return False if bool_OUTPUT_ONLY else '![IER:04]'
