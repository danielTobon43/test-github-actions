from logging import raiseExceptions


def sum(a, b):  
    return a + b


def main():
    res = sum(10, 5)
    print(f'The sum is {res}')
    

if __name__ == "__main__":
    main()