url = input().split('/')
divide_url = {}

divide_url['protocol'] = url[0].strip(':')
divide_url['host'] = url[2]
divide_url['others'] = url[3]

for key, value in divide_url.items():
    print('{}: {}' .format(key, value))