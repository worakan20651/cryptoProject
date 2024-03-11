import cryptoMath
import random

def ElgamalEncrypt(pbK, data): 
    # if('.' in data):
    #     with open(data, 'rb') as file:
    #         bytes_read = file.read() 
    # else:
    #     bytes_read = input()
    # # method ที่ใช้ในการเข้ารหัส  ให้เข้ารหัสได้ทั้งข้อความจากหน้าจอและไฟล์ประเภทต่างๆ
    # # Input : key ที่ใช้ในการ...รหัส, Plaintext โดยที่ Plaintext เป็นได้ทั้ง ข้อความที่ได้รับมาจากหน้าจอ หรือ ไฟล์ชนิดต่างๆ
    # # Output: Ciphertext file
    p, g, y = pbK
    k = random.randint(1, p - 2)
    
    while cryptoMath.gcd(k,p-1) != 1:
        k = random.randint(1,p-2)
    
    c1 = cryptoMath.mod_exp(g, k, p)
    
    # break character into list
    # print("Data = ",data)
    # en_msg = [char for char in data]
    cipher = data.decode("utf-8")
    # print("message before encryption = ", en_msg , " \n")
    
    s = cryptoMath.mod_exp(y, k, p)
    en_msg = []
    # encrypt data one by one
    for i in range(len(cipher)):
        en_msg.append(s * ord(cipher[i]))
        # print("charactor : ",cipher[i], " into : ", en_msg[i])
        
    # print("cipher type = ", type(en_msg))
        
    # print("c1 ", c1, "\nc2 ", en_msg, "\n")
    return c1,  en_msg


def ElgamalDecrypt(cipher, pvK, p):
    dr_msg = []
    # Unpack the ciphertext tuple
    
    
    a, b = cipher
    # print("b : ",b)
    
    # Extract components of the private key
    if cryptoMath.mod_exp(a, p-1, p) == 1:
        x = cryptoMath.mod_exp(a, p-1-pvK, p)
    else:
        return "Something went wrong with ciphertext or private key" 
    
    print(type(cipher))
    
    for i in range(len(b)):
        c = int(b[i])
        t = chr((c*x)%p)
        # print("ch is ", t)
        dr_msg.append(t)
    
    with open('testTxT.txt', 'w')as f:
        for i in dr_msg:
            f.write(i)
    
    return f
