from h2o_wave import main, app, Q, ui


@app('/main')
async def serve(q: Q):
    if q.args.show_inputs:
        q.page['textbox'].items = [
            ui.text(f'textbox={q.args.textbox}'),
            ui.button(name='show_form', label='Back', primary=True),
        ]
    else:
        q.page['textbox'] = ui.form_card(box='1 1 4 10', items=[
            ui.textbox(name='textbox', label='Enter the text to be analyzed'),
            ui.button(name='show_inputs', label='Request', primary=True),
        ])
    await q.page.save()
