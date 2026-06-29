from art import logo
print(logo)
user_data= {}

is_more=True
while is_more:
    name = input("Enter your name:")
    bid = int(input("Enter your bid: $"))
    user_data[name]=bid

    others=input("Is there any other who wants to bid? (Yes/No): ").lower()
    if others=="no":
        # Find the highest bid and the name associated with it
        highest_value=max(user_data.values())
        top_key=max(user_data,key = user_data.get)
        print(f"The person with the highest Bidder is {top_key} with Bid ${highest_value}")
        is_more=False
    elif others=="yes":
        print("\n"*20)



