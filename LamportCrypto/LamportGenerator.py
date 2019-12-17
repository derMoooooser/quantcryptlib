import secrets
import hashlib
import HashFunction

class LamportGenerator:
    def __init__(self, usedHashFunction):
        self.hashFunction = usedHashFunction
    
    def createKeyPair(self):
        if self.hashFunction.getTypeOf() == hashlib.sha512:
            privateKey = self.createRandomSequence(512)
            publicKey = self.hashSequence(privateKey)
        if self.hashFunction.getTypeOf() == hashlib.sha256:
            privateKey = self.createRandomSequence(256)
            publicKey = self.hashSequence(privateKey)
        if self.hashFunction.getTypeOf() == hashlib.md5:
            privateKey = self.createRandomSequence(128)
            publicKey = self.hashSequence(privateKey)
        return publicKey, privateKey
    

            
    def createRandomSequence(self, n):
        sequence = []
        for i in range(0, n):
            sequence.append((secrets.randbits(2048),secrets.randbits(2048)))
        return sequence

    def hashSequence(self, sequence):
        sequenceOfHashes = []
        for number in sequence:
            sequenceOfHashes.append(self.hashFunction.getHexHash(number[0]),self.hashFunction.getHexHash(number[1]))
        return sequenceOfHashes
            
    def createSignatureForMessage(self, message, keyPair):
        messageHashBin = bin(int(self.hashFunction.getHexHash(message), 16))
        signature = []
        for digit, numberTuple in zip(messageHashBin[2:], keyPair[1]):
            if digit == "0":
                signature.append(numberTuple[0])
            else:
                signature.append(numberTuple[1])
        return signature

