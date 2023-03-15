from todo_project import celery_app

@celery_app.task(bind=True)
def test_task(self):
    import time
    import requests
    from bs4 import BeautifulSoup

    res = requests.get('https://github.com/tms-course/py-2022/tree/develop')
    soup = BeautifulSoup(res.text, 'html.parser')
    nodes = []
    for row in soup.find_all('div', {'class': 'Box-row'}):
        typ = row.find('svg')['aria-label']
        node_name = row.find('a', {'class': 'Link--primary'})
        # last_commit = row.find('a', {'class': 'Link--secondary'})
        
        node = {
            'type': typ,
            'name': node_name.text,
            'url': node_name['href'],
            # 'last_commit': last_commit.text,
        }
        nodes.append(node)

    time.sleep(5)

    return nodes