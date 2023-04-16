from io import BytesIO
from flask import Flask, request, send_file, render_template
from PyPDF2 import PdfFileMerger

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/merge', methods=['POST'])
def merge():
    file1 = request.files.get('file1')
    file2 = request.files.get('file2')

    if not file1 or not file2:
        return 'Please select two pdf files to merge. Python', 400

    merger = PdfFileMerger()

    merger.append(file1)
    merger.append(file2)

    output = BytesIO()
    merger.write(output)
    merger.close()

    output.seek(0)

    return send_file(output, attachment_filename='merged.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run()

