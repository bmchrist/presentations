class ExampleClass:
    """A simple example class"""
    def __init__(self):
	self.data = 12345

    def f(self):
        return 'hello world'

    def get_value(self):
	return self.data

    def set_value(self, val):
	self.data = val
