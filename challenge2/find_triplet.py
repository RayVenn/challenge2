import sys
from challenge2.find_pair import read_input_file, find_pair

def find_triplet(item_list, balance):
    """
    Find triplet with input txt file and balance we have
    :param item_list: list of tuple with name and price from input text file
    :param balance: balance value we have for the gifts
    :return: the most valuable triplet items less than balance
    """
    max_res = 0
    length = len(item_list)
    item1, item2, item3 = None, None, None

    if length >= 3:
        for i in range(length):
            # just loop for each item and run find_pair with the sub list after index i
            pairs = find_pair(item_list[i+1:], balance-item_list[i][1])
            if pairs[0]:
                sum_of_triplet = pairs[0][1] + pairs[1][1] +  item_list[i][1]

                if sum_of_triplet > max_res:
                    max_res = sum_of_triplet
                    item1, item2, item3 = item_list[i], pairs[0], pairs[1]


    return item1, item2, item3


def main():
    if len(sys.argv) < 3:
        raise Exception('Need 2 arguments: {} <txt_item_file> <balance_value>'.format(__file__))
    item_list = read_input_file(sys.argv[1])
    triplet = find_triplet(item_list, int(sys.argv[2]))
    if not triplet[0]:
        print('Not Possible')
    else:
        print('{} {}, {} {}, {} {}'.format(
            triplet[0][0], triplet[0][1], triplet[1][0], triplet[1][1], triplet[2][0], triplet[2][1]))


if __name__ == '__main__':
    main()