from strips_domain import STRIPS_domain
from planning_problem import Planning_problem

domain = STRIPS_domain()

locations = [f'L{i}' for i in range(1, 11)]
robot = 'R1'
containers = ['C1', 'C2']

# Operatory move, load, unload
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

# Początek: robot i oba kontenery w L1
initial = [
    'at(R1, L1)', 'at(C1, L1)', 'at(C2, L1)', 'empty(R1)'
]

# Cel: C1 na L10, C2 na L9 (wymusza podróże w tę i z powrotem)
goal = ['at(C1, L10)', 'at(C2, L9)']

problem = Planning_problem(initial, goal, domain)
