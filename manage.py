'''
    Example Implementation: Server Management
'''

import sys
from tsk import TaskRunner, Task

tr = TaskRunner(enableHelp = True) # enable help to automatically generate a 'help' command

tr.AddTask(Task('dev', '...run development server...'))
tr.AddTask(Task(['production', 'pro'], '...run production server...'))
tr.AddTask(Task(['test'], '...run tests...'))
tr.AddTask(Task(['migrate'], '...run db migrations...'))

# Run the command line argument
tr.RunTask(sys.argv[1])
