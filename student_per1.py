class Student:
    def __init__(self, first_name: str, last_name: str, 
            grades: list[int] = None):
        pass
        assert(isinstance(first_name, str))
        assert(isinstance(last_name, str))
        self.first_name = first_name
        self.last_name = last_name
        if grades is None:
            self.grades = []
        else:
            self.grades = grades
        for grade in self.grades:
            assert(isinstance(grade, int))

    def __str__(self) -> str:
        """Provide a *human*-readable version of an instance."""
        return f"Student: {self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        """Provide a *Python*-readable version of an instance."""
        ret = f"Student('{self.first_name}', '{self.last_name}', "
        ret += f"grades = {self.grades})"
        return ret

if __name__ == "__main__":
    tracie = Student("Tracie", "Liu")
    kai = Student("Kai", "Mehta")
    tracie.grades.append(98)
    tracie.grades.append(97)
    tracie.grades.append(100)
    tracie_clone = eval(repr(tracie))
    kai_clone = eval(repr(kai))
    print(f"{tracie.grades=}")
    print(f"{tracie_clone.grades=}")
    tracie.grades.append(101)
    print(f"{tracie.grades=}")
    print(f"{tracie_clone.grades=}")
    kai.grades.append(96)
    print(f"{kai.grades=}")