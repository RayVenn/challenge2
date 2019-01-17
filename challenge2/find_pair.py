import sys


def read_input_file(input_file):
    """
    Read the input file and return as a list of tuples
    :param input_file: file name of input text file
    :return: list of tuples containing all items
    """
    item_list = []
    with open(input_file, 'r') as input_f:
        for line in input_f:
            item, value = tuple(line.split(','))
            item_list.append((item.strip(), int(value.strip())))

    return item_list


def find_pair(input_file, balance):
    """
    Find pair with input txt file and balance we have
    :param input_file: file name of input text file
    :param balance: balance value we have for the gifts
    :return: the most valuable dual items less than balance
    """
    item_list = read_input_file(input_file)
    i, j = 0, len(item_list)-1
    item1, item2 = None, None

    while i < j:
        sum_of_gift = item_list[i][1] + item_list[j][1]

        if balance < sum_of_gift:
            j -= 1
        elif balance >= sum_of_gift:
            if not item1 or sum_of_gift > item1[1] + item2[1]:
                item1, item2 = item_list[i], item_list[j]
            i += 1

    return item1, item2


if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception('Need 2 arguments: {} <txt_item_file> <balance_value>'.format(__file__))
    PAIRS = find_pair(sys.argv[1], int(sys.argv[2]))
    print('{} {}, {} {}'.format(
        PAIRS[0][0],
        PAIRS[0][1],
        PAIRS[1][0],
        PAIRS[1][1]))
