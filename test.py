
def determine_grades(score):
    if score >= 80:
        return "jeles"
    elif score >= 70:
        return "jo"
    elif score >= 60:
        return "kozepes"
    elif score >= 50:
        return "eleseges"
    else:
        return "elegtelen"


if __name__ == "__main__":
    scores = []
    while True:
        user_input = input("Your score: ")

        if user_input == "q":
            break

        scores.append(int(user_input))
        print(scores)

    for score in scores:
        grade = determine_grades(score)
        print(grade)
