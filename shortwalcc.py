# ShortWalcc python reference implementation (ShortWalcc.Py)
# Compatible with shortwalcc v1.0
# GPLv3
# @furretra1n
import os
import sys
class interpreter():
    def interpret(code):
        
        if '->' and '<-' not in code and ' + ' in code: # complex if statement
                code2 = code.split(' + ')
                result = int(code2[0]) + int(code2[1])
                return result
        elif '->' and '<-' not in code and ' - ' in code:
                code = code.split(' - ')
                result = int(code[0]) - int(code[1])
                return result

        elif '->' and '<-' not in code and ' / ' in code:
                return int(code.split(' / ')[0]) / int(code.split(' / ')[1])
        elif '->' and '<-' not in code and ' * ' in code:
                return int(code.split(' * ')[0]) * int(code.split(' * ')[1])
        elif '->' in code:
            parsed = code.split(' -> ')
            parsed = [ parsed[1], parsed[0] ]
            return parsed
        elif '<-' in code:
            
            if '{' and '}' not in code: # if not a function, treat as a regular var
                parsed = code.split(' <- ')
                
                if ' + ' in code:
                    varname = parsed[0]
                    parsed = parsed[1].split(' + ')
                    return [varname, int(parsed[0]) + int(parsed[1])]

                elif ' - ' in code:
                    return [parsed[0], int(parsed[1].split(' - ')[0]) - int(parsed[1].split(' - ')[1])]
                
                return parsed
            
            elif '{' and '}' in code: # if function, treat as function  
                return 'Not Implemented'


i = interpreter
print(i.interpret('1 -> a'))
print(i.interpret('1 + 1'))
print(i.interpret('a <- 1'))
print(i.interpret('a <- { furret }'))
print(i.interpret('a <- 1 + 1'))
print(i.interpret('a <- 1 - 1'))
print(i.interpret('3 - 1'))
print(i.interpret('3 / 2'))
print(i.interpret('2 * 2'))
