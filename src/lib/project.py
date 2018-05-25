from process import Process

class Project:

    def __init__(self, options):
        self.options = options
        self.process = Process()

    def date(self):
        return self._get_date()

    def _get_date(self):
        return self.process.execute("date").rstrip('\n')

    def print_example_arg(self):
        return self.options.known.example
