from functools import wraps 
from datetime import tzinfo, datetime, timedelta

def timer(f):
    @wraps(f)
    
    def test_decorators:
        date = datetime.now()
        if(user_logged_in):
            f()
        else:
            print("logged in")
        print(date)
        print(datetime.now() - date)
    
    return test_decorators

@check_logged_in
def print_name():
    '''
        takes a string and returns a string
    '''
    print("Mike")
    print("Eniwoke")
    print("Daniel")
    print("Cire")

print_name()