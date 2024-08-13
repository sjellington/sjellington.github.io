"""Returns action most efficacious from user's perspective for achieving value using Savage's model."""

def enter() -> None:
    print("")

enter()
actions: list[str] = []
action: str = input("Specify an action to evaluate, e.g., 'studying', 'mowing the lawn', etc.: ")

while action.lower() != "done": #compiles list of actions to test
    actions.append(action)
    action = input("Input another action. If there are no other actions you wish to evaluate, input 'done': ")
enter()

possibles: list[str] = []
possible: str = input("Specify a possibility to test against, e.g., 'I will pass the test', 'my brother-in-law will visit me', etc.: ")

while possible.lower() != "done": #compiles list of possible world-states to test against
    possibles.append(possible)
    possible = input("Input another possibility. If there are no more possible states you wish to test against, input 'done': ")
enter()

matrix: list[list[int]] = []
rows: int = len(actions)
columns:int = len(possibles)
index_one: int = 0 

for row in range(rows): #compiles matrix of utilities based upon world-states
    empty: list[int] = []
    index_two: int = 0
    for column in range(columns):
        empty.append(int(input(f"On a scale of 1-10, how much do I value {actions[index_one]} if I know that {possibles[index_two]}?: ")))
        index_two += 1
    matrix.append(empty)
    index_one += 1
enter()

probabilities: list[int] = []
possibles_index: int = 0

while possibles_index < columns: #compiles list of probabilities
    probabilities.append(int(input(f"On a scale of 1-100, how confident am I that {possibles[possibles_index]}?: ")))
    possibles_index += 1
enter()

high_action: int = 0
high_action_index: int = 0
value_index: int = 0

while value_index < columns: #performs weighted average calculations
    high_action += matrix[0][value_index] * probabilities[value_index]
    value_index += 1

high_action_test: int = 0
row_index: int = 1

while row_index < rows: #identifies most efficacious action
    high_action_test = 0
    value_index = 0
    while value_index < columns:
        high_action_test += matrix[row_index][value_index] * probabilities[value_index]
        value_index += 1
    if high_action_test > high_action:
        high_action = high_action_test
        high_action_index = row_index
    row_index += 1

print(f"You should consider {actions[high_action_index]}.") #returns result
enter()