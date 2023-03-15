class SuperManager:
    def __enter__(self):
        print('Entering into manager...')
        
        return self

    def __exit__(self, *args) -> None:
        print('Exiting the manager...', args)


    def __aenter__(self):
        ...
    
    def __aexit__(self):
        ...

with SuperManager() as m:
    print('Context manager body', m)
async def x():
    async with SuperManager() as m:
        print('hello')

