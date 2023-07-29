class Processor:
    def __init__(self):
        self.filters = list()
 
    def add(self, filter):
        self.filters.extend(filter)
 
    def execute(self, message):
        print("Executing pipeline...")
        for message_filter in self.filters:
            message_filter(message)
 
def double_data(message):
    message['data'] = [x*2 for x in message['data']]
 
def update_header(message):
    message['header'] = 'this is the updated message'
 
processor = Processor()
 
processor.add([double_data,
              update_header]) # note we are adding the function object, not making a function call
 
message = {'header': 'this is the original message',
           'data': [1,2,3]}
 
processor.execute(message)
for key, value in message.items():
    print(key + ' : ' + str(value))