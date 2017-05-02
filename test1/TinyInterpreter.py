#-*coding:utf-8-*
what_to_execute={
    "instructions":[("LOAD_VALUE",0), #the first number
                    ("LOAD_VALUE",1),#the second number
                    ("ADD_TWO_VALUES",None),
                    ("PRINT_ANSWER",None)],
    "numbers":[7,5]}
class Interpreter:
    #stack是编译器的一个属性
    def __init__(self):
        self.stack=[]#相当于构造函数
    #the LOAD_VALUE  tells the interpreter to push a number on to the stack
    def LOAD_VALUE(self,number):
        self.stack.append(number)
        print('加载数据')

    def ADD_Two_VALUES(self):
        first_num=self.stack.pop()
        second_num=self.stack.pop()
        total=first_num+second_num
        self.stack.append(total)
        print('两个数据相加')

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print('打印结果')
        print(answer)
    def run_code(self,what_to_execute):
        instructions=what_to_execute["instructions"]
       # instructions=[("LOAD_VALUE",0), ("LOAD_VALUE",1) , ("ADD_TWO_VALUES",None),("PRIN_ANSWER",None) ]
        numbers=what_to_execute["numbers"]
        #numbers=[7,5]
        # 对instructions中的每一个操作进行如下操作：
        for each_step in instructions:
            instruction,argument=each_step  #  instruction="LOAD_VALUE" ,argument=1,分别赋值
            #每个指令对应下面的操作
            if   instruction=="LOAD_VALUE":
                number=numbers[argument]
                self.LOAD_VALUE(number)
            elif instruction=="ADD_TWO_VALUES":
                self.ADD_Two_VALUES()
            elif instruction=="PRINT_ANSWER":
                self.PRINT_ANSWER()
if __name__=="__main__":
    interpreter=Interpreter()
    interpreter.run_code(what_to_execute)
