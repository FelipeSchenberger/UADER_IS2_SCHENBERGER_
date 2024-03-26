import matplotlib.pyplot as plt

def collatz_sequence(n):
    iterations = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iterations += 1
    return iterations

def main():
    start_numbers = []
    iteration_counts = []

    for num in range(1, 10001):
        iterations = collatz_sequence(num)
        start_numbers.append(num)
        iteration_counts.append(iterations)

    plt.scatter(iteration_counts, start_numbers, marker='.')
    plt.title('Conjetura de Collatz')
    plt.xlabel('Número de Iteraciones')
    plt.ylabel('Número Inicial de la Secuencia')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
