from strips_domain import STRIPS_domain
from planning_problem import Planning_problem

domain = STRIPS_domain()

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

initial = ['at(R1, L1)', 'at(C1, L10)', 'empty(R1)']
goal = ['at(C1, L50)']

problem = Planning_problem(initial, goal, domain)
