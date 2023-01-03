registerd = {}


def func_1():
    print("Давай начнем")
    

def func_2():
    print("Давай закончим")
    
def register_func(another_func, name):
    registerd[name] = another_func
    
    
register_func(func_1, "start")
register_func(func_2, "stop")

user_input = input("Введите комануду ")
func_to_call = registerd.get(user_input)
func_to_call()
