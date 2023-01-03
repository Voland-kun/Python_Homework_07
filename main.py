from inout import *
from calc import calculation
from logi import logging

a = get_number()
oper = get_operator()
b = get_number()
res = calculation(a,b,oper)
result = f'{a}{oper}{b}={res}'
print(result)
logging(result)