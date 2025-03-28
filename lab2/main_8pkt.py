from importlib import import_module
from forward_planner import forward_search
from astar_planner import astar_search
from heuristics import num_unsatisfied_goals
from problem1 import  problem1_1,problem2_1,problem3_1
from problem2 import problem1_2, problem2_2, problem3_2
from problem3 import problem1_3,problem2_3,problem3_3



def test(problem, label):
    from forward_planner import forward_search
    from astar_planner import astar_search
    from heuristics import num_unsatisfied_goals

    print(f"\n=== 🔍 {label} ===")
    
    print("\n▶️ Forward search:")
    plan, _ = forward_search(problem, timeout=300)
    if plan:
        for step in plan:
            print("  ", step)
    else:
        print("❌ No plan found.")

    print("\n⭐ A* search with heuristic:")
    plan, _ = astar_search(problem, heuristic_fn=num_unsatisfied_goals, timeout=300)
    if plan:
        for step in plan:
            print("  ", step)
    else:
        print("❌ No plan found.")
    


print(f"\n=== 🔍 Problem załadunku  ===")
test(problem1_3, "Etap 1: Załadunek C1")
test(problem2_3, "Etap 2: Transport C1 do L10")
test(problem3_3, "Etap 3: Transport C2 do L9")

print("=== 🔍 Problem z wieza===")
test(problem1_2, "Etap 1: Dolna część wieży (D-E-F)")
test(problem2_2, "Etap 2: Środek wieży (B-C-D)")
test(problem3_2, "Etap 3: Zwieńczenie (A-B)")


print(f"\n=== 🔍 Problem z robotem ===")
test(problem1_1, "Etap 1: robot idzie do L10")
test(problem2_1, "Etap 2: robot ładuje kontener")
test(problem3_1, "Etap 3: robot przewozi kontener na L50")