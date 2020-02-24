[plt.show() for _, __, ___, plt in [(plt.plot(x, y1, color='r'), plt.plot(x, y2, color='r'), np, plt) for x, y1, y2, np, plt in [(x, 0.618*np.abs(x) - 0.8* np.sqrt(64-x**2), 0.618*np.abs(x) + 0.8* np.sqrt(64-x**2), np, plt) for x, np, plt in [(np.linspace(-8, 8, 1024), np, plt) for np, plt in [(__import__('numpy'), __import__('pylab'))]]]]]

# numpy matplotlib
