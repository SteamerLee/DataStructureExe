#！/usr/bin/python
# -*- coding: utf-8 -*-#

'''
---------------------------------
 Name:         back_lookup
 Description:  
 Author:       Steamer
 Date:         03/03/2019
---------------------------------
'''


class BTNode(object):
    def __init__(self, val=None, left_node=None, right_node=None):
        self.val = val
        self.left_node = left_node
        self.right_node = right_node


class BiTree(object):

    def __init__(self, data):
        self.data = iter(data)

    def createBiTree(self, tree=None):
        try:
            next_data = next(self.data)
            if next_data is '*':
                tree = None
            else:
                tree = BTNode(next_data)
                tree.left_node = self.createBiTree(tree.left_node)
                tree.right_node = self.createBiTree(tree.right_node)

        except Exception as error:
            print(error)
        return tree

    def pre_lookup(self, node):

        if node is not None:
            print(node.val)  # pre
            self.pre_lookup(node.left_node)
            self.pre_lookup(node.right_node)

    def middle_lookup(self, node):

        if node is not None:
            self.middle_lookup(node.left_node)
            print(node.val)  # middle
            self.middle_lookup(node.right_node)

    def post_lookup(self, node):

        if node is not None:
            self.post_lookup(node.left_node)
            self.post_lookup(node.right_node)
            print(node.val)  # post


def main():

    input_data = input('Pls input BiTree value\n')
    data = list(input_data)
    tree = BiTree(data)
    print('Start to create BiTree!')
    Bitree = tree.createBiTree()
    print('BiTree created!')
    print('-----------------------------------------')
    print('Pre-Search:')
    print(tree.pre_lookup(Bitree))
    print('-----------------------------------------')
    print('Middle-Search:')
    print(tree.middle_lookup(Bitree))
    print('-----------------------------------------')
    print('Post-Search:')
    print(tree.post_lookup(Bitree))
    print('Done!')

if __name__ == '__main__':
    main()