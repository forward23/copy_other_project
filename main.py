import requests

url = input('ENTER URL or type q for exit: ')


while url != 'q':
    try:
        res = requests.get(url)
        print(f'Status code of {url} is {res.status_code}')
        break
    except Exception as exc:
        print(exc)
        url = input('ENTER URL or type q for exit: ')


print('The end!')




