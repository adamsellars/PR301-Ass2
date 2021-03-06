from model.class_maker import NewClass


class ClassFinder:

    def __init__(self) -> None:
        self.my_classes = []

    def find_class(self, file_data: str) -> None:
        assert type(file_data) is str, "find_class method must take string as input parameter"
        letters = file_data.split()
        # Find total amount of words in the list
        total = len(letters)
        # for each word in the list
        self.build_class(letters, total)

    def build_class(self, list_of_letters, total_letters):
        for i in range(total_letters):
            if list_of_letters[i - 1] == "class":
                self.add_class(list_of_letters, i)
            elif ":" == list_of_letters[i]:
                self.add_attribute(list_of_letters, i)
            elif "(" in list_of_letters[i]:
                self.add_method(list_of_letters, i, total_letters)

    def add_class(self, letters, i):
        a_new_class = letters[i]
        a_new_class = NewClass(a_new_class)
        self.my_classes.append(a_new_class)

    def add_attribute(self, list_of_letters, i):
        if ("(" not in list_of_letters[i - 1]) and (list_of_letters[i - 1][0].islower()):
            attribute = list_of_letters[i - 1] + " " + list_of_letters[i] + " " + list_of_letters[i + 1]
            self.my_classes[-1].add_attribute(attribute)

    def add_method(self, list_of_letters, i, total_letters):
        part_of_method = ""
        for j in range(i, total_letters):
            if ")" in list_of_letters[i]:
                part_of_method += list_of_letters[i]
                break
            elif ")" in list_of_letters[j]:
                part_of_method += (" " + list_of_letters[j])
                if list_of_letters[j + 1] == ":":
                    part_of_method += list_of_letters[j + 1] + " " + list_of_letters[j + 2]
                    break
            elif "}" in list_of_letters[j]:
                break
            else:
                part_of_method += " " + (list_of_letters[j])
        if list_of_letters[i + 1] == ":":
            method = part_of_method + list_of_letters[i + 1] + " " + list_of_letters[i + 2]
        else:
            method = part_of_method
        self.my_classes[-1].add_method(method)

    def get_all_my_classes(self) -> list:
        assert type(self.my_classes) is list, "get_all_my_classes must return a list"
        return self.my_classes

    def relationship_finder(self, file_data):
        assert type(file_data) is str, "relationship_finder file_data input parameter must be a string"
        # possible relationships
        file_data = file_data.split()
        list_of_relationships = ["--", "o--"]
        total_letters = len(file_data)
        total_classes = len(self.my_classes)
        self.build_relationship(file_data, list_of_relationships, total_letters, total_classes)

    def build_relationship(self, file_data, list_of_relationships, total_letters, total_classes):
        for i in range(total_letters):
            if file_data[i] in list_of_relationships:
                class_one, my_relationship, class_two = file_data[i - 1], file_data[i], file_data[i + 1]
                for j in range(total_classes):
                    if self.my_classes[j].class_name == class_one:
                        a_relationship = my_relationship + " " + class_two
                        self.my_classes[j].add_relationship(a_relationship)
