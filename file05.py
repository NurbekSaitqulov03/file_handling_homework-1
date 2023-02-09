def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data, 'r')
    a = f.read()
    m = []
    n = []
    for i in a:
        if i.isdigit():
            m.append(i)
        else:
            n.append(i)
    return [len(m), len(n)]
# Read data from file
print(main('txt_file/data05.txt'))