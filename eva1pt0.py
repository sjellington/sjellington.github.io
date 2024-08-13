"""Returns user's fair price of a share of stock."""

def enter() -> None:
    print("")

enter()
good_earnings_report: int = int(input("What is your estimate of a good earnings report for this stock?: ")) #initializes good earnings report
enter()
bad_earnings_report: int = int(input("What is your estimate of a bad earnings report for this stock?: ")) #initializes bad earnings report
enter()
confidence: int = int(input("On a scale of 1-100, what is your confidence in a good earnings report?: ")) #initializes confidence level

confidence /= 100 #converts confidence to decimal value

fair_price: int = good_earnings_report*confidence + bad_earnings_report*(1 - confidence) #performs weighted average calculations

enter()
print(f"The fair price to pay for this share is ${fair_price}.") #returns result
enter()
