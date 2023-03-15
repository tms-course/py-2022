def char_gen(s: str) -> str:
    for i in s:
        yield i
        
def num_gen(n: int)-> int:
    for i in range(n):
        yield i
        
cg = char_gen('hello')
ng = num_gen(7)

tasks = [cg, ng]

while tasks:
    task = tasks.pop(0)
    try:
        value = next(task)
        print(value)
        tasks.append(task)
    except StopIteration:
        pass