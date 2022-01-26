def summ(a,b,c=0):
    print(f'a={a} ,b={b}, c={c}')
    return a+b+c
sm1=summ(1,2)
print(sm1)
sm3=summ(1,2,5)
print(sm3)
sm4=summ(a=5,c=1,b=3)
print(sm4)

def new_sum(*args):
    print(args)
    result=0
    for i in args:
        result+=i
    return result
sm5=new_sum(1,2,3,6,5)
print(sm5)

def new_func(**kwargs):
    print(kwargs['name'], kwargs['age'])
new_func(name='mah',age='banoo')