class STRIPS_domain:
    def __init__(self):
        self.operators = []

    def add_operator(self, operator):
        required_keys = {'name', 'precond', 'add', 'delete'}
        if not required_keys.issubset(operator.keys()):
            raise ValueError("Operator must have keys: name, precond, add, delete")
        self.operators.append(operator)

    def applicable_operators(self, state):
        return [op for op in self.operators if set(op['precond']).issubset(state)]

    def apply(self, state, operator):
        new_state = set(state)
        new_state.difference_update(operator['delete'])
        new_state.update(operator['add'])
        return new_state
