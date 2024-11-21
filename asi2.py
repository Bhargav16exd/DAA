def scheduling(jobs):
    

    #Sort the Jobs according to the profit
    jobs = sorted(jobs,key=lambda x:x[2] , reverse=True)

    #Find Maximum Deadline 
    maxDeadline = max(jobs,key=lambda x:x[1])

    #Schedule 
    schedule = [-1] * maxDeadline[1]

    print(schedule)


    for job in jobs:
        id , deadline , profit = job

        for slot in range(deadline-1,-1,-1):
            if schedule[slot] == -1 :
                schedule[slot] = id 
                break
            
    print(schedule)


#Main 

n = input("Number of Jobs : ")
jobs = []

for i in range(int(n)):
    id       =  input(f"Enter ID for job {i+1} ")
    deadline = int(input(f"Enter Deadline for job {i+1} "))
    profit   = int(input(f"Enter Profit for job {i+1} "))
    jobs.append((id,deadline,profit))

scheduling(jobs)