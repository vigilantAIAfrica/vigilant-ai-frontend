import psutil
import time
import os

# Create logs directory if it doesn't exist (Professional touch)
if not os.path.exists("logs"):
    os.makedirs("logs")

print("🛡️ Vigilant AI Heartbeat Monitor Started...")

while True:
    try:
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        
        if cpu > 80:
            print(f"⚠️ ALERT: High CPU Usage ({cpu}%)!")
        
        # 'a' means append - it keeps adding to the bottom of the file
        with open("logs/health.log", "a") as f:
            f.write(f"{time.ctime()}: CPU {cpu}% | RAM {mem}%\n")
            f.flush() # Forces the computer to save NOW (Crucial for rural power stability)
            
        time.sleep(5)
    except Exception as e:
        print(f"❌ Error monitoring system: {e}")
        time.sleep(10)
