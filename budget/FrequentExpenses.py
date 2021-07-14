from . import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()

expenses.read_expenses('data/spending_data.csv')

#create empty list
spending_categories = []

#create for loop
for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter=collections.Counter(spending_categories)
print(spending_counter)

#most common spending_categories
top5 = spending_counter.most_common(5)

#use zip command
categories, count = zip(*top5)

#create bar chart
fig, ax = plt.subplots()
ax.bar(categories,count)
ax.set_title('# of Purchases by Category')
plt.show()
