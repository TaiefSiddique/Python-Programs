import sys

max_val = 1000
INFINITY = 9999
MAX = 8
ue5 = 0
ii = 0
sc = 0
customer = [{'number': 0, 'sit': '', 'name1': '', 'name': '', 'mobile_no': 0, 'roadNo': 0, 'houseNo': 0, 'payable': 0.0,
             'paid': 0.0, 'returned': 0.0, 'pay': {'month': 0, 'day': 0, 'year': 0}} for _ in range(100)]


def input1(i):
    global ii
    print("\n\n         Ticket No:", ii)
    customer[i]['number'] = ii
    ii += 1
    customer[i]['name'] = input("\n         Name:")
    customer[i]['mobile_no'] = int(input("         mobile no:"))
    customer[i]['sit'] = input("         Seat:")
    customer[i]['roadNo'] = int(input("         Road No:"))
    customer[i]['houseNo'] = int(input("         House No:"))
    customer[i]['payable'] = float(input("         Total Payable:"))
    customer[i]['paid'] = float(input("         Paid:"))
    customer[i]['returned'] = customer[i]['paid'] - customer[i]['payable']
    print("         Returned: {:.2f}".format(customer[i]['returned']))
    date_input = input("         Payment date(mm/dd/yyyy):").split('/')
    customer[i]['pay']['month'] = int(date_input[0])
    customer[i]['pay']['day'] = int(date_input[1])
    customer[i]['pay']['year'] = int(date_input[2])


def input_accounts():
    global sc
    print("How many Accounts you want to enter: ")
    sc = int(input())
    for i in range(sc):
        input1(i)
    ticket_counter()


def search():
    global sc
    print("Sub Menu\n")
    print("1. Search by Ticket Number\n")
    print("2. Search by Customer Name\n")
    kc = int(input())
    if kc == 1:
        cc = int(input("Enter Ticket number to search "))
        for i in range(sc):
            if cc == customer[i]['number']:
                display(i)
                input("Press Enter to continue...")
                ticket_counter()
    elif kc == 2:
        name = input("Enter Customer name to search ")
        flag = 1
        for i in range(sc):
            if name == customer[i]['name']:
                display(i)
                flag = 0
                input("Press Enter to continue...")
                ticket_counter()

        if flag:
            print("No account with searched Name")
            input("Press Enter to continue...")
            ticket_counter()
    else:
        print("\nInvalid Choice ")
        input("Press Enter to continue...")
        ticket_counter()


def display(i):
    print("\n\n    Ticket no    :{}".format(customer[i]['number']))
    print("    Name           :{}".format(customer[i]['name']))
    print("    Seat            :{}".format(customer[i]['sit']))
    print("    Mobile no      :0{}".format(customer[i]['mobile_no']))
    print("    Road No        :{}".format(customer[i]['roadNo']))
    print("    House No       :{}".format(customer[i]['houseNo']))
    print("    Payable        :{:.2f}".format(customer[i]['payable']))
    print("    Paid           :{:.2f}".format(customer[i]['paid']))
    print("    Returned       :{:.2f}".format(customer[i]['returned']))
    print("    Payment date   :{}/{}/{}".format(customer[i]['pay']['month'],
                                              customer[i]['pay']['day'],
                                              customer[i]['pay']['year']))


def display_booked_seats():
    for i in range(sc):
        print("{}".format(customer[i]['sit']))


def ticket_counter():
    print("MENU\n")
    print("1. Input\n")
    print("2. Search\n")
    print("3. Display All\n")
    print("4. Booked Sits\n")
    hg = int(input())
    if hg == 1:
        input_accounts()
    elif hg == 2:
        search()
    elif hg == 3:
        for i in range(sc):
            display(i)
        input("Press Enter to continue...")
        ticket_counter()
    elif hg == 4:
        display_booked_seats()
        input("Press Enter to continue...")
        ticket_counter()


def dijkstra(G, n, startnode):
    global MAX
    sys.stdout.write("\033c")  # clear console
    cost = [[0 for _ in range(MAX)] for _ in range(MAX)]
    distance = [0] * MAX
    pred = [0] * MAX
    visited = [0] * MAX
    count = mindistance = nextnode = i = j = 0

    for i in range(n):
        for j in range(n):
            if G[i][j] == 0:
                cost[i][j] = INFINITY
            else:
                cost[i][j] = G[i][j]

    for i in range(n):
        distance[i] = cost[startnode][i]
        pred[i] = startnode
        visited[i] = 0

    distance[startnode] = 0
    visited[startnode] = 1
    count = 1

    while count < n - 1:
        mindistance = INFINITY
        for i in range(n):
            if distance[i] < mindistance and not visited[i]:
                mindistance = distance[i]
                nextnode = i

        visited[nextnode] = 1
        for i in range(n):
            if not visited[i] and mindistance + cost[nextnode][i] < distance[i]:
                distance[i] = mindistance + cost[nextnode][i]
                pred[i] = nextnode

    a = [['R', 'A', 'N'], ['M', 'Y', 'M'], ['S', 'Y', 'L'], ['R', 'A', 'J'], ['D', 'H', 'K'], ['K', 'H', 'L'],
         ['B', 'A', 'R'], ['C', 'T', 'G']]

    for i in range(n):
        if i != startnode:
            temp1 = temp2 = i
            k = 0
            sys.stdout.write("\n{}=".format(distance[temp2]))
            while k < 3:
                sys.stdout.write(a[i][k])
                k += 1

            j = i
            while j != startnode:
                j = pred[j]
                sys.stdout.write("<-")
                k = 0
                while k < 3:
                    sys.stdout.write(a[j][k])
                    k += 1


def route_visualization():
    global MAX
    G = [[0 for _ in range(MAX)] for _ in range(MAX)]
    n = 8
    u = 0

    G[0][0] = 0
    G[0][1] = 292
    G[0][2] = 503
    G[0][3] = 211
    G[0][4] = 298
    G[0][5] = 395
    G[0][6] = 466
    G[0][7] = 546

    G[1][0] = 292
    G[1][1] = 0
    G[1][2] = 191
    G[1][3] = 239
    G[1][4] = 110
    G[1][5] = 330
    G[1][6] = 291
    G[1][7] = 357

    G[2][0] = 503
    G[2][1] = 191
    G[2][2] = 0
    G[2][3] = 448
    G[2][4] = 235
    G[2][5] = 440
    G[2][6] = 402
    G[2][7] = 358

    G[3][0] = 211
    G[3][1] = 239
    G[3][2] = 448
    G[3][3] = 0
    G[3][4] = 243
    G[3][5] = 266
    G[3][6] = 337
    G[3][7] = 491

    G[4][0] = 298
    G[4][1] = 110
    G[4][2] = 235
    G[4][3] = 243
    G[4][4] = 0
    G[4][5] = 221
    G[4][6] = 182
    G[4][7] = 248

    G[5][0] = 395
    G[5][1] = 330
    G[5][2] = 440
    G[5][3] = 266
    G[5][4] = 221
    G[5][5] = 0
    G[5][6] = 144
    G[5][7] = 348

    G[6][0] = 466
    G[6][1] = 291
    G[6][2] = 402
    G[6][3] = 337
    G[6][4] = 182
    G[6][5] = 144
    G[6][6] = 0
    G[6][7] = 238

    G[7][0] = 546
    G[7][1] = 357
    G[7][2] = 358
    G[7][3] = 491
    G[7][4] = 248
    G[7][5] = 348
    G[7][6] = 238
    G[7][7] = 0

    print(" ---------------------------------------")
    print("|  0.Rangpur")
    print("|  1.Mymensingh")
    print("|  2.Sylhet")
    print("|  3.Rajshahi")
    print("|  4.Dhaka")
    print("|  5.Khulna")
    print("|  6.Barisal")
    print("|  7.Chittagong")
    print(" ---------------------------------------")
    u = int(input("Enter Current Location: "))
    dijkstra(G, n, u)
    input("Press Enter to continue...")
    main()


def dijkstra_drive_assist(G, n, startnode):
    global MAX, ue5
    sys.stdout.write("\033c")  # clear console
    cost = [[0 for _ in range(MAX)] for _ in range(MAX)]
    distance = [0] * MAX
    pred = [0] * MAX
    visited = [0] * MAX
    count = mindistance = nextnode = i = j = 0
    for i in range(n):
        for j in range(n):
            if G[i][j] == 0:
                cost[i][j] = INFINITY
            else:
                cost[i][j] = G[i][j]
    for i in range(n):
        distance[i] = cost[startnode][i]
        pred[i] = startnode
        visited[i] = 0
    distance[startnode] = 0
    visited[startnode] = 1
    count = 1
    while count < n - 1:
        mindistance = INFINITY
        for i in range(n):
            if distance[i] < mindistance and not visited[i]:
                mindistance = distance[i]
                nextnode = i
        visited[nextnode] = 1
        for i in range(n):
            if not visited[i] and mindistance + cost[nextnode][i] < distance[i]:
                distance[i] = mindistance + cost[nextnode][i]
                pred[i] = nextnode

    a = [['R', 'A', 'N'], ['M', 'Y', 'M'], ['S', 'Y', 'L'], ['R', 'A', 'J'], ['D', 'H', 'K'], ['K', 'H', 'L'],
         ['B', 'A', 'R'], ['C', 'T', 'G']]

    for i in range(n):
        if i != startnode:
            temp1 = temp2 = i
            k = 0
            if i == ue5:
                sys.stdout.write("\n{}=".format(distance[temp2]))
                while k < 3:
                    sys.stdout.write(a[i][k])
                    k += 1

                j = i
                while j != startnode:
                    j = pred[j]
                    sys.stdout.write("<-")
                    k = 0
                    while k < 3:
                        sys.stdout.write(a[j][k])
                        k += 1


def drive_assist():
    global MAX, ue5
    G = [[0 for _ in range(MAX)] for _ in range(MAX)]
    n = 8
    u1 = 0

    G[0][0] = 0
    G[0][1] = 292
    G[0][2] = 503
    G[0][3] = 211
    G[0][4] = 298
    G[0][5] = 395
    G[0][6] = 466
    G[0][7] = 546

    G[1][0] = 292
    G[1][1] = 0
    G[1][2] = 191
    G[1][3] = 239
    G[1][4] = 110
    G[1][5] = 330
    G[1][6] = 291
    G[1][7] = 357

    G[2][0] = 503
    G[2][1] = 191
    G[2][2] = 0
    G[2][3] = 448
    G[2][4] = 235
    G[2][5] = 440
    G[2][6] = 402
    G[2][7] = 358

    G[3][0] = 211
    G[3][1] = 239
    G[3][2] = 448
    G[3][3] = 0
    G[3][4] = 243
    G[3][5] = 266
    G[3][6] = 337
    G[3][7] = 491

    G[4][0] = 298
    G[4][1] = 110
    G[4][2] = 235
    G[4][3] = 243
    G[4][4] = 0
    G[4][5] = 221
    G[4][6] = 182
    G[4][7] = 248

    G[5][0] = 395
    G[5][1] = 330
    G[5][2] = 440
    G[5][3] = 266
    G[5][4] = 221
    G[5][5] = 0
    G[5][6] = 144
    G[5][7] = 348

    G[6][0] = 466
    G[6][1] = 291
    G[6][2] = 402
    G[6][3] = 337
    G[6][4] = 182
    G[6][5] = 144
    G[6][6] = 0
    G[6][7] = 238

    G[7][0] = 546
    G[7][1] = 357
    G[7][2] = 358
    G[7][3] = 491
    G[7][4] = 248
    G[7][5] = 348
    G[7][6] = 238
    G[7][7] = 0

    print(" ---------------------------------------")
    print("|  0.Rangpur")
    print("|  1.Mymensingh")
    print("|  2.Sylhet")
    print("|  3.Rajshahi")
    print("|  4.Dhaka")
    print("|  5.Khulna")
    print("|  6.Barisal")
    print("|  7.Chittagong")
    print(" ---------------------------------------")
    u1 = int(input("Enter Current Location: "))
    ue5 = int(input("Enter Destined Location: "))
    dijkstra_drive_assist(G, n, u1)
    input("Press Enter to continue...")
    main()


def dijkstra_route_visualization(G, n, startnode):
    sys.stdout.write("\033c")  # clear console
    cost = [[0 for _ in range(MAX)] for _ in range(MAX)]
    distance = [0] * MAX
    pred = [0] * MAX
    visited = [0] * MAX
    count = mindistance = nextnode = i = j = 0
    for i in range(n):
        for j in range(n):
            if G[i][j] == 0:
                cost[i][j] = INFINITY
            else:
                cost[i][j] = G[i][j]
    for i in range(n):
        distance[i] = cost[startnode][i]
        pred[i] = startnode
        visited[i] = 0
    distance[startnode] = 0
    visited[startnode] = 1
    count = 1
    while count < n - 1:
        mindistance = INFINITY
        for i in range(n):
            if distance[i] < mindistance and not visited[i]:
                mindistance = distance[i]
                nextnode = i
        visited[nextnode] = 1
        for i in range(n):
            if not visited[i] and mindistance + cost[nextnode][i] < distance[i]:
                distance[i] = mindistance + cost[nextnode][i]
                pred[i] = nextnode

    a = [['R', 'A', 'N'], ['M', 'Y', 'M'], ['S', 'Y', 'L'], ['R', 'A', 'J'], ['D', 'H', 'K'], ['K', 'H', 'L'],
         ['B', 'A', 'R'], ['C', 'T', 'G']]

    for i in range(n):
        if i != startnode:
            temp1 = temp2 = i
            k = 0
            sys.stdout.write("\n{}=".format(distance[temp2]))
            while k < 3:
                sys.stdout.write(a[i][k])
                k += 1

            j = i
            while j != startnode:
                j = pred[j]
                sys.stdout.write("<-")
                k = 0
                while k < 3:
                    sys.stdout.write(a[j][k])
                    k += 1


def route_visualization():
    G = [[0 for _ in range(MAX)] for _ in range(MAX)]
    n = 8
    u = 0

    G[0][0] = 0
    G[0][1] = 292
    G[0][2] = 503
    G[0][3] = 211
    G[0][4] = 298
    G[0][5] = 395
    G[0][6] = 466
    G[0][7] = 546

    G[1][0] = 292
    G[1][1] = 0
    G[1][2] = 191
    G[1][3] = 239
    G[1][4] = 110
    G[1][5] = 330
    G[1][6] = 291
    G[1][7] = 357

    G[2][0] = 503
    G[2][1] = 191
    G[2][2] = 0
    G[2][3] = 448
    G[2][4] = 235
    G[2][5] = 440
    G[2][6] = 402
    G[2][7] = 358

    G[3][0] = 211
    G[3][1] = 239
    G[3][2] = 448
    G[3][3] = 0
    G[3][4] = 243
    G[3][5] = 266
    G[3][6] = 337
    G[3][7] = 491

    G[4][0] = 298
    G[4][1] = 110
    G[4][2] = 235
    G[4][3] = 243
    G[4][4] = 0
    G[4][5] = 221
    G[4][6] = 182
    G[4][7] = 248

    G[5][0] = 395
    G[5][1] = 330
    G[5][2] = 440
    G[5][3] = 266
    G[5][4] = 221
    G[5][5] = 0
    G[5][6] = 144
    G[5][7] = 348

    G[6][0] = 466
    G[6][1] = 291
    G[6][2] = 402
    G[6][3] = 337
    G[6][4] = 182
    G[6][5] = 144
    G[6][6] = 0
    G[6][7] = 238

    G[7][0] = 546
    G[7][1] = 357
    G[7][2] = 358
    G[7][3] = 491
    G[7][4] = 248
    G[7][5] = 348
    G[7][6] = 238
    G[7][7] = 0

    print(" ---------------------------------------")
    print("|  0.Rangpur")
    print("|  1.Mymensingh")
    print("|  2.Sylhet")
    print("|  3.Rajshahi")
    print("|  4.Dhaka")
    print("|  5.Khulna")
    print("|  6.Barisal")
    print("|  7.Chittagong")
    print(" ---------------------------------------")
    u = int(input("Enter Current Location: "))
    dijkstra_route_visualization(G, n, u)
    input("Press Enter to continue...")
    main()


def drive_assist_visualization():
    global MAX, ue5
    G = [[0 for _ in range(MAX)] for _ in range(MAX)]
    n = 8
    u1 = 0

    G[0][0] = 0
    G[0][1] = 292
    G[0][2] = 503
    G[0][3] = 211
    G[0][4] = 298
    G[0][5] = 395
    G[0][6] = 466
    G[0][7] = 546

    G[1][0] = 292
    G[1][1] = 0
    G[1][2] = 191
    G[1][3] = 239
    G[1][4] = 110
    G[1][5] = 330
    G[1][6] = 291
    G[1][7] = 357

    G[2][0] = 503
    G[2][1] = 191
    G[2][2] = 0
    G[2][3] = 448
    G[2][4] = 235
    G[2][5] = 440
    G[2][6] = 402
    G[2][7] = 358

    G[3][0] = 211
    G[3][1] = 239
    G[3][2] = 448
    G[3][3] = 0
    G[3][4] = 243
    G[3][5] = 266
    G[3][6] = 337
    G[3][7] = 491

    G[4][0] = 298
    G[4][1] = 110
    G[4][2] = 235
    G[4][3] = 243
    G[4][4] = 0
    G[4][5] = 221
    G[4][6] = 182
    G[4][7] = 248

    G[5][0] = 395
    G[5][1] = 330
    G[5][2] = 440
    G[5][3] = 266
    G[5][4] = 221
    G[5][5] = 0
    G[5][6] = 144
    G[5][7] = 348

    G[6][0] = 466
    G[6][1] = 291
    G[6][2] = 402
    G[6][3] = 337
    G[6][4] = 182
    G[6][5] = 144
    G[6][6] = 0
    G[6][7] = 238

    G[7][0] = 546
    G[7][1] = 357
    G[7][2] = 358
    G[7][3] = 491
    G[7][4] = 248
    G[7][5] = 348
    G[7][6] = 238
    G[7][7] = 0

    print(" ---------------------------------------")
    print("|  0.Rangpur")
    print("|  1.Mymensingh")
    print("|  2.Sylhet")
    print("|  3.Rajshahi")
    print("|  4.Dhaka")
    print("|  5.Khulna")
    print("|  6.Barisal")
    print("|  7.Chittagong")
    print(" ---------------------------------------")
    u1 = int(input("Enter Current Location: "))
    ue5 = int(input("Enter Destined Location: "))
    dijkstra_drive_assist(G, n, u1)
    input("Press Enter to continue...")
    main()


def main():
    sys.stdout.write("\033c")  # clear console
    print(" -----------------------------------------------------------------------")
    print("|                      Welcome to the Smart City                        |")
    print(" -----------------------------------------------------------------------")
    print("| 1. Route Visualization                                               |")
    print("| 2. Drive Assist & Visualization                                      |")
    print("| 3. Route Visualization with Drive Assist                             |")
    print("| 4. Exit                                                               |")
    print(" -----------------------------------------------------------------------")

    choice = int(input("Choose the option(1/2/3/4): "))

    if choice == 1:
        route_visualization()
    elif choice == 2:
        drive_assist_visualization()
    elif choice == 3:
        sys.stdout.write("\033c")  # clear console
        route_visualization()
        input("\n\nPress Enter to continue...")
        drive_assist_visualization()
    elif choice == 4:
        sys.exit()
    else:
        print("Invalid Input. Please enter a valid option.")
        input("Press Enter to continue...")
        main()


if __name__ == "__main__":
    main()
