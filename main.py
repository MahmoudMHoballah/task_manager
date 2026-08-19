tasks = []
def main():
    while True:
        message = '''
Welcome To Task Manager
1. Add Task To Complete
2. Mark Task As Completed
3. View Tasks
4. Quit'''
        print(message)
        user_input = input('Enter A choice ')
        if user_input == '1':
            add_task()
        elif user_input == '2':
            mark_task_as_completed()
        elif user_input == '3':
            view_tasks()
        elif user_input == '4':
            break
        else:
            print('Enter Number Between 1 To 4 ')

def add_task():
    task_input = input('Enter A Task ')
    task_info = {
'task' : task_input,
'completed' : False 
        }
    tasks.append(task_info)
    print('Tasks Added Successfully ')


def mark_task_as_completed():
    r
def view_tasks():
    pass
if __name__ == '__main__':
    main()