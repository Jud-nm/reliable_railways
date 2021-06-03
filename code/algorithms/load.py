from connections import Connection

employeeList = list()
employeeDict = {}

f = open("/reliable_railways/data/ConnectiesNationaal.csv")
myLine = f.readline()
print(myLine)
while (len(myLine)>0):
    connection_info = myLine.split(",")
    connection = (connection_info[0], connection_info[1])
    duration = connection_info[2]

    print("connection_info: ", connection_info)
    connections = {}
    connections[connection] = Connection(connection, duration )
    print(connections)
    myLine = f.readline()
f.close()