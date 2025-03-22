from importlib import import_module
from forward_planner import forward_search
from astar_planner import astar_search
from heuristics import num_unsatisfied_goals
# 'problem1','problem2'
problem_modules = [  'problem2']

for idx, mod_name in enumerate(problem_modules, 1):
    print(f"\n=== 🔍 Problem {idx} ===")

    problem_module = import_module(mod_name)
    problem = problem_module.problem

    print("\n▶️ Forward search:")
    plan, time_info = forward_search(problem, timeout=300)
    if plan:
        print(f"✅ Plan found ({len(plan)} actions):")
        for step in plan:
            print("  ", step)
    else:
        print("❌ No plan found.")
    print("⏱ Time:", time_info)

    print("\n⭐ A* search with heuristic:")
    plan, time_info = astar_search(problem, heuristic_fn=num_unsatisfied_goals, timeout=300)
    if plan:
        print(f"✅ Plan found ({len(plan)} actions):")
        for step in plan:
            print("  ", step)
    else:
        print("❌ No plan found.")
    print("⏱ Time:", time_info)
