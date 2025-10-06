import psutil
import time

# Boshlang‘ich qiymatlar
old_bytes_sent = psutil.net_io_counters().bytes_sent
old_bytes_recv = psutil.net_io_counters().bytes_recv

print("🔍 Trafik kuzatuvchi ishga tushdi (CTRL+C bilan to‘xtating):\n")

while True:
    time.sleep(1)  # 1 soniyada bir o‘lchaymiz
    new_bytes_sent = psutil.net_io_counters().bytes_sent
    new_bytes_recv = psutil.net_io_counters().bytes_recv

    sent = new_bytes_sent - old_bytes_sent
    recv = new_bytes_recv - old_bytes_recv

    print(f"⬆️ Chiquvchi (upload): {sent / 1024:.2f} KB/s | ⬇️ Kiruvchi (download): {recv / 1024:.2f} KB/s")

    old_bytes_sent = new_bytes_sent
    old_bytes_recv = new_bytes_recv
