"""Returns probabilistic advantage of purchasing a lottery ticket."""

from math import comb

def enter() -> None:
    print("")

enter()
num: int = int(input("How many lottery numbers are selected?: "))
enter()
field: int = int(input("What is the range of possible numbers selected?: "))
enter()

possibles: list[float] = []
index: int = 0

while index <= num: #creates list of probabilities based on user input
    possibles.append((comb(num,index)*comb(field - num,num - index))/comb(field,num))
    index += 1

prizes: list[int] = []
index: int = 0

while index <= num: #creates list of prizes based on user input
    prizes.append(int(input(f"What is the prize for matching {index} out of {num} numbers?: ")))
    enter()
    index += 1

index = 0
expect: int = 0

while index <= num: #sums expected value of ticket
    expect += possibles[index]*prizes[index]
    index += 1

ticket_price: int = int(input("What is the price of a ticket?: "))
enter()

expected_return: int = int((expect - ticket_price)/ticket_price * 100) #calculates expected return
print(f"You can expect a(n) {expected_return}% return on your investment.")
enter()

if expect >= ticket_price: #tests expected value against price of ticket
    print("It is probabilistically advantageous to buy a ticket.")
else:
    print("It is probabilistically disadvantageous to buy a ticket.")
enter()