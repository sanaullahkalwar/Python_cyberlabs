import pandas as pd
import matplotlib.pyplot as plt

# Load CSV log
df = pd.read_csv('/home/sanaullah/Desktop/MS-Cyber-Security/Second-semester/Python-and-Shell-Programming/Bash-Scripting/CyberLab/Scripts/Regular expressions/Internet_speed_monitoring/speed_log.csv')

# Ensure Timestamp is parsed as datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Sort by time (in case entries are unordered)
df = df.sort_values('Timestamp')

# Plot Download and Upload Speeds over Time
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['Download (Mbps)'], label='Download Speed (Mbps)', linewidth=2)
plt.plot(df['Timestamp'], df['Upload (Mbps)'], label='Upload Speed (Mbps)', linewidth=2)
plt.xlabel('Time')
plt.ylabel('Speed (Mbps)')
plt.title('Internet Speed Over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot Ping over Time
plt.figure(figsize=(10, 5))
plt.plot(df['Timestamp'], df['Ping (ms)'], color='red', linewidth=2)
plt.xlabel('Time')
plt.ylabel('Ping (ms)')
plt.title('Ping Over Time')
plt.grid(True)
plt.tight_layout()
plt.show()
