import hashlib

class Hashfunction:
    def __init__(self, usedHashfunction):
        if usedHashfunction == "sha512":
            self.hashFunction = hashlib.sha512
            self.algortihm = "sha512"
        if usedHashfunction == "sha256":
            self.hashFunction = hashlib.sha256
            self.algorithm = "sha256"
        if usedHashfunction == "md5":
            self.hashFunction = hashlib.md5
            self.algorithm = "md5"
    
    def getHexHash(self, message):
        if type(message) != bytes:
            message = str(message).encode()
        return self.hashFunction(message).hexdigest()
        
    def getTypeOf(self):
        return self.hashFunction
        
    @staticmethod
    def concat(hash1, hash2):
        if int(hash1, 16) > int(hash2, 16):
            return hash1 + hash2
        else:
            return hash2 + hash1 