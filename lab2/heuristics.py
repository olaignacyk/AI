def num_unsatisfied_goals(state, goal):
    return len([g for g in goal if g not in state])
