# Plot random walk
dpi = 300
fig, ax = plt.subplots()
fig.set_size_inches(3, Circ * 3. / Length)
ax.set_xlim(0, Length - 1)
ax.set_ylim(0, Circ - 1)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.plot(*zip(*trajectory), linewidth=0.3)
plt.savefig("plots/"+__file__[:-3]+".png", bbox_inches="tight", dpi=dpi)
