class CompareStr:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return f"你输入的字符串是{self.string!r}"

    def __repr__(self):
        return f"String:{self.string}, Length: {len(self.string)}"

    def __len__(self):
        return len(self.string)

    def __eq__(self, other):
        if not isinstance(other, CompareStr):
            return NotImplemented#让python自己判断
        return self.string == other.string
        