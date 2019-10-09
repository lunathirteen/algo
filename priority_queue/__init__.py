class PriorityQueue:
    """Implementation of priority queue"""

    def __init__(self):
        self.array = []
        self.heap_size = 0

    def _sift_up(self, index):
        parent_node = index//2
        if index == 1 or self.array[index-1] <= self.array[parent_node-1]:
            return

        self.array[index-1], self.array[parent_node-1] =\
            self.array[parent_node-1], self.array[index-1]

        self._sift_up(parent_node)

    def _sift_down(self, array, root):

        left = root*2 + 1
        right = root*2 + 2
        largest = root

        if left < self.heap_size and array[left] > array[largest]:
            largest = left
        if right < self.heap_size and array[right] > array[largest]:
            largest = right
        if largest != root:
            array[root], array[largest] = array[largest], array[root]
            self._sift_down(array, largest)
        return

    def insert(self, element):
        self.array.append(element)
        self.heap_size += 1
        self._sift_up(self.heap_size)

        return

    def extract_max(self):
        max_element = self.array[0]
        self.heap_size -= 1
        if self.heap_size < 1:
            self.array = []
            return max_element

        self.array[0] = self.array.pop(-1)
        self._sift_down(self.array, 0)
        return max_element

if __name__ == "__main__":

    n = int(input())

    a = PriorityQueue()

    for i in range(n):
        try:
            action, element = input().split(" ")
            a.insert(int(element))
        except ValueError:
            max_element = a.extract_max()
            print(max_element)
