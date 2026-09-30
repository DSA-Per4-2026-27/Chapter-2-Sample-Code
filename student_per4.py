class Student:
    def __init__(self, first_name: str, last_name: str, 
            grades: list[int] = None) -> None:
        assert(isinstance(first_name, str))
        assert(isinstance(last_name, str))
        if grades is not None:
            assert(isinstance(grades, list))
        self.first_name = first_name
        self.last_name = last_name
        if grades is not None:
            self.grades = grades
        else:
            self.grades = []

    def __str__(self) -> str:
        """Provide a *human*-readable version of an instance."""
        return f"Student: {self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        """Provide a *Python*-readable version of an instance."""
        ret =  f"Student('{self.first_name}', '{self.last_name}', "
        ret += f"grades={self.grades})"
        return ret

if __name__ == "__main__":
    jt = Student('JT', 'Cochrane')
    jt.grades.append(97)
    jt.grades.append(95)
    jt.grades.append(101)
    kayley = Student('Kayley', 'Xu')
    jt_clone = eval(repr(jt))
    print(f"{jt=}, {jt.grades=}")
    print(f"{jt_clone=}, {jt_clone.grades=}")
    print(f"{kayley=}, {kayley.grades=}")
    jt.grades.append(96)
    print(f"{jt=}, {jt.grades=}")
    print(f"{jt_clone=}, {jt_clone.grades=}")
    print(f"{kayley=}, {kayley.grades=}")

