class Todo:
    def __init__(self,id,task,due_date,note,status):
        self.id=id
        self.task=task
        self.due_date=due_date
        self.note=note
        self.status=status
    def __str__(self):
        return"{},{},{},{},{}".format(self.id,self.task,self.due_date,self.note,self.status)