from typing import TypeVar, Generic, List, Dict, Union

T = TypeVar('T')
Key = Union[str, int]


# Generic Stack: Implement a generic stack class that can hold elements of any type. The stack should support
# operations like push, pop, and peek.

class stack(Generic[T]):
    def __init__(self):
        self.elements = []

    def push(self, element: T) -> None:
        self.elements.append(element)

    def remove_data(self, element: T) -> None:
        self.elements.pop(element)

    def show(self) -> List[T]:
        return self.elements


s = stack()

s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push('ww')
print(s.show())
s.remove_data(4)
print(s.show())


# Generic Sorting Algorithms: Implement generic versions of popular sorting algorithms such as Bubble Sort,
# Insertion Sort, Selection Sort, Merge Sort, and Quick Sort. The algorithms should be able to sort arrays of any type.
#
# Generic Cache: Implement a generic cache class that can store key-value pairs of any type. The cache should support
# operations like get, set, and evict based on a specific eviction policy.


class DataRepository(Generic[T]):
    def __init__(self):
        self.data: Dict[Key, List[T]] = {}

    def add_data(self, key: Key, item: T) -> None:
        if key in self.data:
            self.data[key].append(item)
        else:
            self.data[key] = [item]

    def remove_data(self, key: Key, item: T) -> None:
        if key in self.data:
            self.data[key].remove(item)

    def get_all_data(self) -> Dict[Key, List[T]]:
        return self.data

    def search_by_id(self, key: Key) -> Dict[Key, List[T]]:
        if key in self.data:
            return self.data
        else:
            print('obj not found')

    def remove_all(self, data):
        self.data.clear()

    def update(self, key: Key, updated_item: T) -> None:
        if key in self.data:
            self.data[key] = [updated_item]
        else:
            print('obj not found')

    # def input_data(self, key: Key) -> None:
    #     items = []
    #     while True:
    #         item = input("Enter an item (or 'done' to finish): ")
    #         if item.lower() == 'done':
    #             break
    #         items.append(item)
    #     self.add_data(key, items)


repository = DataRepository()
repository.add_data(1, "value1")
repository.add_data(2, "value2")
repository.add_data(3, [1, 2, 3, 4, 5])

print(repository.get_all_data())

repository.remove_data("key1", "value2")
print(repository.get_all_data())

repository.update(3, 'we')
print(repository.get_all_data())

# repository.input_data(1)
# print(repository.get_all_data())
