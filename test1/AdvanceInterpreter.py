#-*-coding:utf-8-*-
#Next let's add variables to our interpreter.
#  Variables require an instruction for storing the value of a variable,
# STORE_NAME; an instruction for retrieving it, LOAD_NAME; and a mapping from variable names to values.
# For now, we'll ignore namespaces and scoping, so we can store the variable mapping on the interpreter object itself.
# Finally, we'll have to make sure that what_to_execute has a list of the variable names,
# in addition to its list of constants.
""">>> def s():
    a = 1
    b = 2
   print(a + b)
"""
#python Interpreter实现上述功能，如何解决变量和实际数字的映射关系
what_to_execute={"instructions":[("LOAD_VALUE",0),("STORE_NAME",0),("LOAD_VALUE",1),
                                 ("STORE_NAME",1),("LOAD_NAME",0),("LOAD_NAME",1),
                                 ("ADD_TWO_VALUES",None),("PRINT_ANSWER",None)],
                 "numbers":[1,2],
                 "names":["a","b"]}
class Interpreter:
    #__init__定义一些基本的属性
    def __init__(self):
        self.stack=[]
        self.environment={}
        #enviroment={"a":1,"b":2}映射关系
    def LOAD_VALUE(self,number):
       self.stack.append(number)
    #建立数字和变量的映射关系
    def STORE_NAME(self,name):
        val=self.stack.pop()
        self.environment[name]=val
        print(val)
    def LOAD_NAEM(self,name):
        #将字母映射对应的数字加载到stack中去
        val=self.environment[name]
        self.stack.append(val)
    def ADD_TWO_VALUES(self):
        the_first_num=self.stack.pop()
        the_second_num=self.stack.pop()
        total=the_first_num+the_second_num
        self.stack.append(total)
    def PRINT_ANSWER(self):
        answer=self.stack.pop()
        print(answer)
        #实现变量名和数字的映射关系
    def parse_argument(self,instruction,argument,what_to_execute):
        numbers=['LOAD_VALUE']
        #变量操作类型
        names=["LOAD_NAME","STORE_NAME"]
        if  instruction in numbers:         #
            #获取实际的数字1,2
            argument=what_to_execute["numbers"][argument]
            #获取变量a,b,获取a,b后在通过load_name将字母映射到对应的数字
        elif instruction in names:
            argument=what_to_execute["names"][argument]
        return argument
    def run_code(self,what_to_execute):
        instructions=what_to_execute["instructions"]
        for each_step in instructions:
            instruction,argument=each_step
            #argument 代表 0,1,经过parse_argument函数后实现argument等于正在的操作数1,2
            argument=self.parse_argument(instruction,argument,what_to_execute)
            if  instruction=="LOAD_VALUE":
                self.LOAD_VALUE(argument)
            elif instruction=="STORE_NAME":
                self.STORE_NAME(argument)
            elif instruction=="LOAD_NAME":
                self.LOAD_NAEM(argument)
            elif instruction == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUES()
            elif instruction=="PRINT_ANSWER":
                self.PRINT_ANSWER()
          """bytecode_method=getattr(self,instruction)
             if argument is None:
                bytecode_method()
             else:
                bytecode_method(argumnent)
            
    
          """

if  __name__=="__main__":
    inter=Interpreter()
    inter.run_code(what_to_execute)

