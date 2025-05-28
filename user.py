class User:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.familia = last_name
    def get_first_name(self):
        return self.name
    def get_last_name(self):
        return self.familia
    def get_first_and_last(self):
        return self.name + self.familia
    def get_student_info(self):
        return f"Student: {self.name}, Familia: {self.familia}, Name and Familia: {self.first_and_last}"