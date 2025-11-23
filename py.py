class HelloWorldSender:
    def __init__(self, message="Hello World"):
        self.message = message
    
    def print_to_console(self):
        print(self.message)
if __name__ == "__main__":
    sender = HelloWorldSender()
    sender.print_to_console()
