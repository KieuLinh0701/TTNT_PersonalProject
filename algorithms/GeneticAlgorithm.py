import random

def geneticAlgorithm(startState, goalState):
    population_size = 50
    generations = 500
    mutation_rate = 0.1
    solution_steps = [startState]  # Lưu các trạng thái để xuất ra

    def fitness(state):
        # Hàm fitness: Số lượng ô đúng vị trí
        return sum(state[i][j] == goalState[i][j] for i in range(3) for j in range(3))

    def flatten(state):
        return [cell for row in state for cell in row]

    def unflatten(flat):
        return [flat[i:i+3] for i in range(0, len(flat), 3)]

    def is_solvable(state):
        # Kiểm tra trạng thái khả giải
        inversions = 0
        flat_state = [x for x in state if x != 0]
        for i in range(len(flat_state)):
            for j in range(i + 1, len(flat_state)):
                if flat_state[i] > flat_state[j]:
                    inversions += 1
        return inversions % 2 == 0

    def generate_population():
        # Tạo quần thể ban đầu
        population = []
        while len(population) < population_size:
            candidate = random.sample(flat_goal, len(flat_goal))
            if is_solvable(candidate):
                population.append(candidate)
        return population

    def crossover(parent1, parent2):
        # Order Crossover (OX)
        size = len(parent1)
        start, end = sorted(random.sample(range(size), 2))
        child = [None] * size
        child[start:end + 1] = parent1[start:end + 1]
        remaining = [item for item in parent2 if item not in child]
        pointer = 0
        for i in range(size):
            if child[i] is None:
                child[i] = remaining[pointer]
                pointer += 1
        return child

    def mutate(individual):
        # Đột biến: Hoán đổi hai ô ngẫu nhiên
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

    # Bắt đầu thuật toán
    flat_start = flatten(startState)
    flat_goal = flatten(goalState)

    if flat_start == flat_goal:
        return solution_steps

    population = generate_population()
    for generation in range(generations):
        # Tính fitness cho từng cá thể
        fitness_scores = [(individual, fitness(unflatten(individual))) for individual in population]
        fitness_scores.sort(key=lambda x: x[1], reverse=True)

        # Chọn lọc: Chọn 50% cá thể tốt nhất
        population = [individual for individual, score in fitness_scores[:population_size // 2]]

        # Tạo thế hệ mới
        next_generation = []
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                mutate(child)
            if child not in next_generation:  # Tránh trùng lặp
                next_generation.append(child)

        population = next_generation

        # Kiểm tra nếu tìm được lời giải
        for individual in population:
            if individual == flat_goal:
                solution_steps.append(unflatten(individual))  # Lưu trạng thái giải
                return solution_steps

        # Lưu trạng thái hiện tại tốt nhất của quần thể
        solution_steps.append(unflatten(population[0]))

    # Trả về danh sách các trạng thái đã duyệt
    return solution_steps