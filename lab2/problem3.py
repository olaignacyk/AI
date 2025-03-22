from strips_domain import STRIPS_domain
from planning_problem import Planning_problem

domain = STRIPS_domain()
machines = [f'M{i}' for i in range(1, 6)]
tasks = [f'T{i}' for i in range(1, 11)]

for m in machines:
    for t in tasks:
        domain.add_operator({
            'name': f'perform({m}, {t})',
            'precond': [f'available({m})', f'pending({t})'],
            'add': [f'completed({t})'],
            'delete': [f'pending({t})']
        })

initial = [f'available({m})' for m in machines] + [f'pending({t})' for t in tasks]
goal = [f'completed({t})' for t in tasks]

problem = Planning_problem(initial, goal, domain)
