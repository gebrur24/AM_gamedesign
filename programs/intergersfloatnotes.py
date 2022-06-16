


import codeop
from distutils.log import info


def student_info(args, kwargs):
    print (args)
    print (kwargs) 

    courses = ['math', 'art']

student_info('Math', 'Art' , name ='Ruth', age=17)

student_info(*courses, **info)
