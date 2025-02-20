#Substitution Box
s_box=[['63','7c','77','7b','f2','6b','6f','c5','30','01','67','2b','fe','d7','ab','76'],
['ca','82','c9','7d','fa','59','47','f0','ad','d4','a2','af','9c','a4','72','c0'],
['b7','fd','93','26','36','3f','f7','cc','34','a5','e5','f1','71','d8','31','15'],
['04','c7','23','c3','18','96','05','9a','07','12','80','e2','eb','27','b2','75'],
['09','83','2c','1a','1b','6e','5a','a0','52','3b','d6','b3','29','e3','2f','84'],
['53','d1','00','ed','20','fc','b1','5b','6a','cb','be','39','4a','4c','58','cf'],
['d0','ef','aa','fb','43','4d','33','85','45','f9','02','7f','50','3c','9f','a8'],
['51','a3','40','8f','92','9d','38','f5','bc','b6','da','21','10','ff','f3','d2'],
['cd','0c','13','ec','5f','97','44','17','c4','a7','7e','3d','64','5d','19','73'],
['60','81','4f','dc','22','2a','90','88','46','ee','b8','14','de','5e','0b','db'],
['e0','32','3a','0a','49','06','24','5c','c2','d3','ac','62','91','95','e4','79'],
['e7','c8','37','6d','8d','d5','4e','a9','6c','56','f4','ea','65','7a','ae','08'],
['e7','c8','37','6d','8d','d5','4e','a9','6c','56','f4','ea','65','7a','ae','08'],
['70','3e','b5','66','48','03','f6','0e','61','35','57','b9','86','c1','1d','9e'],
['e1','f8','98','11','69','d9','8e','94','9b','1e','87','e9','ce','55','28','df'],
['8c','a1','89','0d','bf','e6','42','68','41','99','2d','0f','b0','54','bb','16']]

# Substitution Box Ends

def printt(State):
    print()
    for i in range(4):
        for j in range(4):
            print(State[i][j]," ",end="")
        print()
    print()

#AddRoundKey Function 
def AddRoundKey(State,w,rnd,Nb):
    for c in range(Nb):
        State[0][c]=hex(int(State[0][c],16)^int(w[rnd*Nb][c],16)).lstrip('0x').zfill(2)
        State[1][c]=hex(int(State[1][c],16)^int(w[rnd*Nb+1][c],16)).lstrip('0x').zfill(2)
        State[2][c]=hex(int(State[2][c],16)^int(w[rnd*Nb+2][c],16)).lstrip('0x').zfill(2)
        State[3][c]=hex(int(State[3][c],16)^int(w[rnd*Nb+3][c],16)).lstrip('0x').zfill(2)
    
def ShiftRows(State):
    for i in range(0,4):
        State[i]=State[i][i:]+State[i][:i]
    
def MixColumns(State):
    mul2=[['00','02','04','06','08','0a','0c','0e','10','12','14','16','18','1a','1c','1e'],
    ['20','22','24','26','28','2a','2c','2e','30','32','34','36','38','3a','3c','3e'],
    ['40','42','44','46','48','4a','4c','4e','50','52','54','56','58','5a','5c','5e'],
    ['60','62','64','66','68','6a','6c','6e','70','72','74','76','78','7a','7c','7e'],
    ['80','82','84','86','88','8a','8c','8e','90','92','94','96','98','9a','9c','9e'],
    ['a0','a2','a4','a6','a8','aa','ac','ae','b0','b2','b4','b6','b8','ba','bc','be'],
    ['c0','c2','c4','c6','c8','ca','cc','ce','d0','d2','d4','d6','d8','da','dc','de'],
    ['e0','e2','e4','e6','e8','ea','ec','ee','f0','f2','f4','f6','f8','fa','fc','fe'],
    ['1b','19','1f','1d','13','11','17','15','0b','09','0f','0d','03','01','07','05'],
    ['3b','39','3f','3d','33','31','37','35','2b','29','2f','2d','23','21','27','25'],
    ['5b','59','5f','5d','53','51','57','55','4b','49','4f','4d','43','41','47','45'],
    ['7b','79','7f','7d','73','71','77','75','6b','69','6f','6d','63','61','67','65'],
    ['9b','99','9f','9d','93','91','97','95','8b','89','8f','8d','83','81','87','85'],
    ['bb','b9','bf','bd','b3','b1','b7','b5','ab','a9','af','ad','a3','a1','a7','a5'],
    ['db','d9','df','dd','d3','d1','d7','d5','cb','c9','cf','cd','c3','c1','c7','c5'],
    ['fb','f9','ff','fd','f3','f1','f7','f5','eb','e9','ef','ed','e3','e1','e7','e5']]

    mul3=[['00','03','06','05','0c','0f','0a','09','18','1b','1e','1d','14','17','12','11'],
    ['30','33','36','35','3c','3f','3a','39','28','2b','2e','2d','24','27','22','21'],
    ['60','63','66','65','6c','6f','6a','69','78','7b','7e','7d','74','77','72','71'],
    ['50','53','56','55','5c','5f','5a','59','48','4b','4e','4d','44','47','42','41'],
    ['c0','c3','c6','c5','cc','cf','ca','c9','d8','db','de','dd','d4','d7','d2','d1'],
    ['f0','f3','f6','f5','fc','ff','fa','f9','e8','eb','ee','ed','e4','e7','e2','e1'],
    ['a0','a3','a6','a5','ac','af','aa','a9','b8','bb','be','bd','b4','b7','b2','b1'],
    ['90','93','96','95','9c','9f','9a','99','88','8b','8e','8d','84','87','82','81'],	
    ['9b','98','9d','9e','97','94','91','92','83','80','85','86','8f','8c','89','8a'],
    ['ab','a8','ad','ae','a7','a4','a1','a2','b3','b0','b5','b6','bf','bc','b9','ba'],
    ['fb','f8','fd','fe','f7','f4','f1','f2','e3','e0','e5','e6','ef','ec','e9','ea'],	
    ['cb','c8','cd','ce','c7','c4','c1','c2','d3','d0','d5','d6','df','dc','d9','da'],	
    ['5b','58','5d','5e','57','54','51','52','43','40','45','46','4f','4c','49','4a'],
    ['6b','68','6d','6e','67','64','61','62','73','70','75','76','7f','7c','79','7a'],	
    ['3b','38','3d','3e','37','34','31','32','23','20','25','26','2f','2c','29','2a'],
    ['0b','08','0d','0e','07','04','01','02','13','10','15','16','1f','1c','19','1a']]
    for i in range(4):
        S0i=int(State[0][i],16)
        S1i=int(State[1][i],16)
        S2i=int(State[2][i],16)
        S3i=int(State[3][i],16)
        S0=hex((int(mul2[int(State[0][i][0],16)][int(State[0][i][1],16)],16))^(int(mul3[int(State[1][i][0],16)][int(State[1][i][1],16)],16))^S2i^S3i).lstrip('0x').zfill(2)
        S1=hex(S0i^(int(mul2[int(State[1][i][0],16)][int(State[1][i][1],16)],16))^(int(mul3[int(State[2][i][0],16)][int(State[2][i][1],16)],16))^S3i).lstrip('0x').zfill(2)
        S2=hex(S0i^S1i^(int(mul2[int(State[2][i][0],16)][int(State[2][i][1],16)],16))^(int(mul3[int(State[3][i][0],16)][int(State[3][i][1],16)],16))).lstrip('0x').zfill(2)
        S3=hex((int(mul3[int(State[0][i][0],16)][int(State[0][i][1],16)],16))^S1i^S2i^(int(mul2[int(State[3][i][0],16)][int(State[3][i][1],16)],16))).lstrip('0x').zfill(2)
        State[0][i]=S0
        State[1][i]=S1
        State[2][i]=S2
        State[3][i]=S3

def SubBytes(a):
        #To Substitue
    for i in range(4):
        for j in range(4):
            for k in range(2):
                if k==0:
                    if a[i][j][k]=='a':
                        x=10
                    elif a[i][j][k]=='b':
                        x=11
                    elif a[i][j][k]=='c':
                        x=12
                    elif a[i][j][k]=='d':
                        x=13
                    elif a[i][j][k]=='e':
                        x=14
                    elif a[i][j][k]=='f':
                        x=15
                    else:
                        x=int(a[i][j][k])
                else:
                    if a[i][j][k]=='a':
                        y=10
                    elif a[i][j][k]=='b':
                        y=11
                    elif a[i][j][k]=='c':
                        y=12
                    elif a[i][j][k]=='d':
                        y=13
                    elif a[i][j][k]=='e':
                        y=14
                    elif a[i][j][k]=='f':
                        y=15
                    else:
                        y=int(a[i][j][k])
            a[i][j]=s_box[x][y]
    return a

def state(txt):
    State=[]
    ind=0
    for l in range(4):          # A for loop for row entries 
        a =[] 
        for m in range(4):      # A for loop for column entries 
            a.append(hex(ord(txt[ind])).lstrip('0x').zfill(2))
            ind+=1 
        State.append(a)
    State = [[State[j][i] for  j in range(len(State))] for i in range(len(State[0]))] #Converting Rows To Columns
    return State

def xor(a,b):
    li=[hex(int(i,16)^int(j,16)).lstrip('0x').zfill(2) for i,j in zip(a,b)]
    return li

def Rcon(i):
    r_c=['02','00','00','00']
    n=r_c.copy()
    if i<9:
        n[0]=hex(int(n[0])**(i-1)).lstrip('0x').zfill(2)
    elif i==9:
        n[0]=hex(27).lstrip('0x')
    else:
        n[0]=hex(36).lstrip('0x')
    return n

def RotWord(temp):
    for i in range(4):
        temp[i]=temp[i][1:]+temp[i][:1]
    return temp

def SubWord(temp):
        #To Substitue
    for i in range(4):
        x=int(temp[i][0],16)
        y=int(temp[i][1],16)
        temp[i]=s_box[x][y]
    return temp

def KeyExpansion(key,Nk,Nb,Nr):
    i=0
    w=[]
    while(i<Nk):
        w.append([hex(ord(key[4*i])).lstrip('0x').zfill(2),hex(ord(key[4*i+1])).lstrip('0x').zfill(2),hex(ord(key[4*i+2])).lstrip('0x').zfill(2),hex(ord(key[4*i+3])).lstrip('0x').zfill(2)])
        i+=1
    i=Nk
    w = [[w[j][i] for  j in range(len(w))] for i in range(len(w[0]))] #Converting Rows To Columns
    while(i<Nb*(Nr+1)):
        temp=w[i-1].copy()
        if i%Nk==0:
            temp=xor(SubWord(RotWord(temp)),Rcon(i//Nk))
        w.append(xor(w[i-Nk],temp))
        i+=1
    return w

def Cipher(in_msg,key,Nb,Nr,Nk):
    State=state(in_msg)
    rnd=0
    print()
    print('-----------------------------------------------------------------------')
    print()
    print('Round:',rnd)
    print('State:')
    printt(State)
    w=KeyExpansion(key,Nk,Nb,Nr)
    AddRoundKey(State,w,rnd,Nb)
    print('After AddRoundKey:')
    printt(State)
    for rnd in range(1,Nr):
        print()
        print('-----------------------------------------------------------------------')
        print()
        print('Round:',rnd)
        print('State:')
        printt(State)
        SubBytes(State)
        print('After SubBytes:')
        printt(State)
        ShiftRows(State)
        print('After ShiftRows:')
        printt(State)
        MixColumns(State)
        print('After MixColumns:')
        printt(State)
        AddRoundKey(State,w,rnd,Nb)
        print('After AddRoundKey:')
        printt(State)
    print()
    print('-----------------------------------------------------------------------')
    print()
    print('Round:',Nr)
    print('State:')
    printt(State)
    SubBytes(State)
    print('After SubBytes:')
    printt(State)
    ShiftRows(State)
    print('After ShiftRows:')
    printt(State)
    AddRoundKey(State,w,Nr,Nb)
    print('After AddRoundKey:')
    printt(State)

    out_msg=State.copy()
    out_msg = [[out_msg[j][i] for  j in range(len(out_msg))] for i in range(len(out_msg[0]))] #Converting Rows To Columns

    flatten_list = [j for sub in out_msg for j in sub]
    out_msg=" ".join(flatten_list)
    print('Output Cipher Text:',out_msg)
mesg=input('Enter Your Message :')
cip_key=input('Enter Key:')
Cipher(mesg,cip_key,4,10,4)