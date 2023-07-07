from bottle import Bottle, run, template, static_file, HTTPError
import psutil
import sqlite3

app = Bottle()

app.error(404)
def error_404(error):
    return "404 Not Found!"

app.error(500)
def error_500(error):
    return "500 Not Found!"

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

    metrics= {
        'cpu_usage' : cpu_usage,
        'memory_usage' : memory_usage,
        'disk_usage' : disk_usage
    }

    #Store metrics in database.
    conn = sqlite3.connect('data/metrics.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO metrics (cpu_usage, memory_usage, disk_usage) VALUES (?, ?, ?)",
                   (metrics['cpu_usage'], metrics['memory_usage'], metrics['disk_usage']))
    
    conn.commit()
    conn.close()

    return template('views/collect_metrics.html', cpu_usage=cpu_usage, memory_usage=memory_usage, disk_usage=disk_usage, metrics=metrics)


# Route for serving static files
@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./static')

if __name__ == '__main__':
    try:
        run (app, host='localhost', port=8080, debug=True)
    finally:
        app.close()