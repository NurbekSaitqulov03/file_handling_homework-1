def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data, 'r')
    a = f.read()
    m = []
    for i in a:
        if i.isdigit():
            m.append(int(i))
    return max(m)
# Read data from file
print(main('txt_file/data08.txt'))