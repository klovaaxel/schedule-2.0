from flask import Flask, render_template, request
import webbrowser

from components.school import schoolWeeks, groups
from components.general import currentWeek

app = Flask(__name__)

@app.route('/schedule', methods=('GET', 'POST'))
def schedule():

    selectedWeek = request.form.get('week-select')
    if selectedWeek == None:
        selectedWeek = currentWeek
    else: 
        selectedWeek = int(selectedWeek)


    selectedGroupID = request.form.get('group-select')
    if selectedGroupID == None: 
        selectedGroupID = 0

    groupIDParam = request.args.get('group')
    if groupIDParam != None:
        selectedGroupID = groupIDParam

    selectedGroupID = int(selectedGroupID)


    return render_template('schedule.html', 
        groups = groups,
        selectedGroupID = selectedGroupID,
        schoolWeeks = schoolWeeks,
        currentWeek = currentWeek,
        selectedWeek = selectedWeek,
    )

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
