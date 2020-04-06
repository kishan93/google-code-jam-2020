class Task():
    index=0
    start=0
    end=0
    worker=""
class Worker():
    name=""
    freeAt=0
    nextIndex=0


def assign(task):
    global workerIndex
    global tasks
    global w
    
    worker = w[workerIndex]
    worker.freeAt = task.end
    tasks[task.index].worker=worker.name
    workerIndex = worker.nextIndex
    

output=""
T = int(raw_input())
for t in range(T):
    
    #init workers
    w= [Worker(),Worker()]
    w[0].name = "C"
    w[0].nextIndex = 1
    w[1].name = "J"
    workerIndex = 0;

    #get tasks
    tasks=[]
    N = int(raw_input())
    for n in range(N):
        taskData = raw_input().split(" ")
        task = Task()
        task.index = n
        task.start = int(taskData[0])
        task.end = int(taskData[1])
        tasks.append(task)
    tasksSorted = sorted(tasks,key=lambda x: x.start)

    #proccess tasks
    flagImpossible = False;
    for task in tasksSorted:
        if task.start >= w[workerIndex].freeAt:
            # will do
            assign(task);
        elif task.start >= w[w[workerIndex].nextIndex].freeAt:
            # will do
            workerIndex = w[workerIndex].nextIndex
            assign(task);
        else:
            # can't do
            flagImpossible = True
            break
    output += "Case #"+str(t+1)+": "
    if flagImpossible:
        output +="IMPOSSIBLE"
    else:
        for task in tasks:
            output += task.worker
    output += "\n"

print(output)