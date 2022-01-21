a=int(input("enter no"))
b=int(input('enter no'))
try:
    print('resource open')
    print(a/b)
    k=int(input('enter no'))
    print(k)
except ZeroDivisionError as e:
    print('wrong',e)
except ValueError as e:
    print('wrongv',e)
except Exception as e:
    print('wrongo',e)

finally:
    print('resource closed')
