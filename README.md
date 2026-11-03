# EX01 Developing a Simple Webserver
## Date:03.11.2026

## AIM:
To develop a simple webserver to serve html pages and display the Windows Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<h1>DHARSINI R (26005256)</h1>
</head>
<body>
<table border="1" cellpadding="5" cellspacing="1" font style="Arial Black">
<tr>
<td>Device name</td>
<td>sucan</td>
</tr>
<tr>
<td>Installed ram</td>
<td>16.0 GB (15.7 GB usable)</td>
</tr>
<tr>
<td>Grapics card</td>
<td>Intel(R) Graphics (128 MB)</td>
</tr>
<tr>
<td>Storage</td>
<td>127 GB of 477 GB used</td>
</tr>
<tr>
<td>Device ID</td>
<td>ED6EDCF4-9704-4704-8948-62712A141159</td>
</tr>
<tr>
<td>Product ID</td>
<td>00342-42943-38930-AAOEM</td>
</tr>
<tr>
<td>System type</td>
<td>64-bit operating system, x64-based processor</td>
</tr>
<tr>
<td>Pen and touch</td>
<td>No pen or touch input is available for this display</td>
</tr>
</table>
</body>
</html>
     
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()
"""


## OUTPUT:
![alt text](<Screenshot (11).png>)
![alt text](<Screenshot (12).png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
