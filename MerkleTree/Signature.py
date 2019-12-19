class Signature:
    def __init__(self, publicKey, oneTimeSignature, MerkleTreeSignature):
        self.publicKey = publicKey
        self.oneTimeSignature = oneTimeSignature
        self.MerkleTreeSignature = MerkleTreeSignature

    def getPublicKey(self):
        return self.publicKey
    
    def getOneTimeSignature(self):
        return self.oneTimeSignature
    
    def getMerkleTreeSignature(self):
        return self.MerkleTreeSignature
    