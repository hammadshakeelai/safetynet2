def even(n):
    return n%2==0
def main():
    n=int(input("enter n: "))
    if even(n):
        print("even")
    else:
        print("odd")
main()