
from LamportVerifier import LamportVerifier
from Hashfunction import Hashfunction
from Signature import Signature

class MerkleVerifier:
    def __init__(self, hashFunction):
        self.hashFunction = Hashfunction(hashFunction)
        self.lamportVerifier = LamportVerifier(self.hashFunction)


    def verify(self, message, signature, certificate):
        oneTimeSig = signature.getOneTimeSignature()
        merkleSig = signature.getMerkleTreeSignature()
        publicKey = signature.getPublicKey()
        if not self.lamportVerifier.verify(message, oneTimeSig, publicKey):
            return False
        return self.publicKeyBelongstoCert(publicKey, merkleSig, certificate)



    def publicKeyBelongstoCert(self, publicKey, MerkleTreeSignature, certificate):
        hashValue = self.hashFunction.getHexHash(publicKey)
        for hashNode in MerkleTreeSignature:
            print(hashValue)
            hashValue = self.hashFunction.getHexHash(Hashfunction.concat(str(hashValue) , str(hashNode)))
        print(hashValue)
        print(certificate)
        return hashValue == certificate
        