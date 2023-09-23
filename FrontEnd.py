import subprocess
from flask import Flask, render_template, request, redirect, url_for
import os
from Textbox_Input import count_nucleotides

app = Flask(__name__)

# Define the directory where uploaded files will be saved
upload_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'UPLOADS')

@app.route('/')
def Dozzd():
    return render_template('design.html')

@app.route('/', methods=['POST'])
def process_sequence():
    if 'input-sequence' in request.form:
        # Process nucleotide sequence from the text box
        sequence_input = request.form['input-sequence']
        sequence_result = count_nucleotides(sequence_input)
        return render_template('design.html', result=sequence_result)
    elif 'input-file' in request.files:
        uploaded_file = request.files['input-file']

        if uploaded_file.filename != '':
            # Ensure the 'UPLOADS' directory exists
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)

            # Save the uploaded file to the 'UPLOADS' directory
            file_path = os.path.join(upload_dir, uploaded_file.filename)
            uploaded_file.save(file_path)

            # Process the uploaded file using Sequence_Info.py
            # Replace 'Sequence_Info.py' with the actual script name and arguments
            subprocess_result = subprocess.run(['python', 'Sequence_Info.py', file_path], stdout=subprocess.PIPE, text=True)

            # Retrieve the output from the subprocess
            sequence_result = subprocess_result.stdout

            # Display the result without generating an output file
            return render_template('design.html', result=sequence_result)

    return redirect(url_for('Dozzd'))

if __name__ == '__main__':
    app.run(debug=True)
