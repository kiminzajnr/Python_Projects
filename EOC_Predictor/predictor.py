import random


def end_of_civilization_predictor():
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
        years_to_simulate = int(input("\nEnter the number of years to simulate: "))

        print("\nSimulating the Impact of Factors over Time:")
        for year in range(1, years_to_simulate + 1):
            print(f"\nYear {year:}")
            for factor, probability in factors.items():
                impact = random.uniform(0, 1)
                if impact < probability:
                    print(f"{factor} has a significant impact on end of civilization.")

            overall_probability = 0
            
            for _ in range(5):
                overall_probability += random.uniform(0, 1)
            print(f"Overall Probability of Civilization Ending: {overall_probability}")

            if overall_probability / 5 > 0.5:
                print("\nWarning: The probability of civilization ending is high. Take necessary precautions.")
                break

if __name__ == "__main__":
    end_of_civilization_predictor()