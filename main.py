def additions(d1,d2):
	return d1 + d2

def subtraction(d1,d2):
	return d1 - d2

def multiply(d1,d2):
	return d1 * d2

def division(d1,d2):
    if d2 == 0:
        return "На ноль делить нельзя"
    else:
        return d1 / d2  



if __name__ == '__main__':
    print(additions(4,2))
    print(subtraction(4,2))
    print(multiply(4,2))
    print(division(4,2))
