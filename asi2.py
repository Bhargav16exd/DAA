def scheduling(jobs):

      jobs = sorted(jobs,key=lambda x:x[2],reverse=True)

      maxDeadline = max(jobs,key=lambda x:x[1])

      schedule = [-1] * maxDeadline[1]

      print(schedule)
      print(jobs)

      for job in jobs:
        id , deadline ,profit = job

        for slot in range(deadline-1 , -1 , -1):
            print(slot)
            print(deadline)
            if schedule[slot] == -1 :
                schedule[slot] = id 
                break
 
    

      print(schedule)




numberOfJobs = input("Enter Number of Jobs : ")
jobs = []
for i in range(int(numberOfJobs)):
    id = input(f"Enter ID for {i+1} : ")
    deadline = int(input(f"Enter Deadline for {i+1} : "))
    profit   = int(input(f"Enter profit for {i+1} : "))
    jobs.append((id,deadline,profit))

result = scheduling(jobs)
