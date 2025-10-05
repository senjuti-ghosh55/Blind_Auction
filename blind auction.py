import art

print(art.logo)



def highest_bidding(bid_dict):
    winner=""
    high=0
    for bidder in bid_dict:
          bid_amount=bid_dict[bidder]
          if bid_amount>high:
               high=bid_amount
               winner=bidder

    print(f"the winner is {winner} with a bid of {high}")


bid={}
continue_bidding=True
while continue_bidding:
     name=input("enter your name?")
     value=int(input("enter the amount of bidding:$"))
     bid[name]=value
     should_continue=input("are there any more bidder?yes or no\n").lower()
     if should_continue =='no':
         continue_bidding=False
         highest_bidding(bid)
     elif should_continue=='yes':
          print("\n"*20)






