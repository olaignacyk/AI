import heapq
import time

def astar_search(problem, heuristic_fn, timeout=300):
    start_time = time.time()
    frontier = []
    heapq.heappush(frontier, (heuristic_fn(problem.initial, problem.goal), 0, problem.initial, []))
    explored = set()

    while frontier:
        if time.time() - start_time > timeout:
            return None, "⏱ Timeout"

        f, cost, state, plan = heapq.heappop(frontier)
        state_key = frozenset(state)

        if problem.goal_test(state):
            return plan, f"{time.time() - start_time:.2f}s"

        if state_key in explored:
            continue
        explored.add(state_key)

        for op in problem.domain.applicable_operators(state):
            new_state = problem.domain.apply(state, op)
            new_cost = cost + 1
            new_plan = plan + [op['name']]
            h = heuristic_fn(new_state, problem.goal)
            heapq.heappush(frontier, (new_cost + h, new_cost, new_state, new_plan))

    return None, "❌ No solution found"
