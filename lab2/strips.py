class Action:
    def __init__(self, name, preconditions, add_effects, del_effects):
        self.name = name
        self.preconditions = set(preconditions)
        self.add_effects = set(add_effects)
        self.del_effects = set(del_effects)

    def applicable(self, state):
        """Sprawdza, czy akcja może być wykonana w danym stanie."""
        return self.preconditions.issubset(state)

    def apply(self, state):
        if not self.applicable(state):
            return None
        new_state = set(state)  # zmiana: kopiujemy jako zwykły set
        new_state.difference_update(self.del_effects)
        new_state.update(self.add_effects)
        return new_state


    def __repr__(self):
        return self.name


class STRIPSProblem:
    def __init__(self, initial_state, goal, actions):
        self.initial_state = set(initial_state)
        self.goal = set(goal)
        self.actions = actions

    def goal_test(self, state):
        return self.goal.issubset(state)

