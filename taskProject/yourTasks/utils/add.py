def sort_tasks(tasks):
    for iter_num in range(len(tasks)-1, 0, -1):
        
        for idx in range(iter_num):
            
            if tasks[idx+1]['priority'] < tasks[idx]['priority']:
            
                temp = tasks[idx+1]
                tasks[idx+1] = tasks[idx]
                tasks[idx] = temp
    return tasks


def add_tasks(tasks, task, priority):

    plst = []
    for t in tasks:
        
        plst.append(t['priority']) 

    plst.sort()
    

    if priority not in plst:
        tasks.append({'task':task, 'priority': priority})

    else:
        tasks.append({'task':task, 'priority': (plst[-1]+1) })
    
    return tasks