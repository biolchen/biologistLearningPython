##
from IPython.display import HTML, display
from matplotlib import pyplot as plt

fig = plt.figure(1)
x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]
plt.subplot(2, 1, 1)

plt.plot(x, straight_line)
plt.subplot(2, 2, 3)
plt.plot(x, parabola)
plt.subplot(2, 2, 4)
plt.plot(x, cubic)
plt.subplots_adjust(wspace=0.35, bottom=0.2)
plt.show(block=False)
##
plt.figure(2)
months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]
plt.cla()
fig = plt.figure(2)
for i in range(8):
    ax = fig.add_subplot(2, 4, i + 1)
    ax.plot(months, hyrule)
    ax.plot(months, kakariko)
    ax.plot(months, gerudo)
    ax.set_title('loc: {}'.format(str(i + 1)))
    legend_labels = ["Hyrule", "Kakariko", "Gerudo Valley"]
    ax.legend(legend_labels, loc=i + 1)
plt.show(block=False)
##
fig = plt.figure(3)
x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]
plt.subplot(2, 1, 1)

plt.plot(x, straight_line)
plt.subplot(2, 2, 3)
plt.plot(x, parabola)
plt.subplot(2, 2, 4)
plt.plot(x, cubic)
plt.subplots_adjust(wspace=1.35, bottom=0.2)
plt.show()
##
fig = plt.figure(4)
month_names = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
    "Nov", "Dec"
]

months = range(12)
conversion = [
    0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85
]

plt.xlabel("Months")
plt.ylabel("Conversion")

plt.plot(months, conversion)

# Your work here
ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
ax.set_yticks([0.10, 0.25, 0.5, 0.75])
ax.set_yticklabels(["10%", "25%", "50%", "75%"])

plt.show()
##
fig = plt.figure(5)
month_names = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
    "Nov", "Dec"
]

months = range(12)
conversion = [
    0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85
]

plt.xlabel("Months")
plt.ylabel("Conversion")

plt.plot(months, conversion)

# Your work here
ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
ax.set_yticks([0.10, 0.25, 0.5, 0.75])
ax.set_yticklabels(["10%", "25%", "50%", "75%"])

plt.show()
##
plt.figure(6)

x = range(6)
y1 = [1, 2, 3, 4, 5, 6]
y2 = [-1, 1, 3, 4, 4, 4]

plt.plot(x, y1, marker='o', color='pink')
plt.plot(x, y2, marker='o', color='gray')

plt.title("Two Lines on One Graph")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")

plt.legend(["Y1", "Y2"], loc=4)

plt.show()
##

months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
    "Nov", "Dec"
]

visits_per_month = [
    9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309,
    8724
]

# numbers of limes of different species sold each month
key_limes_per_month = [
    92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0,
    106.0
]
persian_limes_per_month = [
    67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0
]
blood_limes_per_month = [
    75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0
]

# create your figure here
fig = plt.figure(num=7, figsize=[12, 8])

ax1 = plt.subplot(1, 2, 1)

x_values = range(len(months))

plt.plot(x_values, visits_per_month, marker='s')
plt.xlabel('Month')
plt.ylabel('# of Site Visits')

ax1.set_xticks(x_values)
ax1.set_xticklabels(months)
plt.title('Site Visits per Month')

ax2 = plt.subplot(1, 2, 2)

plt.plot(x_values,
         key_limes_per_month,
         color='green',
         label='Key Limes',
         marker='s')

plt.plot(x_values,
         persian_limes_per_month,
         color='blue',
         label='Persian Limes',
         marker='d')

plt.plot(x_values,
         blood_limes_per_month,
         color='red',
         label='Blood Limes',
         marker='o')

ax2.set_xticks(x_values)
ax2.set_xticklabels(months)
plt.title('Limes Sold per Month')

plt.legend()

plt.subplots_adjust(wspace=.1)
plt.show()
matplotlib.get_configdir()
# ?%%



print('aaa')
# ?%%
