import random


def end_of_civilization_predictor():
    """
    Simulates the impact of various factors on the potential end of civilization.

    This function prompts the user to enter the number of years they want to simulate
    and then simulates the impact of factors such as climate change, overpopulation,
    probability of war, deadly pathogens, and technological catastrophes. It calculates
    the overall probability of civilization ending based on 5 random events and displays
    warnings if the probability is high.

    Returns: None
    """
    print("Welcome to the End of Civilizaton Predictor!!")

    # factors and probabilities
    factors = {
        "Climate Change": 0.3,
        "Overpopulation": 0.2,
        "Probability of War": 0.25,
        "Deadly Pathogens": 0.15,
        "Technological Catastrophe": 0.1,
    }

    total_probability = 0
    for prob in factors.values():
        total_probability += prob

    print("\nFactors and Their Probabilities:")
    for factor, probability in factors.items():
        print(f"{factor}: {probability * 100}%")

    print("\nTotal Probability:", total_probability)

    while 1:
        # take number of years from user
        years_to_simulate = int(input("\nEnter the number of years to simulate: "))

        # simulate impact of each factor
        print("\nSimulating the Impact of Factors over Time:")
        for year in range(1, years_to_simulate + 1):
            print(f"\nYear {year:}")
            for factor, probability in factors.items():
                impact = random.uniform(0, 1)
                if impact < probability:
                    print(f"{factor} has a significant impact on end of civilization.")

            # calculate overall probability of civiliztion ending
            overall_probability = 0
            
            for _ in range(5):
                overall_probability += random.uniform(0, 1)
            print(f"Overall Probability of Civilization Ending: {overall_probability}")

            # display a warning if overall probability is high
            if overall_probability / 5 > 0.5:
                print("\nWarning: The probability of civilization ending is high. Take necessary precautions.")
                break

        # Run again?
        run_again = input("\nDo you want to run the simulation again? (yes/no): ")
        if run_again.lower() != "yes":
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    end_of_civilization_predictor()