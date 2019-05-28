def check_empty_string(string: str, field: str):
    if not string:
        raise Exception('Not allowed empty strings for {}.'.format(field))
    return True

def check_if_key_exists(key: str, obj: dict):
    if key not in obj:
        raise Exception('Not allowed empty object for {}.'.format(key))
    return True

def check_empty_string_in_array(array: [], field:str):
    for a in array:
        if check_empty_string(a,field):
            continue

