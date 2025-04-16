# Initialize arrays to store admitted and not admitted candidates
admitted = []
not_admitted = []

def check_admission():
    # Get candidate details
    name = input("Enter candidate's name: ")
    jamb_score = int(input("Enter JAMB score: "))
    credits = int(input("Enter number of credits in 5 key subjects: "))
    interview_passed = input("Did the candidate pass the interview? (yes/no): ").lower()

    # Check criteria for Computer Science
    cs_admitted = (jamb_score >= 250) and (credits >= 5) and (interview_passed == "yes")

    # Check criteria for Mass Communication
    mass_comm_admitted = (jamb_score >= 230) and (credits >= 5) and (interview_passed == "yes")

    # Determine admission
    if cs_admitted:
        admitted.append({"name": name, "course": "Computer Science"})
        print(f"{name} has been admitted into Computer Science!")
    elif mass_comm_admitted:
        admitted.append({"name": name, "course": "Mass Communication"})
        print(f"{name} has been admitted into Mass Communication!")
    else:
        not_admitted.append({"name": name})
        print(f"{name} was not admitted.")

# Main program
while True:
    check_admission()
    more_candidates = input("Do you want to check another candidate? (yes/no): ").lower()
    if more_candidates != "yes":
        break

# Display results
print("\nAdmitted Candidates:")
for candidate in admitted:
    print(f"{candidate['name']} - {candidate['course']}")

print("\nNot Admitted Candidates:")
for candidate in not_admitted:
    print(candidate['name'])