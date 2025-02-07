# taskmaster.py

class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def __str__(self):
        """Return a string representation of the task."""
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.title}, Status: {status}"


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        """Add a task to the project."""
        if isinstance(task, Task):
            self.tasks.append(task)

    def remove_task(self, task_title):
        """Remove a task from the project by its title."""
        self.tasks = [task for task in self.tasks if task.title != task_title]

    def list_tasks(self):
        """List all tasks in the project."""
        return [str(task) for task in self.tasks]

    def __str__(self):
        """Return a string representation of the project."""
        return f"Project: {self.name}, Total Tasks: {len(self.tasks)}"


# Example usage
if __name__ == "__main__":
    # Create a new project
    project = Project("Home Renovation")

    # Add tasks to the project
    project.add_task(Task("Paint the walls", "Paint all the walls in the living room"))
    project.add_task(Task("Install new lights", "Install ceiling lights in all rooms"))
    project.add_task(Task("Buy furniture", "Purchase furniture for the living room"))

    # Mark a task as completed
    project.tasks[0].mark_completed()

    # List all tasks
    print(project.list_tasks())
