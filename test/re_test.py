import re


line = re.search('=(.+)', 'AAA=BBB\n').groups()[0]
print(line)

