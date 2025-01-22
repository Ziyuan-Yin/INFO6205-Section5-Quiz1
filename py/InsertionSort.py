from typing import List


class InsertionSort:
    def __init__(self, array):
        self.array = array

    def sort(self) -> List:
        """Sorts the array using Insertion Sort."""
        for i in range(1, len(self.array)):
            self.insert(i)
        return self.array

    def insert(self, i):
        """Inserts the 'Transition element' into its correct position in the sorted portion of the array."""
        while i > 0 and self.array[i - 1] > self.array[i]:
            self.swap(i, i - 1)
            i -= 1
    #     TODO: TO BE IMPLEMENTED

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
