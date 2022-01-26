str1=input('enter your string: ')
str1=str1.replace('.',' ')
list_str1= str1.split(' ')
uniqe=set(list_str1)
uniqe=list(uniqe)
uniqe.remove('')
dic_count_word={}
for word in uniqe:
    dic_count_word[word]=list_str1.count(word)
sort_dic=sorted(dic_count_word.items(),key=lambda x:x[1],reverse=True)
output=[{a:b} for a,b in sort_dic][0:3]
print(output)

