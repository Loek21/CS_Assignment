import csv
import matplotlib.pyplot as plt
year_list = []
WO_list = []
beer_list = []
with open("istherecorrelation.csv") as input:
    reader = csv.reader(input, delimiter=';')
    next(reader)
    for row in reader:
        year_list.append(int(row[0]))
        WO_list.append(float(row[1].replace(",","."))*1000)
        beer_list.append(float(row[2].replace(",","."))*1000)

fig = plt.figure()
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.5, hspace=0.5)
ax1 = fig.add_subplot(2,1,1)
ax1.plot(year_list, WO_list, "b-", label="Number of WO students")
ax1.set_ylabel("Number of students")
ax1.set_xlabel("Year")
plt.title("Correlation between WO students and beer consumption?")
ax1.legend(loc="best")
ax2 = fig.add_subplot(2,1,2)
ax2.plot(year_list, beer_list, "r-", label="Beer consumption in hectoliter")
ax2.legend(loc="best")
ax2.set_ylabel("Hectoliter of beer consumed")
ax2.set_xlabel("Year")
fig.savefig('plot.svg', format='svg', dpi=300)
