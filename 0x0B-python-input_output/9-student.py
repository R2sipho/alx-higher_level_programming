#!/usr/bin/python3
"""Defines a class Student."""

class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_dict(self):
        """Get a dictionary representation of the Student."""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }

# Example usage:
if __name__ == "__main__":
    # Creating a Student object
    student1 = Student("John", "Doe", 20)

    # Getting the dictionary representation
    student_dict = student1.to_dict()

    # Printing the dictionary representation
    print(student_dict)

