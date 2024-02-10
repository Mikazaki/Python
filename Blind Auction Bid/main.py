from replit import clear
from art import logo
print(logo)


dn = {}

fr = True
while fr is True:
  name = input("What is your name: ")
  bid = input("What is your bid: $")
  dn[name] = bid
  
  q = input("Are there any other bidders? type 'yes' or 'no'\n").lower()

  if q == 'no':
    fr = False
    highest_bid = 0
    highest_bidder = ""
    for name, bid in dn.items():
      value = int(bid)
      if value > highest_bid:
          highest_bid = value
          highest_bidder = name
    print(f"The highest bid was made by {highest_bidder}, with the amount of ${highest_bid}")

  else:
    clear()

  