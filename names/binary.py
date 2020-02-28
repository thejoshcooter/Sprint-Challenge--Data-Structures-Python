class BinarySearch:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearch(value)
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearch(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            if self.left:
                return self.left.contains(target)
            else:
                return False

    def get_max(self):
        if self.right == None:
            return self.value
        if self.right:
            return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)