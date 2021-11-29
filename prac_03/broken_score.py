"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """Get score and return category."""
    score = float(input("Enter score: "))
    print(categorize_score(score))
    random_score = random.uniform(1, 10)
    print(f"Randomize score: {random_score:.2f}.\nResult: {categorize_score(random_score)}")


def categorize_score(score):
    """Categorize score and return result."""
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == '__main__':
    main()
