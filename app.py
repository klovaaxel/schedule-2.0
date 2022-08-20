from flask import Flask, render_template, request
import webbrowser

from components.school import schoolWeeks, groups
from components.general import currentWeek

app = Flask(__name__)

@app.route('/schedules', methods=('GET', 'POST'))
def schedules():

    # Week dropdown and url param
    selectedWeek = request.form.get('week-select')
    if selectedWeek == None:
        selectedWeek = currentWeek
    else:
        selectedWeek = int(selectedWeek)
    
    weekParam = request.args.get('week')
    if weekParam != None:
        selectedWeek = int(weekParam)

    # Group dropdown and url param
    selectedGroupID = request.form.get('group-select')
    if selectedGroupID == None: 
        selectedGroupID = 0

    groupIDParam = request.args.get('group')
    if groupIDParam != None:
        selectedGroupID = groupIDParam

    selectedGroupID = int(selectedGroupID)


    return render_template('schedules.html', 
        groups = groups,
        selectedGroupID = selectedGroupID,
        schoolWeeks = schoolWeeks,
        currentWeek = currentWeek,
        selectedWeek = selectedWeek,
    )

@app.route('/schedule/<string:group>/<string:course>')
def schedule(group, course):
    return render_template('shedule.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
