import requests
import re

request = requests.get('https://api.leaked.wiki/clientinfo?json=yes')
userIp = re.search(r'\{"IP":"(.*?)"',request.text)

def actionOne():
    inputHost = input('Host (example.com): ')
    request = requests.get('https://api.leaked.wiki/host2ip?domain={0}&json=yes'.format(inputHost))
    userIp = re.search(r'"output":"(.*?)"',request.text)
    print('IP for {0} == {1}'.format(inputHost, userIp.group(1)))

def actionTwo():
    inputIp = input('IP (127.0.0.1): ')
    request = requests.get('https://api.leaked.wiki/ip2host?ip={0}&json=yes'.format(inputIp))
    userHost = re.search(r'"output":"(.*?)"',request.text)
    print('Host for {0} == {1}'.format(inputIp, userHost.group(1)))

def actionThree():
    request = requests.get('https://api.leaked.wiki/randomfact?json=yes')
    fact = re.search(r'"output":"(.*?)"',request.text)
    print('Random Fact: {0}'.format(fact.group(1)))


print('  ___  ______ _____   _____           _______           ')
print(' / _ \ | ___ \_   _| |_   _|         | | ___ \          ')
print('/ /_\ \| |_/ / | |     | | ___   ___ | | |_/ / _____  __')
print('|  _  ||  __/  | |     | |/ _ \ / _ \| | ___ \/ _ \ \/ /')
print('| | | || |    _| |_    | | (_) | (_) | | |_/ / (_) >  < ')
print('\_| |_/\_|    \___/    \_/\___/ \___/|_\____/ \___/_/\_\\')
print()

print('Your ip Is: {0}'.format(userIp.group(1)))

print()
print('Your IP Was resolved through an API.')
print('You can now create your own custom API querys please choose one of the following below')
print()

print('1. Resolve IP From Host  2. Resolve Host From IP 3. Generate Random Fact')
print()

choice = input('Command: ')

if choice == '1':
    actionOne()
elif choice == '2':
    actionTwo()
elif choice == '3':
    actionThree()
else:
    print('Please choose a differnet command.')


