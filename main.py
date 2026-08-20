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
    in_completed_task = [task for task in tasks if task['completed'] == False]
    if not in_completed_task:
        print('No Task To Mark It')
        return
    for i , task in enumerate(in_completed_task):
        print(f'{i+1}. {task['task']}')
        print('-' * 30)
    task_number = int(input('Enter Number Of Task To Complete'))
    in_completed_task[task_number-1]['completed'] = True
    print('Task Completed')

def view_tasks():
    if not tasks:
        print('No Tasks To View')
        return
    for i , task in enumerate(tasks):
        status = "✅" if task["completed"] else "❌"
        print(f'{i+1}. {task["task"]} {status}')
        print('-' * 20 )
if __name__ == '__main__':
    main()