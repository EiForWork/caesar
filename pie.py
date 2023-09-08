#python pie chart test
import matplotlib.pyplot as plt

sizes = [100,200,600,500]  # ข้อมูลสำหรับสัดส่วนของแต่ละส่วน
labels = ['ส่วน 1', 'ส่วน 2', 'ส่วน 3', 'ส่วน 4']  # รายการชื่อสำหรับแต่ละส่วน
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # ทำให้ Pie Chart เป็นรูปวงกลม
plt.show()
