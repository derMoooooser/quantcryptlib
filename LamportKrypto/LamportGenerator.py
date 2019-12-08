import hashlib
import secrets

#LamportGenerator is a class used to generate Lamport-Private and Public-Keys.
#A Lamport-Keypair can only be used once, so with every message a new keypair has to be generated
class LamportGenerator:
    def __init__(self, usedHashfunction):
        if usedHashfunction == "sha512":
            self.hashFunction = hashlib.sha512
        elif usedHashfunction == "sha256":
            self.hashFunction = hashlib.sha256
        elif usedHashfunction == "md5":
            self.hashFunction = hashlib.md5
        else:
            print("No valid option.")
    
    def createKeyPair(self):
        if self.hashFunction == hashlib.sha512:
            self.privateKey = self.createRandomSequence(512)
            self.publicKey = self.hashSequence(self.privateKey)
        if self.hashFunction == hashlib.sha256:
            self.privateKey = self.createRandomSequence(256)
            self.publicKey = self.hashSequence(self.privateKey)
        if self.hashFunction == hashlib.md5:
            self.privateKey = self.createRandomSequence(128)
            self.publicKey = self.hashSequence(self.privateKey)
    
    def getPrivateKey(self):
        return self.privateKey

    def getPublicKey(self):
        return self.publicKey
            
    def createRandomSequence(self, n):
        sequence = []
        for i in range(0, n):
            sequence.append((secrets.randbits(2048),secrets.randbits(2048)))
        return sequence

    def hashSequence(self, sequence):
        sequenceOfHashes = []
        for number in sequence:
            sequenceOfHashes.append(self.hashFunction(str(number).encode()).hexdigest())
        return sequenceOfHashes
            
    def createSignatureForMessage(self, message):
        messageHashBin = bin(int(self.hashFunction(message).hexdigest(), 16))
        signature = []
        for digit, numberTuple in zip(messageHashBin[2:], self.privateKey):
            if digit == "0":
                signature.append(numberTuple[0])
            else:
                signature.append(numberTuple[1])
        return signature
