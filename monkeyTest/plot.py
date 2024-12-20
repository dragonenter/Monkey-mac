import pickle
import matplotlib.pyplot as plt


with open('./info/cd9dcec_men.pickle', 'rb') as file:
    data = pickle.load(file)
    data_list = [x // 1024 for x in data]

# 打印数据以查看内容
print(data_list)
plt.plot(data_list)
plt.title('Line Graph Example')  # 添加标题
plt.xlabel('Index')              # 添加X轴标签
plt.ylabel('Y Axis Label')
plt.show()

# with open('./info/cd9dcec_cpu.pickle', 'rb') as file:
#     data = pickle.load(file)
#     data_list = [x // 1024 for x in data]
#
# # 打印数据以查看内容
# print(data)
# plt.plot(data)
# plt.title('Line Graph Example')  # 添加标题
# plt.xlabel('Index')              # 添加X轴标签
# plt.ylabel('Y Axis Label')
# plt.show()