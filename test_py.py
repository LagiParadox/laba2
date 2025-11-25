import unittest
import sys
import io
from py import HelloWorldSender

class TestHelloWorldSender(unittest.TestCase):
    
    def test_default_message(self):
        sender = HelloWorldSender()
        self.assertEqual(sender.message, "Hello World")
    
    def test_custom_message(self):
        sender = HelloWorldSender("Custom Message")
        self.assertEqual(sender.message, "Custom Message")
    
    def test_print_to_console(self):
        sender = HelloWorldSender("Test")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        sender.print_to_console()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Test")
    
    def test_send_count_increases(self):
        sender = HelloWorldSender()
        initial_count = sender.send_count
        sender.print_to_console()
        self.assertEqual(sender.send_count, initial_count + 1)
    
    def test_print_with_emojis_contains_message(self):
        sender = HelloWorldSender("Test")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        sender.print_with_emojis()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Test", output)
    def test_get_version(self):
        sender = HelloWorldSender()
        version_info = sender.get_version()
        self.assertIn("HelloWorldSender v", version_info)

    def test_print_info(self):
        sender = HelloWorldSender("Test")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        sender.print_info()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("HelloWorldSender", output)
        self.assertIn("Текущее сообщение: Test", output)
if __name__ == '__main__':
    unittest.main()