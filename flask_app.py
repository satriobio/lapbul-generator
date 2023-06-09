from flask import Flask, request, render_template
from mistune import html
import io
import csv

def toHTML(markdown):
    return html(markdown)

def toObj(file):
    uploaded_file = request.files[file]    
    csv_data = uploaded_file.read().decode('utf-8')
    csv_file = io.StringIO(csv_data)

    data = []
    reader = csv.DictReader(csv_file, delimiter =';')
    for row in reader:
        data.append({
            'tanggal'   : row['tanggal'], 
            'kegiatan'  : row['kegiatan'], 
            'lokasi'    : row['lokasi'], 
            'masuk'     : row['masuk'], 
            'keterangan': row['keterangan'], 
            })

    return data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        return render_template(
            'base.html',
            name = request.form['user'],
            role = request.form['role'],
            type = request.form['type'],
            number = request.form['number'],
            number_date = request.form['number_date'],
            month = request.form['month'],
            month2 = request.form['month'],
            year = request.form['year'],
            scope = toHTML(request.form['scope']),
            output = toHTML(request.form['output']),
            plan = toHTML(request.form['plan']),
            attachmentA = toObj('attachmentA'),
            pemeriksa = request.form['pemeriksa'],
            pemeriksa_role = request.form['pemeriksa_role'],
            menyetujui = request.form['menyetujui'],
            menyetujui_role = request.form['menyetujui_role'],
            mengetahui = request.form['mengetahui'],
            mengetahui_role = request.form['mengetahui_role'],
        )
    return render_template('form.html')
