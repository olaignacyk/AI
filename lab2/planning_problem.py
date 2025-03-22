class Planning_problem:
    def __init__(self, initial, goal, domain):
        self.initial = set(initial)
        self.goal = set(goal)
        self.domain = domain

    def goal_test(self, state):
        return self.goal.issubset(state)
