PATRON = "010002000100"

while True:
    i = input("n: ")
    n = abs(int(i))

    an = PATRON [(n - 1) % len (PATRON)]
    print(f"a({n}) = {an}\n")
