#  Real-Time Network Traffic Monitor (Python)
A simple Python script that tracks your **internet traffic (upload & download speeds)** in real time using the `psutil` library.  
Displays data every second directly in your terminal.

---

##  Features
-  Real-time upload and download speed monitoring  
-  Uses `psutil` to read system network statistics  
-  Updates every second  
-  Lightweight and runs directly in the terminal  
-  Cross-platform (works on Windows, Linux, and macOS)

---

##  Requirements
Install the required library before running:

```bash
pip install psutil
 Usage
Run the script in your terminal:

bash
Copy code
python network_monitor.py
Example output:

bash
Copy code
 Trafik kuzatuvchi ishga tushdi (CTRL+C bilan to‘xtating):

⬆️ Chiquvchi (upload): 12.45 KB/s | ⬇️ Kiruvchi (download): 58.22 KB/s
⬆️ Chiquvchi (upload): 8.73 KB/s  | ⬇️ Kiruvchi (download): 33.19 KB/s
⬆️ Chiquvchi (upload): 10.04 KB/s | ⬇️ Kiruvchi (download): 41.67 KB/s
To stop the program, press CTRL + C.

 Project Structure
Copy code
network-monitor/
│
├── network_monitor.py
└── README.md
 How It Works
The script gets initial values of sent and received bytes using psutil.net_io_counters().

Every second, it calculates the difference from the previous values.

The upload and download rates are displayed in KB/s.

Notes
This script measures total system traffic, not per-application.

Works best with a one-second refresh rate (time.sleep(1)).

Requires psutil package (which is safe and widely used).

 Author
Developed by Coder-dev2006
 Python-based real-time network utility.

 License
This project is licensed under the MIT License — feel free to use and share.
