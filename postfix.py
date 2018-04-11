from pythonds.basic.stack import Stack

def postfixEval(expr):
    operandStack = Stack()
    tokenLits = expr.split()
    
    for toke in tokelist:
        if token in "0123456789":
            perandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            perand1 = operandStack.pop()
            result = doMath(token,operand1,oeprand2)
            operandStack.push(resutl)
    return operandStack.pop()
def doMth(op,op1,op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
         return op1 - op2