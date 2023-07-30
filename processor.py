class Processor():
    def __init__(self):
        self.filters = list()
 
    def add(self, filter):
        self.filters.extend(filter)
 
    def execute(self, task):
        print("Executing pipeline...")
        for task_filter in self.filters:
            print("Executing step "+ task_filter.__name__ + " ...")
            task_filter(task)
            print(" Done!")
 
def double_data(task):
    task['data'] = [x*2 for x in task['data']]
 
def update_header(task):
    task['header'] = 'this is the updated message'
 
simple_processor = Processor()
 
simple_processor.add([double_data,
              update_header]) # note we are adding the function object, not making a function call
 
task = {'header': 'this is the original message',
           'data': [1,2,3]}
 
simple_processor.execute(task)

for key, value in task.items():
    print(key + ' : ' + str(value))