from time import sleep

def fibo1(a, b):
    if a == 0:
        print(b)
    
    secuencia = a + b
    print(secuencia)
    sleep(2)
    fibo2(secuencia, b)

def fibo2(c, d):
    secuencia = c + d
    print(secuencia)
    fibo1(d, secuencia)

def main():
    fibo1(0,1)

def nigger():
    pass

if __name__ == "__main__":
    main()
