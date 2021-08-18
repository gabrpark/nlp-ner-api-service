from h2o_wave import main, app, Q, ui
import requests
import json

@app('/wave_app')
async def serve(q: Q):
    if q.args.show_inputs:
        payload = q.args.textbox
        URL_param = f"http://127.0.0.1:8000/?input_text={payload}" #api endpoint + parameter
        res = requests.post(URL_param) # Send the input text to the api then receive the NER analysis
        data = res.text # Take the content of the response from the api
        parse_json = json.loads(data)
        q.page['textbox'].items = [
            ui.text(f'Results={parse_json}'), # Display the NER analysis result
            ui.button(name='show_form', label='Back', primary=True),
        ]
    else:
        q.page['textbox'] = ui.form_card(box='1 1 4 10', items=[
            ui.textbox(name='textbox', label='Enter the text to be analyzed by NER'),
            ui.button(name='show_inputs', label='Submit', primary=True),
        ])
    await q.page.save()