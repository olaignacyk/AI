from collections import deque
import time

def forward_search(problem, timeout=300):
    start_time = time.time()
    frontier = deque([(problem.initial, [])])
    explored = set()

    while frontier:
        if time.time() - start_time > timeout:
            return None, "⏱ Timeout"

        state, plan = frontier.popleft()
        state_key = frozenset(state)

        if problem.goal_test(state):
            print(f"🔢 Eksplorowano {len(explored)} unikalnych stanów")  
            return plan, f"{time.time() - start_time:.2f}s"

        if state_key in explored:
            continue
        explored.add(state_key)

        for op in problem.domain.applicable_operators(state):
            new_state = problem.domain.apply(state, op)
            new_plan = plan + [op['name']]
            frontier.append((new_state, new_plan))
    print(f"🔢 Eksplorowano {len(explored)} unikalnych stanów")


    return None, "❌ No solution found"
