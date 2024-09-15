from simpleai.search import SearchProblem, astar, hill_climbing, simulated_annealing, genetic, beam, greedy
import random

# Define the N-Queens problem class
class NQueensProblem(SearchProblem):
    def __init__(self, N):
        self.N = N
        super(NQueensProblem, self).__init__(initial_state=tuple([-1] * N))  # Start with an empty board

    def actions(self, state):
        column = state.index(-1) if -1 in state else self.N  # find the first empty column
        if column == self.N:
            return []  # No more actions if the state is fully populated
        return [row for row in range(self.N) if row not in state[:column]]  # Avoid rows already used

    def result(self, state, action):
        column = state.index(-1)
        new_state = list(state)
        new_state[column] = action
        return tuple(new_state)

    def is_goal(self, state):
        return state.count(-1) == 0 and self._no_conflicts(state)

    def _no_conflicts(self, state):
        # Check if queens don't conflict
        for col1 in range(len(state)):
            for col2 in range(col1 + 1, len(state)):
                row1, row2 = state[col1], state[col2]
                if row1 == row2 or abs(row1 - row2) == abs(col1 - col2):  # Same row or diagonal
                    return False
        return True

    def heuristic(self, state):
        # Heuristic: Number of conflicting pairs of queens
        conflicts = 0
        for col1 in range(len(state)):
            for col2 in range(col1 + 1, len(state)):
                row1, row2 = state[col1], state[col2]
                if row1 == row2 or abs(row1 - row2) == abs(col1 - col2):  # Same row or diagonal
                    conflicts += 1
        return conflicts

    def value(self, state):
        # For genetic algorithm: The fewer conflicts, the better (maximizing fitness)
        return -self.heuristic(state)

    def generate_random_state(self):
        # Generate a random state for the genetic algorithm
        state = list(range(self.N))
        random.shuffle(state)
        return tuple(state)

    def crossover(self, state1, state2):
        # Implement crossover: Combine two parent states to create a new child state
        cut = random.randint(1, self.N - 2)  # Random crossover point
        child = state1[:cut] + state2[cut:]  # Combine two parents
        return child

    def mutate(self, state):
        # Implement mutation: Randomly swap two queens in the state
        state = list(state)
        index1, index2 = random.sample(range(self.N), 2)
        state[index1], state[index2] = state[index2], state[index1]
        return tuple(state)

# Define the number of queens
N = 8

# Create an instance of the problem
problem = NQueensProblem(N)

# Running A* Search
print("\nRunning A* Search:")
astar_result = astar(problem)
for action, state in astar_result.path():
    print(f"State:\n{state}")

# Running Best-First Search (Greedy Search)
print("\nRunning Best-First Search (Greedy Search):")
greedy_result = greedy(problem)
for action, state in greedy_result.path():
    print(f"State:\n{state}")

# Running Hill-Climbing
print("\nRunning Hill-Climbing:")
hill_climbing_result = hill_climbing(problem)
for action, state in hill_climbing_result.path():
    print(f"State:\n{state}")

# Running Simulated Annealing
print("\nRunning Simulated Annealing:")
sa_result = simulated_annealing(problem)
for action, state in sa_result.path():
    print(f"State:\n{state}")

# Running Genetic Algorithm
print("\nRunning Genetic Algorithm:")
genetic_result = genetic(problem, population_size=100, mutation_chance=0.1)
print(f"State:\n{genetic_result.state}")

# Running Beam Search
print("\nRunning Beam Search:")
beam_result = beam(problem, beam_size=5)
for action, state in beam_result.path():
    print(f"State:\n{state}")