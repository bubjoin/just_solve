class quick:
    def __init__(self, arr):
        self.arr = arr

    def place_pivot(self, left_idx, right_idx):
        if right_idx - left_idx <= 0:
            return
        pivot_idx = right_idx
        pivot = self.arr[right_idx]
        right_idx -= 1
        while 1:
            while self.arr[left_idx] < pivot:
                left_idx += 1
            while self.arr[right_idx] > pivot:
                right_idx -= 1
            if left_idx >= right_idx:
                break
            self.arr[left_idx], self.arr[right_idx] = self.arr[right_idx], self.arr[left_idx]
            left_idx += 1
        self.arr[left_idx], self.arr[pivot_idx] = self.arr[pivot_idx], self.arr[left_idx]
        return left_idx
    
    def quick_sort(self, left_idx, right_idx):
        if right_idx - left_idx <= 0:
            return
        pivot_idx = self.place_pivot(left_idx, right_idx)
        self.quick_sort(left_idx, pivot_idx-1)
        self.quick_sort(pivot_idx+1, right_idx)

test = quick([5,6,7,10,8,9,4,3,2,1])

test.quick_sort(0, 9)

print(test.arr)
