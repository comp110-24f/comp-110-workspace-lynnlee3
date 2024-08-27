"""Tea party"""

__author__ = "730485520"


def main_planner(guests: int):
    """Print everything."""
    print(f"A Cozy Tea Party for {guests} People!")
    tea_count = tea_bags(guests)
    print(f"Tea Bags: {tea_count}")
    treat_count = treats(guests)
    print(f"Treats: {treat_count}")
    cost = costs(tea_count, treat_count)
    print(f"Cost: ${cost}")


def tea_bags(people: int) -> int:
    """Return total tea_bags."""
    return people * 2


def treats(people: int) -> int:
    """Return total treats."""
    return int(tea_bags(people) * 1.5)


def costs(tea_count: int, treat_count: int) -> float:
    """Return total cost."""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
