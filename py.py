import time
import random

class HelloWorldSender:
    def __init__(self, message="Hello World"):
        self.message = message
        self.send_count = 0
    
    def print_to_console(self):
        print(self.message)
        self.send_count += 1
    
    def print_rainbow(self):
        colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
        result = ""
        for i, char in enumerate(self.message):
            result += colors[i % len(colors)] + char
        print(result + '\033[0m')
        self.send_count += 1
    
    def print_animated(self):
        for char in self.message:
            print(char, end='', flush=True)
            time.sleep(0.1)
        print()
        self.send_count += 1
    
    def print_with_emojis(self):
        emojis = ["🌟", "🚀", "🎉", "🔥", "💫"]
        print(f"{random.choice(emojis)} {self.message} {random.choice(emojis)}")
        self.send_count += 1
    
    def surprise_mode(self):
        modes = [self.print_rainbow, self.print_animated, self.print_with_emojis]
        random.choice(modes)()

if __name__ == "__main__":
    sender = HelloWorldSender()
    
    sender.print_to_console()
    sender.print_rainbow()
    sender.print_animated()
    sender.print_with_emojis()
    
    print("\nСюрприз!")
    sender.surprise_mode()