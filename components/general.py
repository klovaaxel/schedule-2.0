from datetime import date
from components.school import schoolWeeks, groups

currentWeek = date.today().isocalendar()[1]

def sortAssignments(selectedWeek):

    schoolWeeksOrder = schoolWeeks[schoolWeeks.index(selectedWeek):] + schoolWeeks[:schoolWeeks.index(selectedWeek)]
    schoolWeeksOrder.append('')

    for groupID in groups: 
        group = groups[groupID]
        for courseID in group['courses']:
            course = group['courses'][courseID]

            course['assignments'].sort(key=lambda x: schoolWeeksOrder.index(x['end-week']), reverse=False)
