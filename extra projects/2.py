import random

options = ("ჭა", "ფურცელი", "მაკრატელი")
running = True

while running:

    player = None
    player2 = random.choice(options)
    if player not in options:
         player = input("Enter a choice (ჭა,ფურცელი,მაკრატელი): ")
    print(f"Player: {player}")
    print(f"Computer: {player2}")

    if player == player2:
        print("თქვენ ხართ გამარჯვებულები!")
    elif player == "ჭა" and player2 == "მაკრატელი":
        print("თქვენ გაიმარჯვეთ!")
    elif player == "ფურცელი" and player2 == "ჭა":
        print("თქვენ გაიმარჯვეთ!")
    elif player == "მაკრატელი" and player2 == "ფურცელი":
        print("თქვენ გაიმარჯვეთ!")
    else:
        print("თქვენ სამწუხაროთ დამარცხდით!")

    if not input("Play again? (yes/no): ").lower() == "y":
        running = False

print("მადლობას გიხდით მონაწილეობის მიღებისთვის!")