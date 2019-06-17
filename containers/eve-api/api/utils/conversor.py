def str_to_bool(s):
    string = str(s)
    if string == 'True':
         return True
    elif string == 'False':
         return False
    else:
         raise ValueError 