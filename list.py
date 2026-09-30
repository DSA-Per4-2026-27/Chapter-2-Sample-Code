def f(x: int) -> None:
    """Modify an integer."""
    x += 1000
    print(f"In f(): {x=}")

def g(my_list: list[int]) -> None:
    """Modify a list."""
    my_list.append(3141592)
    print(f"In g(): {my_list=}")
    
def h(s: str) -> None:
    """Modify a string."""
    s += "1000"
    print(f"In h(): {s=}")

a = 1
print(f"Global: {a=}")
f(a)
print(f"Global: {a=}")

print()

a_list = [1,2,3]
print(f"Global: {a_list=}")
g(a_list)
print(f"Global: {a_list=}")

print()

my_str = "This is a string."
print(f"Global: {my_str=}")
h(my_str)
print(f"Global: {my_str=}")
