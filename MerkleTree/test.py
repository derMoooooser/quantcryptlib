from Merkletree import MerkleTree
from MerkleVerifier import MerkleVerifier
from HashFunction import Hashfunction

M = MerkleTree(256,"sha256")
sig = M.signMessage("Message")
RootCert = M.getRootCertificate()
leaf = M.pickLeaf()


V = MerkleVerifier("sha256")
print(V.verify("Message", sig, RootCert))