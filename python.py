class Number:
    def _init_(self, Maximum):
        self.Maximum = Maximum
        self.max_Maximum = max(Maximum)
        print("Max san:", self.max_Maximum)

Maximum = (2,5,9,10,11,12)
number = Number(Maximum)
def find_max(list1):
    return max(list1)
a = find_max([2,3,4,5,6,7])
print("Max:", a)
