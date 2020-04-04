import requests
import matplotlib
import matplotlib.pyplot as plt

SITES = [
    'http://www.google.com',
    'http://www.google.it',
    'http://netflix.com',
    'http://polimi.it',
    'https://beep.metid.polimi.it'
]
N = 10

max_val = 0
min_val = 0


# Initialize the plot
plt.figure()

for url in SITES:
    times = []
    
    print('Now testing (id: ', id, ') ', url)
    for i in range(N):
        req = requests.get(url)
        times.append(req.elapsed.microseconds/1000)

    print('Response times:')
    print('Max: ', '{0:.2f}'.format(max(times)), 'ms')
    print('Min: ', '{0:.2f}'.format(min(times)), 'ms')
    print('Avg: ', '{0:.2f}'.format(sum(times) / len(times)), 'ms')

    # Save max time and plot the data
    max_val = max([max_val, max(times)])
    min_val = min([min_val, min(times)])
    plt.plot(times, label=url)
    plt.ylim([.9*min_val, 1.1*max_val])

plt.title('GET request response times')
plt.xlabel('ID Richiesta')
plt.ylabel('[ms]')
plt.grid()
plt.legend(loc='lower right', fontsize=8)
plt.show()