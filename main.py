from data import nested_list as nsl
from MyIterator import MyIterator


def my_generator(nested_list: list):
    def field_lst(nested_list: list):
        new_lst = []
        for item in nested_list:
            if type(item) == list:
                new_lst += field_lst(item)
            else:
                new_lst.append(item)
        return new_lst

    flat_list = field_lst(nested_list)

    for item in flat_list:
        yield item


if __name__ == '__main__':

    list_iterator = MyIterator(nsl)
    print('+' * 30)
    for item in list_iterator:
        print(item)

    print('+' * 30)

    flat_list = [item for item in list_iterator]
    print(flat_list)

    print('+' * 30)

    for item in my_generator(nsl):
        print(item)

    print('+' * 30)
