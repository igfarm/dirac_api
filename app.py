from flask import Flask, render_template, request, redirect, url_for
from dirac import DiracLiveProcessor
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
name = os.getenv("NAME")
dirac_url = os.getenv("DIRAC_URL")
port = int(os.getenv("PORT", 5000))
camilla_url = os.getenv("CAMILLA_URL")
uvmeter_url = os.getenv("UVMETER_URL")

processor = DiracLiveProcessor(base_url=dirac_url)

@app.route('/')
def index():
    try:
        slots = processor.get_slots()
        active_slot = processor.get_active_slot()
        speaker_gain = processor.get_speaker_gain()
        filter_state = processor.get_filter_state()
    except Exception as e:
        return f"An error occurred: {e}"

    return render_template('index.html', 
                           name=name,
                           slots=slots, 
                           active_slot=active_slot, 
                           speaker_gain=speaker_gain,
                           filter_state=filter_state,
                           uvmeter_url=uvmeter_url,
                           camilla_url=camilla_url)

@app.route('/set-slot', methods=['POST'])
def set_slot():
    slot_index = request.form.get('slot_index')
    try:
        processor.set_active_slot(int(slot_index))
    except Exception as e:
        return f"An error occurred: {e}"

    return redirect(url_for('index'))

@app.route('/reset-gain', methods=['POST'])
def reset_gain():
    try:
        processor.set_speaker_gain(0)
    except Exception as e:
        return f"An error occurred: {e}"

    return redirect(url_for('index'))

@app.route('/set-filter-state', methods=['POST'])
def set_filter_state():
    filter_state = request.form.get('filter_state') == 'true'
    try:
        processor.set_filter_state(filter_state)
    except Exception as e:
        return f"An error occurred: {e}"

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=port)