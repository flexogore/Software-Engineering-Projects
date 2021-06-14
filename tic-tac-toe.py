from IPython.display import clear_output
from itertools import groupby

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def loop_break():
    return False

def is_free(x, row):
    if row[x%3 - 1] == ' ':
        return True
    else:
        print("This position is occupied! Please pick another one. ")
        return False
        
symbols = {1: 'X', -1: 'O'}

def change_symbol(symbol):
    kyes = [key  for (key, value) in symbols.items() if value == symbol]
    return symbols[kyes[0] * (-1)]

def get_location():
    i = input("Throw me some numbers: ")
    while i.isdigit() == False or int(i) not in range(1,10):
        i = input("Throw me some numbers: ")
    return int(i)

def is_full(buffer):
    digit = 0
    for value in buffer.values():
        if value.count(' ') == 0:
            digit += 1
    if digit == 3:
        return True
    
def congratulate():
    print("Congratulations! You are the real Tic Tac Toe master!")

flag = 0
ON = 1
OFF = 0

trigger = ON

symbol = 'X'

tics = dict()
tics['row1'] = [' ', ' ', ' ']
tics['row2'] = [' ', ' ', ' ']
tics['row3'] = [' ', ' ', ' ']

tics1 = list()
for keu, value in tics.items():
    tics1.append(value)

greeting()    

while flag != 1:
    
    x = get_location()
    
    order = x/3
    
    if order < 1 or (order == 1 and x%3 == 0):
        if is_free(x, tics['row1']):
            tics['row1'][x%3 - 1] = symbol
            trigger = ON
        else:
            trigger = OFF
    elif (order >= 1 and order < 2)or(order == 2 and x%3 == 0):
        if is_free(x, tics['row2']):
            tics['row2'][x%3 - 1] = symbol
            trigger = ON
        else:
            trigger = OFF
    else:
        if is_free(x, tics['row3']):
            tics['row3'][x%3 - 1] = symbol
            trigger = ON
        else:
            trigger = OFF
        
    print('-------------')
    for key,value in tics.items():
        print(value[0], ' | ', value[1], ' | ', value[2])
        print('-------------')
    
    for value in tics.values():
        if all_equal(value) and value.count(' ') == 0:
            congratulate()
            flag = 1

    for x in zip(*tics.values()):
        if all_equal(x) and x.count(' ') == 0:
            congratulate()
            flag = 1
                
    if (tics['row1'][0] == symbol and tics['row3'][2] == symbol and tics['row2'][1] == symbol) or \
        (tics['row1'][2] == symbol and tics['row3'][0] == symbol and tics['row2'][1] == symbol):
        congratulate()
        flag = 1
        
    if is_full(tics) and flag != 1:
        print('Draw!')
        flag = 1
                
    clear_output(wait=True)
    
    if trigger == ON:
        symbol = change_symbol(symbol)
