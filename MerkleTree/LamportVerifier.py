import hashlib

class LamportVerifier:
    def __init__(self, usedHashfunction):
        self.hashFunction = usedHashfunction

    def verify(self, message, signature, publicKey):
        inconsistent = False
        messageHashBin = bin(int(self.hashFunction.getHexHash(message), 16))
        for digit, preHashedPair, toHash in zip(messageHashBin[2:], publicKey, signature):
            hashOfSigDigit = self.hashFunction.getHexHash(toHash)
            if digit == "0":
                if not hashOfSigDigit == preHashedPair[0]:
                    inconsistent = True
                    break
            if digit == "1":
                if not hashOfSigDigit == preHashedPair[1]:

                    inconsistent = True
                    break
        return not inconsistent
        



    