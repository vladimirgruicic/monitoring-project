from bottle import Bottle, run, template, static_file
import psutil
import sqlite3

app = Bottle()

@app.route('/')
def home():
    return template('views/home.html')

@app.route('/alerts')
def alerts():
    return template('views/alert.html')

@app.route('/collect_metrics')
def collect_metrics():
    #Metrics that we collect.
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    #Store metrics in database.
    conn = sqlite3.connect('data/metrics.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO metrics (cpu_usage, memory_usage, disk_usage) VALUES (?, ?, ?)",
                   (cpu_usage, memory_usage, disk_usage))
    
    conn.commit()
    conn.close()

    return "Metrics collected and stored in database sucessfully!"


# Route for serving static files
@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./static')

if __name__ == '__main__':
    run (app, host='localhost', port=8080, debug=True)