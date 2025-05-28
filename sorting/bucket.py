data = []
n = int(input("Enter the number of objects present: "))
for i in range(n):
    element = float(input(f"Enter number {i+1}: "))
    data.append(element)

def bucket_sort(data):
    data = data.copy()

    if len(data) == 0:
        print("Empty input.")
        return

    min_val = min(data)
    max_val = max(data)
    range_val = max_val - min_val

    bucket_count = 10
    buckets = [[] for _ in range(bucket_count)]

    for num in data:
        index = int(((num - min_val) / range_val) * (bucket_count - 1))
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_data = [num for bucket in buckets for num in bucket]

    print("Sorted data using Bucket Sort:", sorted_data)

bucket_sort(data)
