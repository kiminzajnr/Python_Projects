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


if __name__ == "__main__":
    end_of_civilization_predictor()