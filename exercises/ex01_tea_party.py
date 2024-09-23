"""My name is Sachil Singh and this program will calculate the cost of a tea party"""

__author__: str = "730771296"


def main_planner(guests: int) -> None:
    """brings all of the functions together"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print(
        "Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests)))
    )  # of guests = people


def tea_bags(people: int) -> int:
    """people is the number of guests attending the tea party."""
    return people * 2  # 1 guest = 2 teas


def treats(people: int) -> int:
    """Defines function that computes the treats needed based on teas needed"""
    return int(tea_bags(people=people) * 1.5)  # 2 people = 3 treats


def cost(tea_count: int, treat_count: int) -> float:
    """computes the cost of the tea bags and the treats combined"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
