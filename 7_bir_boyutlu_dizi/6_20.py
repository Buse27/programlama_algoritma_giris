# Affine şifre çözme 
def cters(g):
    for i in range(1,27):
        if ((g*i)%26==1):
            return i
sm=input("şifreli kelime: ").upper(); m=""
a=int(input("Anahtar (a): ")); b=int(input("Anahtar (b): "))
ta=cters(a)
for i in range(len(sm)):
    y=ord(sm[i])-65
    if (y-b<0):
        y+=26
    m+=chr((ta*(y-b))%26+65)
print("\nşifresi çözülmüş kelime: %s"%m)                
