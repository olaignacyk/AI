from strips_domain import STRIPS_domain
from planning_problem import Planning_problem

domain = STRIPS_domain()

from strips_domain import STRIPS_domain
from planning_problem import Planning_problem
from forward_planner import forward_search
from astar_planner import  astar_search
from heuristics import num_unsatisfied_goals

domain = STRIPS_domain()

# Operatory ruchu
for i in range(1, 50):
    domain.add_operator({
        'name': f'move(R1, L{i}, L{i+1})',
        'precond': [f'at(R1, L{i})'],
        'add': [f'at(R1, L{i+1})'],
        'delete': [f'at(R1, L{i})']
    })
    domain.add_operator({
        'name': f'move(R1, L{i+1}, L{i})',
        'precond': [f'at(R1, L{i+1})'],
        'add': [f'at(R1, L{i})'],
        'delete': [f'at(R1, L{i+1})']
    })

# Operatory załadunku/rozładunku
for i in range(1, 51):
    domain.add_operator({
        'name': f'load(R1, C1, L{i})',
        'precond': [f'at(R1, L{i})', f'at(C1, L{i})', 'empty(R1)'],
        'add': [f'holding(R1, C1)'],
        'delete': [f'at(C1, L{i})', 'empty(R1)']
    })
    domain.add_operator({
        'name': f'unload(R1, C1, L{i})',
        'precond': [f'at(R1, L{i})', f'holding(R1, C1)'],
        'add': [f'at(C1, L{i})', 'empty(R1)'],
        'delete': [f'holding(R1, C1)']
    })

# 🔹 Etap 1: robot idzie do L10
initial1 = ['at(R1, L1)', 'at(C1, L10)', 'empty(R1)']
goal1 = ['at(R1, L10)']
problem1_1 = Planning_problem(initial1, goal1, domain)

# 🔹 Etap 2: robot ładuje kontener
initial2 = ['at(R1, L10)', 'at(C1, L10)', 'empty(R1)']
goal2 = ['holding(R1, C1)']
problem2_1 = Planning_problem(initial2, goal2, domain)

# 🔹 Etap 3: robot przewozi kontener na L50
initial3 = ['at(R1, L10)', 'holding(R1, C1)']
goal3 = ['at(C1, L50)']
problem3_1 = Planning_problem(initial3, goal3, domain)




