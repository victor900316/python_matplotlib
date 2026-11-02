import matplotlib.pyplot as plt
plt.rc("font", family="Microsoft JhengHei") #設定中文字型
#一組資料點(1,2),(2,4),(3,6)
plt.plot([1,2,3],[2,4,6])
plt.show()
# #兩組資料點
#     (1,2),(2,4),(3,6)
#     (1,1),(2,2),(3,3)
plt.plot([1,2,3],[[2,1],[4,2],[6,3]],label=["第一組標籤","第二組標籤"])
plt.legend() #顯示圖例
plt.xlabel("X軸說明")
plt.ylabel("Y軸說明")
plt.show()

#從csv格式的檔案載入資料,並繪製折線圖
import  csv
file=open("data.csv",encoding="utf-8")
reader=csv.reader(file)
header=next(reader) #讀取標題列
print("標題", header)
x=[]
y=[] 
for row in reader:
    print("每列的資料" ,row)
    x.append(int(row[0]))
    y.append([int(row[1]), int(row[2])])
plt.plot(x, y,label=["小王","小美"])
plt.legend()
plt.xlabel(header[0])
plt.ylabel("薪資")
plt.show()