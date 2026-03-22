from tasks.models import Priority, Category, Task, Note, Subtask
from faker import Faker
from django.utils import timezone

fake = Faker()

def run():
    priority_names = ["High", "Medium", "Low", "Critical", "Optional"]
    for name in priority_names:
        Priority.objects.get_or_create(name=name)
    print("Priorities created.")

    category_names = ["Work", "School", "Personal", "Finance", "Projects"]
    for name in category_names:
        Category.objects.get_or_create(name=name)
    print("Categories created")

    priorities = list(Priority.objects.all())
    categories = list(Category.objects.all())

    for _ in range(10):
        task = Task.objects.create(
            title=fake.sentence(nb_words=5),
            description=fake.paragraph(nb_sentences=3),
            deadline=timezone.make_aware(fake.date_time_this_month()),
            status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
            priority=fake.random_element(elements=priorities),
            category=fake.random_element(elements=categories),
        )

    for _ in range(2):
            Note.objects.create(
                task=task,
                content=fake.paragraph(nb_sentences=3),
            )

    for _ in range(3):
            Subtask.objects.create(
                parent_task=task,
                title=fake.sentence(nb_words=5),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
            )

    print("10 Tasks created")
    print("20 Notes created")
    print("30 SubTasks created")
    print("Database seeded successfully!")