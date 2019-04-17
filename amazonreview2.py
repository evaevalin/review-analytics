data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 100000 == 0:  #10000的倍數 餘數=0
            print (len(data)) #每10000筆 出現一次資訊
print('檔案讀取完,有',len(data),'筆資料')

print(data[0])   # 列印出第一筆留言

#文字記述 (留言分析程式 查出字出現幾次)  
wc = {}# word_count字典
for d in data:#d:一筆留言 data:有100萬筆留言的清單
    words = d.split() #split()預設就是空白空字串切，遇到空白就切變成words清單，現在拆成很多小字串
    for word in words: #清單裡的每一個字word
        if word in wc:
        	wc[word] += 1 #去wc字典找word 如果有出現在字典裡 就+1             
        else: 
        	wc[word] = 1 #如果字典沒有這個word 那就新增字裏頭 次數就當作1

for word in wc:    #印成這樣比較清楚 因為如果直接印print(word) 會印出超多 格式也很亂
    if wc[word] > 1000000: #出現在字典的次數超過100000次
        print(word, wc[word]) 

print(len(wc)) #印出字典的長度 總共有幾個字
print(wc['allen'])#看allen在這個字典 出現幾次

#讓使用者查字
while True:  #可以無限迴圈 一直查
     word = input('請問您想要查什麼字: ')
     if word == 'q':#要加一個q 不然會繼續無限迴圈 出不去 慘~
         break
     if word in wc: #必須加此行 不然到時候沒有字 程式會當掉
        print(word, '出現過的次數為: ',wc[word],'次')
     else:
        print('這個字沒有在這裡頭喔')
print('感謝使用本查詢功能') #break才不會進去繞




# sum_len = 0
# for d in data:
#     sum_len = sum_len + len(d)
# print('留言平均長度是',sum_len/len(data), '字數')

# new = []
# for d in data:
#     if len(d) < 100:
#         new.append(d)
# print('一共有', len(new), '筆資料長度小於100字')
# print(new[0])
# print(new[1])



# good =[]
# for d in data:
#     if 'good' in d:
#         good.append(d)
# print('共有', len(good), '筆留言提到good')
# print(good[0])

# good = [d for d in data if 'good' in d] #篩選快寫法
# print(good)

# bad = ['bad' in d for d in data]
# print(bad)

# bad =[]
# for d in data: 
#     bad.append('bad' in d)






