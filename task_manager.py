import psutil

def get_system_info():
    """Retrieve basic system information."""
    cpu_usages = psutil.cpu_percent(interval=1)

    mem = psutil.virtual_memory()
    total_memory = mem.total / (1024 ** 3)  # Convert to GB
    used_memory = mem.used / (1024 ** 3)    # Convert to GB 

    stats = {
        "CPU": f"{cpu_usages}%",
        "Total Memory": f"{used_memory:.2f} / {total_memory:.2f} GB"
    }

    for partition in psutil.disk_partitions():
       
       try:

        usage = psutil.disk_usage(partition.mountpoint)
        used_gb = usage.used / (1024 ** 3)
        total_gb = usage.total / (1024 ** 3)
        stats[f"Disk ({partition.device})"] = f"{used_gb:.2f} / {total_gb:.2f} GB"
       except PermissionError:
        continue  # Skip partitions that cannot be accessed
    return stats

resource = get_system_info()
for name, usage in resource.items():
    print(f"{name}: {usage}")  
