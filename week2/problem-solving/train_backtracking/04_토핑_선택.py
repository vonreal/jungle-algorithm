# 부분집합

# 각 토핑을 넣거나/안넣거나 선택할 수 있다.
# 가능한 모든 피자 조합을 구하라. (아무것도 안 넣는 것 포함)

# Example 1:
# Input: toppings = [페퍼로니, 치즈, 올리브]
# Output: [
#   [], 
#   [페퍼로니], 
#   [치즈], 
#   [올리브], 
#   [페퍼로니, 치즈], 
#   [페퍼로니, 올리브], 
#   [치즈, 올리브], 
#   [페퍼로니, 치즈, 올리브]
# ]

# Example 2:
# Input: toppings = [햄, 파인애플]
# Output: [[], [햄], [파인애플], [햄, 파인애플]]

toppings = ["페퍼로니", "치즈", "올리브"]

result = []

def backtraking(start, combination):
    result.append(combination[:])
    if start == len(toppings):
        return 
    
    for index in range(start, len(toppings)):
        combination.append(toppings[index])
        backtraking(index + 1, combination)
        combination.pop()

backtraking(0, [])
print(result)
