class Controller:
    def __init__(self):
        self.bot_routs = ('$select', '$update', '$delete', '$insert', '$size')

    def check_routs(self, command):
        return False if command not in self.bot_routs else True
