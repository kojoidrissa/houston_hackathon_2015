def my_routes(stop_id):
    '''
    string -->dict
    get a stop id as a string, return a dict of
    {stop_id:[trip_id1, trip_id2...trip_idn]}
    '''

    import csv
    with open('stop_times_mini.csv', newline='') as csvfile:
        timetable = csv.reader(csvfile)
        for row in timetable:
            if row[3] == stop_id:
                print(', '.join(row))

# with open('some.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(someiterable)