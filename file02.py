def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    x = open(data, 'r')
    y = x.read()
    a = y.split('/n')
    m = ('').join(a)
    return len(m)
# Read data from file
print(main('txt_file/data02.txt'))