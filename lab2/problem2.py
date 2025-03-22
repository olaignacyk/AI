from strips_domain import STRIPS_domain
from planning_problem import Planning_problem

domain = STRIPS_domain()
blocks = [chr(i) for i in range(65, 75)]  # A-J

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

initial = [f'on_table({b})' for b in blocks] + ['hand_empty'] + [f'clear({b})' for b in blocks]
goal = [f'on({blocks[i]}, {blocks[i+1]})' for i in range(len(blocks) - 1)]

problem = Planning_problem(initial, goal, domain)
