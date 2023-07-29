

class Processor():
    def __init__(self):
        self.filters = list()
 
    def add(self, filter):
        self.filters.extend(filter)
 
    def execute(self, task):
        print("Executing pipeline...")
        for task_filter in self.filters:
            task_filter(task)
 
