from LamportGenerator import LamportGenerator
import math
from Hashfunction import Hashfunction
from Signature import Signature


class MerkleTree:
    def __init__(self, size, usedHashFunction):
        if not self.twoIsBase(size):
            print("size has to be a power of two")
            return None
        self.hashFunction = Hashfunction(usedHashFunction)
        self.generator = LamportGenerator(self.hashFunction)
        self.size = size
        self.unusedLeafs = []
        self.rootNode = self.initializeTree()
    
    def twoIsBase(self, number):
        result = 1
        while result < number:
            result = result * 2
        return result == number

    def initializeTree(self):
        rootNode = self.initializeTreeUtil(1)
        return rootNode
        
    def initializeTreeUtil(self, level):
        if level < self.size:
            leftChild = self.initializeTreeUtil(level * 2)
            rightChild = self.initializeTreeUtil(level * 2)
        else:
            newLeaf = Leaf(self.hashFunction, self.generator.createKeyPair())
            self.unusedLeafs.append(newLeaf)
            return newLeaf
        newNode = Node(self.hashFunction, leftChild, rightChild)
        leftChild.setParent(newNode)
        leftChild.setSibling(rightChild)
        rightChild.setParent(newNode)
        rightChild.setSibling(leftChild)
        return newNode
    
    def signMessage(self, message):
        usedLeaf = self.pickLeaf()
        print("Hash used Leaf:")
        keyPair = usedLeaf.getKeyPair()
        singleSignature = self.generator.createSignatureForMessage(message, keyPair)
        leaf = usedLeaf
        hashesNeededToVerify = self.getHashesOfSiblings(leaf)
        return Signature(keyPair[0], singleSignature, hashesNeededToVerify)
            

    
    def getHashesOfSiblings(self, leafnode):
        hashes = []
        currentNode = leafnode
        while currentNode.parent != None:
            print(currentNode.getHashValue())
            hashes.append(currentNode.sibling.getHashValue())
            currentNode = currentNode.parent
        print("\n")
        return hashes
        
    def pickLeaf(self):
        return self.unusedLeafs.pop()
    
    def getRootCertificate(self):
        return self.rootNode.getHashValue()




class Node:
    def __init__(self, hashFunction, leftChild, rightChild):
        self.parent = None
        self.sibling = None
        self.hashFunction = hashFunction
        self.rightChild = rightChild
        self.leftChild = leftChild
        self.hashValue = hashFunction.getHexHash(Hashfunction.concat(rightChild.getHashValue(), leftChild.getHashValue()))
    
    def setParent(self, parent):
        self.parent = parent

    def setSibling(self, sibling):
        self.sibling = sibling

    def getHashValue(self):
        return self.hashValue

        
class Leaf:
    def __init__(self, hashFunction, keyPair):
        self.parent = None
        self.sibling = None
        self.hashFunction = hashFunction
        self.hashValue = hashFunction.getHexHash(keyPair[0])
        self.keyPair = keyPair
    
    def getHashValue(self):
        return self.hashValue

    def setParent(self, parent):
        self.parent = parent

    def setSibling(self, sibling):
        self.sibling = sibling
    
    def getKeyPair(self):
        return self.keyPair


