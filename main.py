"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    cost =annual_cost / SEMESTERS_PER_YEAR
    return cost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    cost = annual_cost / MONTHS_PER_YEAR
    return cost


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    cost = annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)
    return cost


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    cost = (annual_cost / 2) / credits
    return cost


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    cost = annual_cost / 2 / credits * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER
    return cost

def cost_per_week(annual_cost):
    """Give back what one week costs."""
    cost = annual_cost / (SEMESTERS_PER_YEAR * (CLASS_DAYS_PER_SEMESTER / 5))
    return cost


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    annual_cost = float(input("Enter the total cost for one year: "))
    # Then ask for the credits this semester.
    credits = int(input("Enter the number of credits this semester: "))

    while True:
        # Show your menu here.
        print("Cost Of College")
        print("1. Per Semester")
        print("2. Per Month")
        print("3. Per Day")
        print("4. Per Credit")
        print("5. Per CS1430 Class")
        print("6. Per Week")
        print("Q. Quit")

        choice = input("Choose an option: ")

        if choice == "Q":
            break
        elif choice == "1":
            cost = cost_per_semester(annual_cost)
            print(f"Cost per semester: ${cost:.2f}")
        elif choice == "2":
            cost = cost_per_month(annual_cost)
            print(f"Cost per month: ${cost:.2f}")
        elif choice == "3":
            cost = cost_per_day(annual_cost)
            print(f"Cost per day: ${cost:.2f}")
        elif choice == "4":
            cost = cost_per_credit(annual_cost, credits)
            print(f"Cost per credit: ${cost:.2f}")
        elif choice == "5":
            cost = cost_per_class(annual_cost, credits)
            print(f"Cost per CS1430 class: ${cost:.2f}")
        elif choice == "6":
            cost = cost_per_week(annual_cost)
            print(f"Cost per week: ${cost:.2f}")
        else:
            print("Invalid choice. Please try again.")
            

        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
