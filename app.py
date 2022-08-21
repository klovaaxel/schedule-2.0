from flask import Flask, render_template, request
import webbrowser

from components.school import schoolWeeks, groups
from components.general import currentWeek



def sortAssignments(selectedWeek):

    schoolWeeksOrder = schoolWeeks[schoolWeeks.index(selectedWeek):] + schoolWeeks[:schoolWeeks.index(selectedWeek)]
    schoolWeeksOrder.append('')

    for groupID in groups: 
        group = groups[groupID]
        for courseID in group['courses']:
            course = group['courses'][courseID]

            course['assignments'].sort(key=lambda x: schoolWeeksOrder.index(x['end-week']), reverse=False)


app = Flask(__name__)

@app.route('/schedule', methods=('GET', 'POST'))
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

@app.route('/schedule/<string:groupID>/<string:course>')
def schedule(groupID, course):     

    selectedWeek = request.args.get('week')
    if selectedWeek == None:
        selectedWeek = currentWeek
    selectedWeek = int(selectedWeek)

    sortAssignments(selectedWeek) 

    return render_template('schedule.html',
        course = groups[groupID]['courses'][course],
        selectedWeek = selectedWeek,
        schoolWeeks = schoolWeeks + ['']
    )

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
