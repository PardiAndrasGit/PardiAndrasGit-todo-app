import sys

def complete_task(n):
    try:
        with open("tasks.txt", "r") as f:
            f = f.readlines()
            lines=[]
            if len(f) >= n-1:
                for i in range(len(f)):
                    if i == n-1:
                        line = "[X]" + f[i][3:]
                        lines.append(line)
                    else:
                        lines.append(f[i])
            else:
                print("Unable to check: index is out of bound")

        with open("tasks.txt", "w") as nf:
            nf.writelines(lines)
    except IOError:
        print("Unable to write file: ", f)



def delete(n):
    try:
        with open("tasks.txt", "r") as f:
            f = f.readlines()
            lines=[]
            if len(f) >=n-1:
                for i in range(len(f)):
                    if i != n-1:
                        lines.append(f[i])
            else:
                print("Unable to remove: index is out of bound")
        with open("tasks.txt", "w") as nf:
            nf.writelines(lines)
    except IOError:
        print("Unable to write file: ", f)


start_message =   """Command Line Todo application\n =============================\n
Command line arguments:\n    -l   Lists all the tasks
    -a   Adds a new task\n    -r   Removes a task\n    -c   Completes a task"""


argument= ["-l", "-a" , "-r", "-c"]

if len(sys.argv) == 1:
    print(start_message)

elif len(sys.argv) > 1 and sys.argv[1] not in argument:
    print("Unsupported argument")
    print(start_message)

elif len(sys.argv) == 2 and sys.argv[1] == argument[0]:
    with open("tasks.txt", "r") as f:
        f = f.readlines()
        if len(f) == 0:
            print("No todos for today! :)")
        else:
            for i, line in enumerate(f):
                print(str(i + 1) + " - " + line, end="")


elif len(sys.argv) == 3 and sys.argv[1] == argument[1]:
    with open("tasks.txt", "r") as f:
        f = f.readlines()
        lines = []
        if len(f) > 0:
            for line in f:
                lines.append(line)
        new_line = "[ ] " + sys.argv[2] + "\n"
        lines.append(new_line)
    with open("tasks.txt", "w") as nf:
        nf.writelines(lines)

elif len(sys.argv) == 3 and sys.argv[1] == argument[3]:
    if sys.argv[2].isnumeric():
        complete_task(int(sys.argv[2]))
    else:
        print("Unable to remove: index is not a number")

elif len(sys.argv) == 3 and sys.argv[1] == argument[2]:
    if sys.argv[2].isnumeric():
        delete(int(sys.argv[2]))
    else:
        print("Unable to remove: index is not a number")



