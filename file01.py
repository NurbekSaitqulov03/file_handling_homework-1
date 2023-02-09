def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data, 'r')
    x = f.read()
    a = x.split(',')
    b = []
    for i in a:
        b.append(int(i))
    return b
# Read data from file
print(main('txt_file/data01.txt'))