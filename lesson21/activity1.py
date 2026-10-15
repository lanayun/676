input("XOR swap - exchange two values without a third variable")
print(" Before: a=5,b=9")
a,b=5,9
a^=b;b^=a;a^=b
print("after:a=",a," b=",b)
n=int(input("enter a number(try3)"))
guess = input("After XOR swap of "+str(n)+"and what does n becone")
a,b=n,8
a^=b;b^=a;a^=b
input("XOR swap exchanges the values.")
print("n became:",a,"your guess:",guess)