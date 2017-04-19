#파일에 포함된 단어들을 리스트로 만들어 반환
#대소문자 통일 -> 숫자, 특수 문자 삭제


f = open('hyu.txt', 'r')
raw_data = f.read()
for i in raw_data:
    if i == "," or i == "." or i == "(" or i == ")" : #특수 문자 제거
        raw_data = raw_data[:raw_data.find(i)] + raw_data[raw_data.find(i)+1:]

list_of_word = raw_data.lower().split()


for s in list_of_word:
    try:
        if type(float(s)) == float: #숫자인 요소들을 리스트에서 제거
            list_of_word.remove(s)
    except ValueError:
        pass

word_dict = {}

for word in list_of_word: #단어와 출현 빈도수를 key, value로 가지는 dict 
    if word not in word_dict.keys():
        word_dict[word] = 1
    elif word in word_dict.keys():
        word_dict[word] += 1

for s in word_dict: #딕셔너리의 key, value를 튜플 형태로 만들어 txt file에 write
    f2 = open('counting_lab.txt', 'a')
    word_tuple = (s, word_dict[s])
    f2.write(str(word_tuple) + "\n")
f2.close()
