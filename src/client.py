import sys
import time
import statistics
import requests

port = sys.argv[1] if len(sys.argv) > 1 else '8100'
URL = f'http://127.0.0.1:{port}/invocations'  # le service local de MLflow

# une transaction tres suspecte (gros montant, 9 operations en 24h, de nuit)
CORPS = {'dataframe_records': [{'montant': 8500.0, 'anciennete': 3,
                                'freq_24h': 9, 'nuit': 1}]}

# 1) un appel, on affiche la reponse
r = requests.post(URL, json=CORPS, timeout=10)
print('reponse :', r.status_code, r.json())

# 2) echauffement : 10 appels non mesures
for _ in range(10):
    requests.post(URL, json=CORPS, timeout=10)

# 3) 200 appels chronometres, en millisecondes
lat = []
for _ in range(200):
    t = time.perf_counter()
    requests.post(URL, json=CORPS, timeout=10)
    lat.append((time.perf_counter() - t) * 1000)

print(f'port {port} | mediane : {statistics.median(lat):.1f} ms'
      f' | p95 : {statistics.quantiles(lat, n=20)[18]:.1f} ms')