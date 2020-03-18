import requests

SITES = [
    'http://www.google.com',
    'http://www.youtube.com'
]
N = 10

avg_times = []

for url in SITES:
    for i in range(N):
        times = []
        req = requests.get(url)
        times.append(req.elapsed.microseconds/1000)
    avg_times.append(sum(times) / len(times))

print('The page with the best average response time is:')
min_avg_id = avg_times.index(min(avg_times))
print(SITES[min_avg_id])
print('Average time: ', avg_times[min_avg_id])
