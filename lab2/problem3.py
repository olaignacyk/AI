from strips_domain import STRIPS_domain
from planning_problem import Planning_problem

domain = STRIPS_domain()

locations = [f'L{i}' for i in range(1, 11)]
robot = 'R1'
containers = ['C1', 'C2']

# Dodaj operatory move
for i in range(len(locations) - 1):
    l1 = locations[i]
    l2 = locations[i + 1]
    domain.add_operator({
        'name': f'move({robot}, {l1}, {l2})',
        'precond': [f'at({robot}, {l1})'],
        'add': [f'at({robot}, {l2})'],
        'delete': [f'at({robot}, {l1})']
    })
    domain.add_operator({
        'name': f'move({robot}, {l2}, {l1})',
        'precond': [f'at({robot}, {l2})'],
        'add': [f'at({robot}, {l1})'],
        'delete': [f'at({robot}, {l2})']
    })

# Załadunek/rozładunek
for c in containers:
    for l in locations:
        domain.add_operator({
            'name': f'load({robot}, {c}, {l})',
            'precond': [f'at({robot}, {l})', f'at({c}, {l})', 'empty(R1)'],
            'add': [f'holding(R1, {c})'],
            'delete': [f'at({c}, {l})', 'empty(R1)']
        })
        domain.add_operator({
            'name': f'unload({robot}, {c}, {l})',
            'precond': [f'at({robot}, {l})', f'holding(R1, {c})'],
            'add': [f'at({c}, {l})', 'empty(R1)'],
            'delete': [f'holding(R1, {c})']
        })

# 🔹 Etap 1: załaduj C1 (znajduje się w L2)
initial1 = ['at(R1, L1)', 'at(C1, L2)', 'at(C2, L3)', 'empty(R1)']
goal1 = ['holding(R1, C1)']
problem1_3 = Planning_problem(initial1, goal1, domain)

# 🔹 Etap 2: przemieść C1 do L10
initial2 = ['at(R1, L2)', 'holding(R1, C1)', 'at(C2, L3)', 'empty(R1)']  # zakładamy sukces etapu 1
goal2 = ['at(C1, L10)']
problem2_3 = Planning_problem(initial2, goal2, domain)

# 🔹 Etap 3: dostarcz C2 do L9
initial3 = ['at(R1, L3)', 'at(C2, L3)', 'empty(R1)', 'at(C1, L10)']
goal3 = ['holding(R1, C2)', 'at(C2, L9)']
problem3_3 = Planning_problem(initial3, goal3, domain)



