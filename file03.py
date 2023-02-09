def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data, 'r')
    a = f.read()
    x = []
    for i in a:
        if i.isdigit():
            x.append(i)
    return x
# Read data from file
print(main('txt_file/data03.txt'))