def prompt(string, in_ = None):
    string=str(string)
    ok = 0
    while ok != 2:
        if ok < 1:
            ans = input(string)
        if in_:
            if ans in in_:
                ok = 2
            else:
                print("Please choose from",list(in_))
                ok = 0
        else:
            oka = input("Confirm? (Y/n) ").lower().strip()
            if oka == "":
                ok = 2
            elif oka == "n":
                ok = 0
            else:
                ok = 1
    return ans
print("--- 3D print quote ---")
print(" [ This is currency and unit independent ]")
proceed = False
print("Calculation options:\n  1: Price by length\n  2: Price by weight
ans = prompt("Please select: ","12")
byLen = not "12".find(ans)>0
if byLen:
    print("Price by length")
else:
    print("Price by mass")

PerUnit = prompt(eval('print("Enter price by ","length" if byLen else "mass",": ",sep="")'))
length = prompt("Enter length of filament output by 
if not byLen:
    density = prompt("Enter density (thickness) of filament")
