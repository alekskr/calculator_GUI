import math


def expression(user_input):
    """Work with expression."""
    for i in user_input:
        if i == ',':
            user_input = user_input.replace(i, '.')
        elif i == ' ':
            user_input = user_input.replace(i, '')
        elif i not in signs and not i.isalnum() and i not in ('(', ')', '=', '.', ','):
            return 'Invalid expression'
    if user_input.isalpha():
        return_variable(user_input)
    elif (user_input[0] not in ('-', '+', '(', ')') and not user_input[0].isalnum()) or (
            user_input[-1] not in (')',) and not user_input[-1].isalnum()):
        return 'Invalid expression'
    elif '=' in user_input:
        assignment(user_input)
    else:
        infix_list = from_string_to_list(user_input)
        return from_infix_to_postfix(infix_list)


def sqrt(a):
    b = expression(a)
    try:
        return str(round(math.sqrt(float(b)), 3))
    except ValueError:
        return 'Invalid expression'
    except TypeError:
        return 'Invalid expression'


def from_string_to_list(infix):
    """Create a list of elements from a string."""
    infix_list = []
    items = ''
    math_signs = ''
    for index, char in enumerate(infix):
        if char.isalnum() or char == '.':
            items = items + char
            if math_signs != '':
                infix_list.append(math_signs)
                math_signs = ''
        elif items != '' and not char.isalnum() and char in signs:
            infix_list.append(items)
            math_signs = math_signs + char
            items = ''
        elif char in signs and items == '':
            math_signs = math_signs + char
        elif math_signs != '' and char in ('(', ')'):
            infix_list.append(math_signs)
            infix_list.append(char)
            math_signs = ''
        elif items != '' and char in ('(', ')'):
            infix_list.append(items)
            infix_list.append(char)
            items = ''
        elif items == '' and math_signs == '' and char in ('(', ')'):
            infix_list.append(char)
    if items != '':
        infix_list.append(items)
    # processing math sings and braces:
    braces = []
    for index, i in enumerate(infix_list):
        if i == '(' and index != 0 and infix_list[index - 1] not in signs:
            return 'Invalid expression'
        elif i == ')' and not infix_list[-1] == ')' and infix_list[index + 1] not in signs:
            return 'Invalid expression'
        elif not i.isalnum() and i not in ('(', ')') and '.' not in i:
            j = process_sign(i)
            infix_list[index] = j
        elif i in ('(', ')'):
            braces.append(i)
    if len(braces) != 0:
        if braces[0] == ')' or infix_list.count('(') != infix_list.count(')'):
            return 'Invalid expression'
    for index, item in enumerate(infix_list):
        if item.isalpha() and item in dict_variables:
            infix_list.remove(item)
            infix_list.insert(index, dict_variables[item])
        elif item.isalpha() and item not in dict_variables:
            return 'Invalid expression'
    return infix_list


def from_infix_to_postfix(infix_list):
    """Convert infix to postfix. Then evaluate the expression."""
    try:
        priority = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}  # priority of mathematical signs
        queue = []
        stack = []
        for i in infix_list:
            if i.isdigit() or '.' in i:
                queue.append(i)
            elif i == '(':
                stack.append(i)
            elif i in signs:
                if len(stack) == 0 or stack[-1] == '(':
                    stack.append(i)
                elif priority[i] > priority[stack[-1]]:
                    stack.append(i)
                else:
                    while len(stack) != 0 and priority[i] <= priority[stack[-1]]:
                        queue.append(stack.pop())
                    stack.append(i)
            elif i == ')':
                while stack[-1] != '(':
                    queue.append(stack.pop())
                stack.pop()
            else:
                return 'Invalid expression'
        while len(stack) != 0:
            queue.append(stack.pop())
        result = []
        for i in queue:
            if i.isdigit() or '.' in i:
                result.append(i)
            elif i in signs and len(result) == 1:
                number1 = float(result.pop())
                if i == '-':
                    result.append(-number1)
                else:
                    result.append(number1)
            else:
                number1 = float(result.pop())
                number2 = float(result.pop())
                if i == '+':
                    val = number2 + number1
                    result.append(val)
                elif i == '-':
                    val = number2 - number1
                    result.append(val)
                elif i == '*':
                    val = number2 * number1
                    result.append(val)
                elif i == '/':
                    try:
                        val = number2 / number1
                        result.append(val)
                    except ZeroDivisionError:
                        return 'Division by zero'
        return str(round(float(result[0]), 3))
    except ValueError:
        return 'Invalid expression'
    except TypeError:
        return 'Unknown variable'
    except IndexError:
        return 'Invalid identifier'


def process_sign(sing):
    """Handle math signs."""
    if len(sing) == 1:
        return sing
    elif sing.count('+') == len(sing):
        return '+'
    elif (sing.startswith('*') or sing.startswith('/')) and len(sing) != 1:
        return 'Invalid expression'
    else:
        z = sing.count('-')
        if z != len(sing):
            return 'Invalid expression'
        elif z > 1 and z % 2 == 0:
            return '+'
        elif z >= 1 and z % 2 != 0:
            return '-'


def return_variable(user_input):
    """Print variable that user defined early."""
    for key in dict_variables.keys():
        if user_input == key:
            print(dict_variables[key])
            break
    else:
        return 'Unknown variable'


def assignment(variables):
    """Add variables to dictionary {dict_variables}."""
    index = variables.find('=')
    key = variables[:index]
    value = variables[index + 1:]
    if not key.isalpha():
        return 'Invalid identifier'
    elif value in dict_variables:
        dict_variables[key] = dict_variables[value]
    for _ in value:
        if value.isdigit() or (value[0].isdigit() and value[-1].isdigit() and '.' in value):
            dict_variables[key] = value
        else:
            print('Invalid assignment')


dict_variables = {}
signs = ('+', '-', '/', '*')


if __name__ == "__main__":
    expression('1')
    print('main')
