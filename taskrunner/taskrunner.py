import sys, subprocess

'''
    --- Custom Task Runner Utilities ---
'''
class Task:
    def __init__(self,name=[],script=''):
        if type(name) == str:
            self.name = [name]
        else:
            self.name = name

        self.script = script

class TaskRunner:
    def __init__(self):
        self.tasks = []

    def AddTask(self,task):
        if task != Task() and type(task) == Task:
            self.tasks.append(task)
        else:
            raise Exception('AddTask must take a valid Task object.')

    def AddTasks(self, tasks):
        # add proper error checking
        for task in tasks:
            self.AddTask(task)

    def RunTask(self,name):
        for task in self.tasks:
            if task.name == name or name in task.name:
                for path in self.__execute(task.script):
                    print(path, end="")
                return
        else:
            raise Exception('The script \'' + name + '\' could not be found.')

    def __execute(self,cmd):
        popen = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        for stdout_line in iter(popen.stdout.readline, ""):
            yield stdout_line 
        popen.stdout.close()
        return_code = popen.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, cmd)

'''
    --- Task Runner Implementation ---
'''
if __name__ == '__main__':
    taskRunner = TaskRunner()
    taskRunner.AddTasks([
        Task(['test'], 'python test.py'),
        Task(['dev','development', 'debug'],'export FLASK_APP=app && export FLASK_ENV=development && flask run'),
        Task(['pro','production'],'gunicorn  --bind 0.0.0.0:80 wsgi:app')
    ])
    taskRunner.RunTask(sys.argv[1])