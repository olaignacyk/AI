from strips_domain import STRIPS_domain
from planning_problem import Planning_problem

domain = STRIPS_domain()
blocks = ['A', 'B', 'C', 'D', 'E', 'F']

# Operatory
for b in blocks:
    domain.add_operator({
        'name': f'pick_up({b})',
        'precond': [f'clear({b})', 'hand_empty', f'on_table({b})'],
        'add': [f'holding({b})'],
        'delete': [f'on_table({b})', 'hand_empty']
    })
    domain.add_operator({
        'name': f'put_down({b})',
        'precond': [f'holding({b})'],
        'add': [f'on_table({b})', 'hand_empty'],
        'delete': [f'holding({b})']
    })
    for c in blocks:
        if b != c:
            domain.add_operator({
                'name': f'stack({b}, {c})',
                'precond': [f'holding({b})', f'clear({c})'],
                'add': [f'on({b}, {c})', 'hand_empty'],
                'delete': [f'holding({b})', f'clear({c})']
            })
            domain.add_operator({
                'name': f'unstack({b}, {c})',
                'precond': [f'on({b}, {c})', f'clear({b})', 'hand_empty'],
                'add': [f'holding({b})', f'clear({c})'],
                'delete': [f'on({b}, {c})', 'hand_empty', f'clear({b})']
            })

# Stan początkowy: wszystko luzem
initial = [f'on_table({b})' for b in blocks] + ['hand_empty'] + [f'clear({b})' for b in blocks]

# Etap 1: dolna część
goal1 = ['on(E, F)', 'on(D, E)']
problem1_2 = Planning_problem(initial, goal1, domain)

# Etap 2: środkowa część
initial2 = initial + goal1  # zakładamy, że cel 1 już osiągnięty
goal2 = ['on(C, D)', 'on(B, C)']
problem2_2 = Planning_problem(initial2, goal2, domain)

# Etap 3: górna część
initial3 = initial2 + goal2
goal3 = ['on(A, B)']
problem3_2 = Planning_problem(initial3, goal3, domain)


