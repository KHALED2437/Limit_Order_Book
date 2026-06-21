import csv

latencies = []
with open('order_processing_times.csv') as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        try:
            latencies.append(float(row[0]))
        except:
            pass

if latencies:
    avg = sum(latencies) / len(latencies)
    min_lat = min(latencies)
    max_lat = max(latencies)
    throughput = 1_000_000 / avg
    
    print(f'Average Latency: {avg:.2f} ns')
    print(f'Min Latency: {min_lat:.2f} ns')
    print(f'Max Latency: {max_lat:.2f} ns')
    print(f'Throughput: {throughput:.0f} orders/sec')
    print(f'Total Orders: {len(latencies)}')