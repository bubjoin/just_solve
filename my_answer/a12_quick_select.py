# Quick select debug version

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
    
    def quick_select(self, qth, left_idx, right_idx):
        print(self.arr)
        self.qth = None
        if right_idx - left_idx <= 0:
            self.qth = left_idx
            return
        pivot_idx = self.place_pivot(left_idx, right_idx)
        print(self.arr)
        print(f"pivot_idx: {pivot_idx}")
        if qth < pivot_idx:
            print("L")
            self.quick_select(qth, left_idx, pivot_idx-1)
        elif qth > pivot_idx:
            print("R")
            self.quick_select(qth, pivot_idx+1, right_idx)
        else:
            print("C")
            self.qth = pivot_idx
            return
        if self.qth:
            return self.arr[qth]

test = quick([5,6,7,10,8,9,4,3,2,1])

print(test.quick_select(9, 0, 9))