#!/usr/bin/env python
from user import User

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # teacher starts with some knowledge
        self.knowledge = [
            "Python basics",
            "Object-oriented programming",
            "Data structures",
            "Inheritance",
            "Unit testing"
        ]

    def teach(self):
        # return a random piece of knowledge
        import random
        return random.choice(self.knowledge)
