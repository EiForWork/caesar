# Line chart
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]  # ค่า x (แนวนอน)
y_values = [10, 12, 8, 15, 9]  # ค่า y (แนวตั้ง)
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b', label='ชื่อเส้น')
plt.xlabel('แกน X')
plt.ylabel('แกน Y')
plt.legend(['Line explain'])
plt.grid(True)  # เพิ่มกริดในกราฟ
plt.show()


