import re
#定义一个类
class CountWord:

    def __init__ (self,file_name):
        self.filename = file_name
        self.dict_count = {}
    def count_word(self):
        with open(self.filename,'r') as f:
            for line in f:
                words = []
                words = [s.lower() for s in re.findall("\w",line)]
                for word in words:
                    self.dict_count[word] = self.dict_count.get(word,0) + 1
    def top_number(self,num):
        return sorted(self.dict_count.items(),key=lambda item:item[1],reverse=True) [:num]
if __name__  == '__main__':
    counter_obj = CountWord("test_count.txt")
    counter_obj.count_word()
    top_num_6 = counter_obj.top_number(6)
    print('test_count.txt','中出现次数前6的单词统计数如下：')
    for word in top_num_6:
        print(word[0],'出现:',word[1],'次')