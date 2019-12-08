import hashlib

class LamportVerifier:
    def __init__(self, usedHashfunction):
        if usedHashfunction == "sha512":
            self.hashFunction = hashlib.sha512
        elif usedHashfunction == "sha256":
            self.hashFunction = hashlib.sha256
        elif usedHashfunction == "md5":
            self.hashFunction = hashlib.md5
        else:
            print("No valid option.")

    def verify(self, message, signature, publicKey):
        inconsistent = False
        messageHashBin = bin(int(self.hashFunction(message).hexdigest(), 16))
        for digit, preHashedPair, toHash in zip(messageHashBin[2:], publicKey, signature):
            hashOfSigDigit = self.hashFunction(str(toHash).encode()).hexdigest()
            if digit == "0":
                if not toHash == preHashedPair[0]:
                    inconsistent = True
                    break
            if digit == "1":
                if not toHash == preHashedPair[1]:
                    inconsistent = True
                    break
        return not inconsistent
        



    