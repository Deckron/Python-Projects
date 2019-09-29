
summ=0
network=0
w1=0
w2=0
w3=0
num = 1
x=0
epoch=0
while x!=4:
    x=0
    epoch+=1
    print("starting epoch ", epoch)
    for y in range(4):
        inp1=int(input("first number: "))
        inp2=int(input("second number: "))
        inp3=int(input("third number: "))
        target=int(input("give target number: "))
        summ= inp1*w1+ inp2*w2 +inp3*w3
        ##print("target",target)
        ##print("sum",summ)
        if summ>0:
            network=1
        if summ==0:
            network=0
        if summ<0:
            network=-1
        ##print("network",network)
        if network == target:
           ## print("equals triggered")
            print("delta weights= (0,0,0)")
            x+=1
            ##print(x)
        if network != target:
            dw1=target*inp1
           ## print("dw1",dw1)
            dw2=target*inp2
          ##  print("dw2",dw2)
            dw3=target*inp3
          ##  print("dw3",dw3)
            w1= dw1+w1
            w2= dw2+w2
            w3= dw3+w3
            print("not equals triggered")
            print(w1,w2,w3)
        if x==4:
            print("found the correct weights")
            break
print (w1, w2, w3)
print("epoch ",epoch)

    
    
