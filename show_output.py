import numpy as np
import matplotlib.pyplot as plt

cars = ['LIKE THEATRE', 'LIKE OTT', ]

data = [43, 57]

explode = (0.1, 0.0)

colors = ( "indigo", "beige")

wp = { 'linewidth' : 1, 'edgecolor' : "green" }

def func(pct, allvalues):
	absolute = int(pct / 100.*np.sum(allvalues))
	return "{:.1f}%\n({:d} )".format(pct, absolute)

fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(data,
								autopct = lambda pct: func(pct, data),
								explode = explode,
								labels = cars,
								shadow = True,
								colors = colors,
								startangle = 90,
								wedgeprops = wp,
								textprops = dict(color ="orange"))

ax.legend(wedges, cars,
		title ="Platforms",
		loc ="center left",
		bbox_to_anchor =(1, 0, 0.5, 1))

plt.setp(autotexts, size = 8, weight ="bold")
ax.set_title("Theatre VS OTT")

plt.show()
