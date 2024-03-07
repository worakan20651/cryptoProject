import primeGenerate
import ElgamalGenerator

req = input("Size and Filename (12 filename.ex) : ")
data = req.split(" ")

prime = primeGenerate.gen_prime(int(data[0]),data[1])

pbK,pvK = ElgamalGenerator.run(prime)

print("(public key) and private key : ",pbK,pvK)