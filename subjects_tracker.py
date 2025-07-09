class Lessons:
    def __init__(self, name):
        self.name = name
        self.complete = False

class Unit:
    def __init__(self, name):
        self.name = name
        self.lessons = []

class Subject:
    def __init__(self, name):
        self.name = name
        self.units = []

class Action:
    def __init__(self, action_type, data):
        self.action_type = action_type
        self.data = data

class StudentLearnerTracker:
    def __init__(self):
        self.subjects = []
        self.undo_stack = []
        self.redo_stack = []

    def add_subject(self, subject_name):
        self.subjects.append(Subject(subject_name))
        self.undo_stack.append(Action("add_subject", subject_name))
        self.redo_stack.clear()

    def add_unit(self, subject_name, unit_name):
        for subject in self.subjects:
            if subject.name == subject_name:
                subject.units.append(Unit(unit_name))
                self.undo_stack.append(Action("add_unit", (subject_name, unit_name)))
                self.redo_stack.clear()

    def add_lesson(self, subject_name, unit_name, lesson_name):
        for subject in self.subjects:
            if subject.name == subject_name:
                for unit in subject.units:
                    if unit.name == unit_name:
                        unit.lessons.append(Lessons(lesson_name))
                        self.undo_stack.append(Action("add_lesson", (subject_name, unit_name, lesson_name)))
                        self.redo_stack.clear()
                        return
        print(f"Error: Could not find subject '{subject_name}' or unit '{unit_name}'.")

    def display(self):
        for subject in self.subjects:
            print(f"Subject: {subject.name}")
            for unit in subject.units:
                print(f"  Unit: {unit.name}")
                for lesson in unit.lessons:
                    status = "Done" if lesson.complete else "Not Done"
                    print(f"    Lesson: {lesson.name} - {status}")

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        action = self.undo_stack.pop()
        self.redo_stack.append(action)
        
        if action.action_type == "add_lesson":
            subject_name, unit_name, lesson_name = action.data
            for subject in self.subjects:
                if subject.name == subject_name:
                    for unit in subject.units:
                        if unit.name == unit_name:
                            unit.lessons = [lesson for lesson in unit.lessons if lesson.name != lesson_name]
                            return
        elif action.action_type == "add_unit":
            subject_name, unit_name = action.data
            for subject in self.subjects:
                if subject.name == subject_name:
                    subject.units = [unit for unit in subject.units if unit.name != unit_name]
                    return
        elif action.action_type == "add_subject":
            subject_name = action.data
            self.subjects = [subject for subject in self.subjects if subject.name != subject_name]

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        action = self.redo_stack.pop()
        self.undo_stack.append(action)
        
        if action.action_type == "add_lesson":
            subject_name, unit_name, lesson_name = action.data
            self.add_lesson(subject_name, unit_name, lesson_name)
        elif action.action_type == "add_unit":
            subject_name, unit_name = action.data
            self.add_unit(subject_name, unit_name)
        elif action.action_type == "add_subject":
            subject_name = action.data
            self.add_subject(subject_name)

if __name__ == "__main__":
    tracker = StudentLearnerTracker()
    tracker.add_subject("Math")
    tracker.add_unit("Math", "Algebra")
    tracker.add_lesson("Math", "Algebra", "Linear Equations")
    tracker.add_lesson("Math", "Algebra", "Quadratic Equations")
    print("Initial state:")
    tracker.display()
    print("\nUndoing last action:")
    tracker.undo()
    tracker.display()
    print("\nRedoing last action:")
    tracker.redo()
    tracker.display()