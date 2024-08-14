import matplotlib as plt

months = ['Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

sales = [50, 40, 50, 45, 40, 35, 40, 45, 55, 65, 95, 90]

plt.plot(months,sales, color = 'purple', linewidth = 4, marker = 'o', markerfacecolor = 'black', markersize = 10)

plt.xlabel('Months of the Year')

plt.ylabel('Sales in Thousands')

plt.title('Janie and Jack Monthly Sales')

plt.show()