#**kwargs means keyword arguments
#**kwargs to let you functions take an arbitrary number of keyword arguments
def print_keyword_args(**kwargs):
    for key,value in kwargs.iteritems():
        #kwargs.iteritems()返回一个字典
        print "%s = %s "%(key,value)
print_keyword_args(first_name='john',last_name='Dow')

# ** unpack   kwargs dictionary
#func(a=1,b=2,c=3)
#args={'a':1,'b':2,'c':3}
func(**args)