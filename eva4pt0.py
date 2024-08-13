"""Returns action most efficacious for achieving value from user's perspective, accounting for act-state dependence."""

def enter() -> None:
    print("")

enter()
actions: list[str] = []
action: str = input("Specify an action to evaluate, e.g., 'studying,' 'mowing the lawn,' etc.: ")

while action.lower() != ("done"): #compiles list of actions to test
    actions.append(action)
    action = input("Input another action. If there are no more actions you wish to evaluate, input 'done': ")
enter()

possibles: list[str] = []
possible: str = input("Specify a possibility to test against, e.g., 'I will pass the test,' 'my brother-in-law will visit me,' etc.: ")

while possible.lower() != ("done"): #compiles list of possible world-states to test against
    possibles.append(possible)
    possible = input("Input another possibility. If there are no more possibilities you wish to test against, input 'done': ")
enter()

values_matrix: list[list[int]] = []
rows: int = len(actions)
columns: int = len(possibles)

index_one: int = 0
index_two: int = 0
empty: list[int] = []

for row in range(rows): #compiles matrix of utilities dependent upon world-states
    empty = []
    index_two = 0
    for column in range(columns):
        empty.append(int(input(f"On a scale of 1-10, how much do I value {actions[index_one]} if I know that {possibles[index_two]}?: ")))
        index_two += 1
    values_matrix.append(empty)
    index_one += 1
enter()

probables_matrix : list[list[int]] = []
action_index: int = 0

while action_index < rows: #compiles matrix of probabilities dependent upon actions
    empty = []
    for possible in possibles:
        empty.append(int(input(f"On a scale of 1-100, how confident am I that {possible}, assuming I have decided upon {actions[action_index]}?: ")))
    probables_matrix.append(empty)
    action_index += 1

final_matrix: list[list[int]] = []
row_index: int = 0
column_index: int = 0

while row_index < rows: #performs element-wise multiplication of values_matrix and probables_matrix
    empty = []
    while column_index < columns:
        empty.append(values_matrix[row_index][column_index] * probables_matrix[row_index][column_index])
        column_index += 1
    final_matrix.append(empty)
    column_index = 0
    row_index += 1

row_index = 0
finals : list[int] = []

while row_index < rows: #sums each row in final_matrix
    value = 0
    for num in final_matrix[row_index]:
        value += num
    finals.append(value)
    row_index += 1
 
high_action: int = finals[0]
high_action_index: int = 0
high_action_test_index: int = 1

while high_action_test_index < rows: #identifies most efficacious action and its location within array actions
    if finals[high_action_test_index] > high_action:
        high_action = finals[high_action_test_index]
        high_action_index = high_action_test_index
    high_action_test_index += 1

enter()
print(f"You should consider {actions[high_action_index]}.") #returns result
enter()
