# 조합

# 후보자들 중에서 k명을 뽑아 팀을 구성하라.
# 순서는 상관없음. (AB와 BA는 같은 팀)

# Example 1:
# Input: members = [A, B, C, D], k = 2
# Output: [AB, AC, AD, BC, BD, CD]

# Example 2:
# Input: members = [A, B, C], k = 2
# Output: [AB, AC, BC]

k = 2
members = ["A", "B", "C", "D"]
result = []

def backtrack(start, current_combination):
    if len(current_combination) == k:
        result.append("".join(current_combination))
        return
    
    for i in range(start, len(members)):
        current_combination.append(members[i])
        backtrack(i + 1, current_combination)
        current_combination.pop()

backtrack(0, [])
print(result)