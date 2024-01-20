#Boolean variable Truthiness and Falsiness

#if value is any non-zero number, a non-empty string, or any non-empty container (list, dictionary, tuple), it will be considered
#___truthy, and the first part of the conditional statement will be executed. Otherwise, if value is 0, an empty string, or an empty 
#___container, it will be considered falsy, and the second part of the conditional statement will be executed.

value = 42

if value:
    print(f"The value {value} is truthy.")
else:
    print(f"The value {value} is falsy.")

#-------------------------------------------------------------------------------------------------------------------------------------

value = False

if value:
    print(f"The value {value} is truthy.")
else:
    print(f"The value {value} is falsy.")

#-------------------------------------------------------------------------------------------------------------------------------------

value = []   # if list is not empty like [23, 56, 89] --> it's give TRUE in output.

if value:
    print(f"The value {value} is truthy.")
else:
    print(f"The value {value} is falsy.")

#-------------------------------------------------------------------------------------------------------------------------------------

value = {}  # if dictionary is not empty like {' name : xyz ', 'sem : 8'} --> it's give TRUE in output.

if value:
    print(f"The value {value} is truthy.")
else:
    print(f"The value {value} is falsy.")

#-------------------------------------------------------------------------------------------------------------------------------------

value = ()   # if tuple is not empty (x,y,z) --> it's give TRUE in output.

if value:
    print(f"The value {value} is truthy.")
else:
    print(f"The value {value} is falsy.")

#-------------------------------------------------------------------------------------------------------------------------------------

value = ''   # Also use : "" 
              # if String is not empty 'vivek' and ' ' --> it's give TRUE in output.

if value:
    print(f"The value {value} is truthy.")
else:
    print(f"The value {value} is falsy.")

#-------------------------------------------------------------------------------------------------------------------------------------

value = None

if value:
    print(f"The value {value} is truthy.")
else:
    print(f"The value {value} is falsy.")
