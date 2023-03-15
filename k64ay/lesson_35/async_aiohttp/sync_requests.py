import requests
from codetiming import Timer

def task(url: str) -> None:
    with Timer(text=f'Task {url} elapsed time: {{:.1f}}'):
        res = requests.get(url)
        res.text

def main() -> None:
    with Timer(text='\nTotal elaped time: {:.1f}'):
        for url in [
            'http://google.com',
            'http://linkedin.com',
            'http://habr.com',
            'http://onliner.by',
        ]:
            task(url)

if __name__ == '__main__':
    main()