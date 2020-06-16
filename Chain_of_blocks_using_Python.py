import hashlib

def sha256(data):
    result=hashlib.sha256(data.encode())
    return result.hexdigest()

class Block:
    def __init__(self,notes,prev):
        self.notes=notes
        self.prevHash=prev
        self.curHash=sha256(str(notes)+str(prev))
    def changeContent(self,newContent):
        self.notes=newContent
        self.curHash=sha256(str(newContent)+str(prevHash))
        

class Blockchain:
    def __init__(self,chain=None):
        self.chain=[]
    def prevHash(self):
        return self.chain[-1].curHash
    def addBlock(self,blockNotes,prevHash):
        block=Block(blockNotes,prevHash)
        self.chain.append(block)
    def isChainValid(self):
        l=self.chain
        valid=True
        for i in range(1,len(l)):
            curBlock=l[i]
            prevBlock=l[i-1]
            if curBlock.prevHash!=prevBlock.curHash:
                valid=False
        return valid
    def printChain(self):
        l=self.chain
        for i in range(len(l)):
            print("*********************")
            print("Block ",i)
            print("Notes ",l[i].notes)
            print("CurHahs ",l[i].curHash)
            print("PrevHash ",l[i].prevHash)
            print("*********************")
    def printTamperedBlock(self):
        l=self.chain
        for i in range(1,len(l)):
            curBlock=l[i]
            prevBlock=l[i-1]
            if curBlock.prevHash!=prevBlock.curHash:
                print("Block after or equals ",i,"is tampered")
                break

print("Block chain using python")
print("Creating a genesis block")
blockchain1=Blockchain()
print("Addidng genesis block manually")
blockchain1.addBlock("Hi this is genesis",0)

n=input("ENter no of blocks u want to add")
n=int(n)
while n>0:
    notes=input("Enter the data for the block")
    prevhash=blockchain1.prevHash()
    #newBlock=Block(notes,prevhash)
    blockchain1.addBlock(notes,prevhash)
    if blockchain1.isChainValid():
        print("Block chain is not tampered yet")
    else:
        print("Block Chain is breaked")
    blockchain1.printChain()
    n-=1
print("Attempting to tamper blockchain")

blockchain1.chain[2]=Block("Tampering",blockchain1.chain[1].curHash)

if blockchain1.isChainValid():
    print("Blockchain has implementation fault")
else:
    print("Your blochcchain has been tampered")

print("PRINTING BLOCKCHAIN AFTER TAMPERING")

blockchain1.printChain()

blockchain1.printTamperedBlock()
