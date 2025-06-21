vote_yes = int(input("How many people voted YES: "))
voted_no = int(input("How many people voted NO: "))
voted_blank = int(input("Number of blank votes: "))

total_votes = vote_yes + voted_no + voted_blank

print(f"YES: {vote_yes * 100 / total_votes}%")
print(f"NO: {voted_no * 100 / total_votes}%")
print(f"Blank: {voted_blank * 100 / total_votes}%")