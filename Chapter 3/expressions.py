import Stack

prec={}
prec['+'] = 1
prec['-'] = 1
prec['*'] = 2
prec['/'] = 2

def evaluate(n1,n2,top):
    if top == '+':
        result=n1+n2
    elif top == '-':
        result=n1-n2
    elif top == '*':
        result=n1*n2
    else:
        result = n1/n2
    return result

OpStack = Stack.Stack()
NumStack = Stack.Stack()

expression = input('Enter expression: ')

terms = list(expression)

for term in terms:
    if term not in ['+','-','/','*']:
        NumStack.push(int(term))
    else:
        done = False
        while not done:
            top = OpStack.top()
            if top == None:
                OpStack.push(term)
                done = True
            elif (prec[term] > prec[top]):
                OpStack.push(term)
                done=True
            else:
                n2 = NumStack.pop()
                n1 = NumStack.pop()
                top = OpStack.pop()
                result = evaluate(n1,n2,top)
                NumStack.push(result)
done=False
while not done:
    top = OpStack.pop()
    if top == None:
        done = True
    else:
        n2 = NumStack.pop()
        n1 = NumStack.pop()
        result = evaluate(n1,n2,top)
        NumStack.push(result)

print('result='+str(NumStack.pop()))                
    
