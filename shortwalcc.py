# ShortWalcc python reference implementation (ShortWalcc.Py)
# Compatible with shortwalcc v1.0
# GPLv3
# @furretra1n
class interpreter():
    def interpret(code): 
        if ' + ' in code: # not complex if statement
            if '->' in code:
                return [code.split(' -> ')[1], int(code.split(' -> ')[0].split(' + ')[0]) + int(code.split(' -> ')[0].split(' + ')[1])]
            elif '<-' in code:
                varname = code.split(' <- ')[0]
                result = int(code.split(' <- ')[1].split(' + ')[0]) + int(code.split(' <- ')[1].split(' + ')[1])
                return [varname, result]
            code2 = code.split(' + ')
            result = int(code2[0]) + int(code2[1])
            return result 
        elif ' - ' in code:    
            if '->' in code:
                varname = code.split(' -> ')[1]
                result = int(code.split(' -> ')[0].split(' - ')[0]) - int(code.split(' -> ')[0].split(' - ')[1])
                return [varname, result]
            elif '<-' in code:
                varname = code.split(' <- ')[0]
                result = int(code.split(' <- ')[1].split(' - ')[0]) - int(code.split(' <- ')[1].split(' - ')[1])
                return ifFloat(varname, result)
            code = code.split(' - ')
            result = int(code[0]) - int(code[1])
            return result
        def ifFloat(varname, result):
            if result.is_integer() == True:
                    result = int(result)
            return [varname, result]
        if ' / ' in code:
            if '->' in code:
                varname = code.split(' -> ')[1]
                result = float(code.split(' -> ')[0].split(' / ')[0]) / float(code.split(' -> ')[0].split(' / ')[1])
                return ifFloat(varname, result)
            if '<-' in code:
                varname = code.split(' <- ')[0]
                result = float(code.split(' <- ')[1].split(' / ')[0]) / float(code.split(' <- ')[1].split(' / ')[1])
                return ifFloat(varname, result)
        elif ' * ' in code:
            if '->' in code:
                varname = code.split(' -> ')[1]
                result = float(code.split(' -> ')[0].split(' * ')[0]) * float(code.split(' -> ')[0].split(' * ')[1])
                return ifFloat(varname, result)
            if '<-' in code:
                varname = code.split(' <- ')[0]
                result = float(code.split(' <- ')[1].split(' * ')[0]) * float(code.split(' <- ')[1].split(' * ')[1])
                return ifFloat(varname, result)
        elif '->' and '<-' not in code and ' ^ ' in code:
                return pow(int(code.split(' ^ ')[0]), int(code.split(' ^ ')[1]))
        elif '->' in code:
            parsed = code.split(' -> ')
            if ' + ' in code:
                return [parsed[1], int(parsed[0].split(' + ')[0]) + int(parsed[0].split(' + ')[1])]
            elif ' - ' in code:
                return [parsed[1], int(parsed[0].split(' - ')[0]) - int(parsed[0].split(' - ')[1])]
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
                elif ' / ' in code:
                    return [parsed[0], int(parsed[1].split(' / ')[0]) / int(parsed[1].split(' / ')[1])]
                elif ' * ' in code:
                    return [parsed[0], int(parsed[1].split(' * ')[0]) * int(parsed[1].split(' * ')[1])]
                elif ' ^ ' in code:
                    return [parsed[0], pow(int(parsed[1].split(' ^ ')[0]), int(parsed[1].split(' ^ ')[1]))]
                return parsed
            
            elif '{' and '}' in code: # if function, treat as function  
                return 'Not Implemented'

i = interpreter
