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

# ✔️ Początkowy stan: wszystko luzem
initial = [f'on_table({b})' for b in blocks] + ['hand_empty'] + [f'clear({b})' for b in blocks]

# 🎯 Cel: wieża A–B–C–D–E–F
goal = [
    'on(A, B)', 'on(B, C)', 'on(C, D)', 'on(D, E)', 'on(E, F)'
]

problem = Planning_problem(initial, goal, domain)
