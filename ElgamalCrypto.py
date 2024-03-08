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
    en_msg = [char for char in data]
    s = cryptoMath.mod_exp(y, k, p)
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])
        
    print("c1 ", c1, "\nc2 ", en_msg, "\n")
    return c1,  en_msg


def ElgamalDecrypt(cipher, pvK, p):
    dr_msh = []
    # Unpack the ciphertext tuple
    
    
    a, b = cipher
    print("b : ",b)
    
    # Extract components of the private key
    if cryptoMath.mod_exp(a, p-1, p) == 1:
        x = cryptoMath.mod_exp(a, p-1-pvK, p)
        print("c2 after calculate ", x)
        plaintext = b * x
    else:
        print("Something went wrong with ciphertext or private key")
    
    return plaintext 
