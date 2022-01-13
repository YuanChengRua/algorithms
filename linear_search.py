def linear_search(list, target):
    """
    
    :param list:
    :param target:
    :return: the index position of the target if found, else returns None
    """
    for i in range(len(list)):
        if list[i] == target:
            return i
    return None