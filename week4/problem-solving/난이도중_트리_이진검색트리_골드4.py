# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639
import sys
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