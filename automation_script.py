
def get_tasks():
    tasks = []
    print("لطفا وظایف خود را وارد کنید (برای پایان دادن، خط خالی بزنید):")
    while True:
        task = input("وظیفه: ")
        if task == "":
            break
        tasks.append(task)
    return tasks

def get_priorities(tasks):
    priorities = []
    print("\nلطفا اولویت هر وظیفه را وارد کنید (عدد کوچکتر = اولویت بالاتر):")
    for task in tasks:
        while True:
            try:
                p = int(input(f"اولویت '{task}': "))
                priorities.append((task, p))
                break
            except ValueError:
                print("لطفا یک عدد صحیح وارد کنید.")
    return priorities

def sort_tasks_alphabetically(tasks):
    return sorted(tasks)

def sort_tasks_by_priority(priorities):
    return [task for task, _ in sorted(priorities, key=lambda x: x[1])]

def save_tasks(sorted_tasks, output_file="sorted_tasks.txt"):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for i, task in enumerate(sorted_tasks, 1):
                file.write(f"{i}. {task}\n")
        print(f"وظایف مرتب‌شده در {output_file} ذخیره شدند.")
    except Exception as e:
        print(f"خطا در ذخیره فایل: {e}")

def main():
    tasks = get_tasks()
    if not tasks:
        print("لیست وظایف خالی است.")
        return

    while True:
        print("\nچگونه می‌خواهید وظایف را مرتب کنید؟")
        print("1. بر اساس حروف الفبا")
        print("2. بر اساس اولویت")
        choice = input("انتخاب شما (1 یا 2): ")
        if choice in ["1", "2"]:
            break
        print("انتخاب نامعتبر است. لطفاً 1 یا 2 را وارد کنید.")

    if choice == "1":
        sorted_tasks = sort_tasks_alphabetically(tasks)
    else:
        priorities = get_priorities(tasks)
        sorted_tasks = sort_tasks_by_priority(priorities)

    print("\nوظایف مرتب شده:")
    for i, task in enumerate(sorted_tasks, 1):
        print(f"{i}. {task}")

    save_tasks(sorted_tasks)

if __name__ == "__main__":
    main()
