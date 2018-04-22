'''
Important to note since this was taken from the book that you should first install the package pythonds in your shell.
3) Extend the buildParseTree function to handle mathematical expressions that do not
have spaces between every character.
4) Extend the buildParseTree and evaluate functions to handle boolean statements.
Remember that "not" is a unary operator, so this will complicate your code somewhat.
'''

from pythonds.trees.binaryTree import BinaryTree
from pythonds.basic.stack import Stack

def buildParseTree(fpexp):
    fplist = []
    num = ''
    # if there are no spaces then this code would execute. 
    if ' ' not in fpexp:
        # go through each character in the string.
        for chr in fpexp:
            # if the character is not the list, then add it to the num string.
            if chr not in ['(', '+', '-', '*', '/', ')', '|', '<', '>', '!', '==', '!=', '<=', '>=', 'not', 'is', 'and', 'or']:
                num = num + chr
            # if it's in the list, and the num isn't empty, append num to the list. Reset num, and append the character.
            if chr in ['(', '+', '-', '*', '/', ')', '&&', '|', '<', '>', '!', '==', '!=', '<=', '>=', 'not', 'is', 'and', 'or']:
                if num != '':
                    fplist.append(num)
                num = ''
                fplist.append(chr)
    else:
        fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')', '&&', '|', '<', '>', '!', '==', '!=', '<=', '>=', 'not', 'is', 'and', 'or']:
            currentTree.setRootVal(i)
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/', '&&', '|', '<', '>', '!', '==', '!=', '<=', '>=', 'not', 'is', 'and', 'or']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def main():
    print('With Spaces: ')
    pt = buildParseTree("( ( 10 + 5 ) * 3 )")
    pt.postorder()
    print('Without Spaces: ')
    pt = buildParseTree("((10+5)*3)")
    pt.postorder()
    print('Boolean Statements')
    pt = buildParseTree("( x != y )")
    pt.postorder()

main() 