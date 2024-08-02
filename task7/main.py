import random
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def monte_carlo_simulation(num_simulations):
    results = {i: 0 for i in range(2, 13)}
    for _ in range(num_simulations):
        result = roll_dice()
        results[result] += 1
    return results

def calculate_probabilities(results, num_simulations):
    probabilities = {k: (v / num_simulations) * 100 for k, v in results.items()}
    return probabilities

def plot_probabilities(probabilities, theoretical_probabilities):
    sums = list(probabilities.keys())
    monte_carlo_probs = list(probabilities.values())
    theoretical_probs = [theoretical_probabilities[sum_] for sum_ in sums]
    
    plt.figure(figsize=(10, 6))
    plt.bar(sums, monte_carlo_probs, width=0.4, label='Monte Carlo', align='center')
    plt.bar([s + 0.4 for s in sums], theoretical_probs, width=0.4, label='Theoretical', align='center')
    
    plt.xlabel('Sum')
    plt.ylabel('%')
    plt.xticks(sums)
    plt.legend()
    plt.show()

theoretical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

num_simulations = 100000

results = monte_carlo_simulation(num_simulations)
probabilities = calculate_probabilities(results, num_simulations)

print("Monte-Carlo:")
for sum_, prob in probabilities.items():
    print(f"Sum1 {sum_}: {prob:.2f}%")

plot_probabilities(probabilities, theoretical_probabilities)