import os
from stat import *

class FilePointer:
    def __init__(self, attrs):
        self.attrs = attrs


class FileNavigator:

    def scan(self, root_path):
        file_pointers = []

        with os.scandir(root_path) as entries:
            for entry in entries:
                stats = os.stat(entry)

                if not S_ISDIR(stats.st_mode):
                    file_pointer = FilePointer(
                        {"path": entry.path,
                         "name": entry.name,
                         "size": stats.st_size}
                    )
                    file_pointers.append(file_pointer)
                else:
                    sub_pointers = self.scan(entry.path)
                    file_pointers.extend(sub_pointers)

        return file_pointers

    def match(self, file_pointers, attr_to_conditions, union_condition):
        matched_files = set()

        for file in file_pointers:

            any_mismatch = False

            for attr in attr_to_conditions:
                cur_file_attr = file.attrs[attr]
                cur_file_conditions = attr_to_conditions[attr]

                for condition in cur_file_conditions:
                    match_status = condition.match(cur_file_attr)

                    if match_status and union_condition == '||':
                        matched_files.add(file)
                        break

                    if not match_status and union_condition == '&&':
                        any_mismatch = True
                        break

            if union_condition == '&&' and not any_mismatch:
                matched_files.add(file)


        return matched_files


class FileCondition:
    def match(self, attr):
        pass

class IntegerCondition(FileCondition):
    def __init__(self, operator, number):
        self.operator = operator
        self.number = number

    def match(self, attr):
        operator = self.operator
        number = self.number

        if operator == '==':
            return attr == number
        elif operator == '>':
            return attr > number
        elif operator == '<':
            return attr < number
        elif operator == '>=':
            return attr >= number
        elif operator == '<=':
            return attr <= number

        return False

class StringCondition(FileCondition):
    def __init__(self, pattern):
        self.pattern = pattern

    def match(self, attr):
        pattern = self.pattern

        if '*' not in pattern:
            return attr == pattern
        elif pattern.startswith('*'):
            rest = pattern[1:]
            return attr.endswith(rest)
        elif pattern.endswith('*'):
            start = pattern[0:len(pattern)-1]
            return attr.startswith(start)

        return False


file_navigator = FileNavigator()
file_pointers = file_navigator.scan("/Users/rigupta/Desktop/")

sc1 = StringCondition("*png")
sc2 = StringCondition("*pdf")
ic1 = IntegerCondition(">", 1000000)

matched_files = file_navigator.match(file_pointers, {"name": [sc1], "size": [ic1]}, '&&')

for fp in matched_files:
    print("{} {}".format(fp.attrs["path"], fp.attrs["size"]))