# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639
import sys

def sol1(): # 이진 탐색 트리를 만들어 진행
    sys.setrecursionlimit(10**6)

    class TreeNode():
        def __init__(self, val=None, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    root = None

    # 이진 탐색 트리 만들기 O(N)
    def insertNode(node, new_node):
        if not node:
            return new_node

        if node.val > new_node.val:
            node.left = insertNode(node.left, new_node)
        else:
            node.right = insertNode(node.right, new_node)

        return node

    for line in sys.stdin:
        node = int(line.strip())
        new_node = TreeNode(node)

        if not root:
            root = new_node
            continue

        insertNode(root, new_node)

    # 후위 순회 출력
    result = []
    def postorder(node):
        if not node:
            return
        
        postorder(node.left)
        postorder(node.right)
        result.append(str(node.val))

    postorder(root)
    print("\n".join(result))

def sol2():
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    result = []

    preorder_list = []
    for data in sys.stdin:
        preorder_list.append(int(data))
    
    def postorder(preorder_list):
        if not preorder_list:
            return
        
        # root
        root = preorder_list[0]
        
        split = len(preorder_list)

        for i in range(1, len(preorder_list)):
            if preorder_list[i] > root:
                split = i
                break

        postorder(preorder_list[1:split])
        postorder(preorder_list[split:])
        result.append(str(root))
    
    postorder(preorder_list)
    print("\n".join(result))

sol2()
