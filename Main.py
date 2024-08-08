class Task:
    def __init__(self, prio=None, desc=None, zi=None, luna=None, an=None):#aici declaram fieldurile la self este necesar sa facem asta pt clean code
        #dar ea este apelata automat
        self.prio = prio
        self.desc = desc
        self.zi = zi
        self.luna = luna
        self.an = an

    def __str__(self):
        return f"{self.desc}  due date:{self.zi}/{self.luna}/{self.an}"

    def add(self):#o simpla motoda pt a seta valori noi pt o variabila cu aceasta clasa
        
        while 1:
            self.prio = input("prioritate task (1-10): ")
            try:
                self.prio =int(self.prio)

                if 1<=self.prio<=10:
                    break
                else:
                    print("enter a valid number: ")
            except ValueError:
                print("enter a valid number: ")


        self.desc = input("descriere task: ")


        while 1:
            self.zi = input("day due: ")
            try:
                self.zi =int(self.zi)

                if 1<=self.zi<=31:
                    break
                else:
                    print("enter a valid day: ")
            except ValueError:
                print("enter a valid day: ")


        while 1:
            self.luna = input("month due: ")
            try:
                self.luna =int(self.luna)

                if 1<=self.luna<=12:
                    break
                else:
                    print("enter a valid month: ")
            except ValueError:
                print("enter a valid month: ")


        while 1:
            self.an = input("year due(>=2024): ")
            try:
                self.an =int(self.an)

                if 2024<=self.an:
                    break
                else:
                    print("enter a valid year: ")
            except ValueError:
                print("enter a valid year: ")

class TaskManager:
    def __init__(self):
        self.toate_task = []

    def add_task(self):

        with open("logs.txt","a") as f:
            task_nou = Task()#dummy data
            task_nou.add()#setam valori task nou
            f.write(f"{task_nou.prio}*{task_nou.desc}*{task_nou.zi}/{task_nou.luna}/{task_nou.an}\n")
            self.toate_task.append(task_nou)

    def view_task(self):
        if not self.toate_task:#lista goala
            print("no tasks to be done")
            return 

        print("Current tasks are: ")
        i = 1
        for task_index in self.toate_task:
            print(f"{i} {task_index}")
            i=i+1
    
    def delete_task(self, index):
        del self.toate_task[index-1]

    def sort_by_prio(self):
        self.toate_task.sort(key = lambda task:task.prio,reverse=True)
    
    def Mainrun(self):
        f = open("logs.txt", "r")
        for x in f:
            task_nou = Task()
            prio_nou ,desc_nou, date_nou = x.split("*")
            day,month,year =date_nou.split("/")
            task_nou.prio = int(prio_nou)
            task_nou.zi = int(day)
            task_nou.luna =int(month)
            task_nou.an =int(year)
            task_nou.desc = desc_nou
            self.toate_task.append(task_nou)
        self.sort_by_prio()
        f.close()


        running =1
        while running:
            ccmd = input("Give command: ")
            if ccmd == "exit":
                running  = 0
            elif ccmd =="add":
                self.add_task()
            elif ccmd == "view":
                self.sort_by_prio()
                self.view_task()
            elif ccmd[0:6] == "delete":
                try:
                    numberlist = int(ccmd[6:])#aici luam numarul
                    self.delete_task(numberlist)
                    f = open("logs.txt","w")
                    for x in self.toate_task:
                        f.write(f"{x.prio}*{x.desc}*{x.zi}/{x.luna}/{x.an}\n")
                    f.close()
                except ValueError:
                    print("invalid task position given")

task_manager = TaskManager()
task_manager.Mainrun()

        

