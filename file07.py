def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data, 'r')
    a = f.read()
    x = 0
    for i in a:
        if i.isdigit():
            x += int(i)
    return x
# Read data from file
print(main('txt_file/data07.txt'))