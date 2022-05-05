class MyIterator:

    def __init__(self, nested_list: list):
        self.nested_list = self.field_lst(nested_list)

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        try:
            self.cursor += 1
            return self.nested_list[self.cursor - 1]
        except:
            raise StopIteration

    def field_lst(self, nested_list: list):
        new_lst = []
        for item in nested_list:
            if type(item) == list:
                new_lst += self.field_lst(item)
            else:
                new_lst.append(item)
        return new_lst