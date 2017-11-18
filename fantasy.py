roster = [
    {"name":"Jared Goff","position":"QB"},
    {"name":"Julio Jones","position":"WR"},
    {"name":"Travis Kelce","position":"TE"},
    {"name":"Demaryius Thomas","position":"WR"},
    {"name":"TY Hilton","position":"WR"},
    {"name":"Lamar Miller","position":"RB"},
    {"name":"Kenyan Drake","position":"RB"},
    {"name":"Christian McCaffrey","position":"RB"},
    {"name":"Rex Burkhead","position":"RB"},
    {"name":"Samaje Perine","position":"RB"},
    {"name":"D'Onta Foreman","position":"RB"},
    {"name":"Jamison Crowder","position":"WR"},
    {"name":"Sammy Watkins","position":"WR"},
    {"name":"DeSean Jackson","position":"WR"}
]

week = [
    {"name":"Jared Goff","points":14.4},
    {"name":"Julio Jones","points":10.1},
    {"name":"Travis Kelce","points":9.3},
    {"name":"Demaryius Thomas","points":7.4},
    {"name":"TY Hilton","points":0},
    {"name":"Lamar Miller","points":12.4},
    {"name":"Kenyan Drake","points":9.1},
    {"name":"Christian McCaffrey","points":0},
    {"name":"Rex Burkhead","points":6.6},
    {"name":"Samaje Perine","points":7.5},
    {"name":"D'Onta Foreman","points":5.8},
    {"name":"Jamison Crowder","points":7.2},
    {"name":"Sammy Watkins","points":6},
    {"name":"DeSean Jackson","points":7.5}
]

def points_list(position):
    n=0
    points = []

    while n<=len(roster)-1:
        if roster[n]['position'] == position:
            #the below assumes week is same order and only has players on roster list
            points.append(week[n]['points'])
            n = n+1
        else:
            n=n+1
    return points

def starter(position,rank):
    points = sorted(points_list(position), reverse=True)[rank-1]
    n=0
    receiver = []
    
    while n<=len(week)-1:
        if week[n]['points']==points and roster[n]['position']==position:
            receiver.append(roster[n]['name'])
            n=n+1
        else:
            n=n+1
    return receiver

starter_list = [
    starter('QB',1)[0],
    starter('RB',1)[0],
    starter('RB',2)[0],
    starter('WR',1)[0],
    starter('WR',2)[0],
    starter('TE',1)[0]
]

flex_positions = ['WR','RB','TE']

def flex_points():
    n=0
    flex_list = []
    while n <= len(roster)-1:
        if roster[n]['name'] not in starter_list and roster[n]['position'] in flex_positions:
            flex_list.append(week[n]['points'])
            n=n+1
        else:
            n=n+1
    return sorted(flex_list, reverse=True)[0]

def flex():
    flex_player = []
    n=0
    while n <=len(week)-1:
        if week[n]['points']==flex_points() and roster[n]['name'] not in starter_list:
            flex_player.append(roster[n]['name'])
            n=n+1
        else:
            n=n+1
    return flex_player

position_list = ['QB','RB1','RB2','WR1','WR2','TE']

for position,starter in zip(position_list,starter_list):
    print(position+": "+starter)
print("FLEX"+": "+flex()[0])
