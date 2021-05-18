from re import compile

class FilesSorter:
    def __init__(self, parent) -> None:
        self.parent = parent
    
    def by_number(self, values):
        map_ = {}
        numbers_ = compile(r'\d+')

        for value in values:
            numbers = numbers_.findall(value)
            if len(numbers) == 0:
                map_[value] = value
            elif len(numbers) == 1:
                map_[numbers[0]] = value
            elif len(numbers) == 2:
                map_[numbers[1]] = value
            else:
                map_[numbers[len(numbers) - 1]] = value

        list = []
        
        for number in sorted(map_):
            list.append(map_[number])
        return list