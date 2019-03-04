import re

even = re.compile(r'\d*[02468]')

decimal = re.compile(r'\d+\.*\d+')

variable = re.compile(r'^[a-zA-Z_]+[a-zA-Z0-9_]+$')

quote = re.compile(r'\"([a-zA-Z0-9_ ]+)\"')
