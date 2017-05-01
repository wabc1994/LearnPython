#-*-coding:utf-8-*-
import re,os
#get all files in designated path
#讲一系列的文件路劲以1数组的形式返回
def get_files(path):
    filepath=os.listdir(path)
    files=[]
    for fp in filepath:
        fpath=path+'/'+fp
        if(os.path.isfile(fpath)):
            files.append(fpath)
        elif(os.path.isdir(fpath)):
            files+=get_files(fpath)
    return files
def get_imortant_word(files):
    worddict={}
    #对每一个文件进行操作
    for filename in files:
        f=open(filename,'rb')
        s=f.read()
        #[a-zA-Z0-9]匹配任意一个数组字母字符
        words=re.findall(r'[a-zA-Z0-9]',s)
        for word in words:
            worddict[word]=worddict[word]+1 if word in worddict else 1
        f.close()
        wordsort=sorted(worddict.items(),key=lambda e:e[1],reverse=True)
        return wordsort
if __name__=="__main__":
    files=get_files('/home/liuxiongcheng/Downloads/Code')
    print files
    wordsort=get_imortant_word(files)
    maxnum=1
    for i in range(len(wordsort)-1):
        if wordsort[i][1]==wordsort[i][1]:
           maxnum+=1
        else:
            break
    f=open("text.txt",'wb')
    for i in range(maxnum):
        f.write(''.join(str(wordsort[i])+'\n'))
      #  f.write(''.join(str(v) for v in wordsort)+'\n')
    f.close()
    for i in range(maxnum):
        print wordsort[i]

#[('a',1),('b',2)]元祖列表
#可以讲元祖列表转换成字符串

