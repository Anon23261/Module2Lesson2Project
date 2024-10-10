# Task 1: Code Correction
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(f"Selected venue: {venue}")

# Task 2: Venue Selection
equipment = "projector" if attendees > 50 else "audio system"
print(f"Recommended equipment: {equipment}")

# Task 3: Catering Choices
vegetarian = input("Do you want vegetarian food? (yes or no): ").lower()
caterer = "Veggie Delight Caterers" if vegetarian == "yes" else "Gourmet Meals Caterers"
print(f"Recommended caterer: {caterer}")
