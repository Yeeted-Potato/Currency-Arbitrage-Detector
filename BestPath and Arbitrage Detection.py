import math
#able to use log

import freecurrencyapi
#able to use the api
client = freecurrencyapi.Client('fca_live_PrujDJNkPUxquOkrpmlkPK48sqbLXuktGonBfZ0Q')
#My client key

#Choice function so users can choose between test exchange rate graph and live api currencies
def choice():
    while True:
        #Set loop
        answer = (input("Type 1 for test exchange rate graph, 2 for choosing with live api currencies\n"))
        try:
            answer = int(answer)
            #try converting to an int
        except ValueError:
            print("\nError: Enter a whole number between 1 and 2\n")
            continue
            #if error print error msg and retry
        if answer == 1 or answer == 2:
            return answer
        #if answer is 1 or 2 return value
        else:
            print("\nError: Enter a whole number between 1 and 2\n")
    #print error msg and retry

def user_amount():
    #Get the amount of currencies the user wants to select
    global user_total_currencies
    #make it a global variable
    while True:
        #set loop
        user_total_currencies = (
        input("Enter the amount of currencies you wish to select (Within 5 - 8)\n"))
        # Ask user for how many currencies
        try:
            user_total_currencies = int(user_total_currencies)
            #Try convert to a int
        except ValueError:
            print("Error: enter a whole number within the range 5 - 8")
            #if not an int print error msg and retry
            continue
        if(user_total_currencies >= 5 and user_total_currencies <= 8):
            print(f"You have selected to choose {user_total_currencies} different currencies")
            return user_total_currencies
        #if within range return value
        else:
            print("Error, Please Enter a number between 5 and 8")
            #if not within range print error

def user():
    #function to get user currencies
    global user_input
    valid_currencies = ['EUR', 'USD', 'JPY', 'RUB', 'AUD', 'CAD', 'NZD', 'HKD']
    #set valid currencies
    while True:
        #set loop
        print(
            f"Choose {user_total_currencies} from {valid_currencies}")
        # print choice of currencies
        try:
            string_input = input(
            str("Make sure to spell correctly e.g. EUR, and leave a comma after each one (except the last currency)!\n"))
            # get choice of currencies
        except ValueError:
            print(f"\nError: Choose {user_total_currencies} currencies (e.g EUR, USD)\n")
            #if not a str print error msg
        user_input = string_input.split(',')  # split the inputs by comma
        user_input = [i.strip(' ') for i in user_input]  # Remove Whitespace
        user_input = [i.upper() for i in user_input]  # Make everything uppercase
        if len(user_input) != user_total_currencies:
            print(f"\nError: Please select a total of {user_total_currencies} currencies\n")
            continue
            #if the amount of currencies is not equal to original value
        if any(currency not in valid_currencies for currency in user_input):
                print("Spelling Error: Please spell correctly, for example, EUR")
                continue
            #if currency entered doesn't match list, error
        print(f"You have selected: {user_input[:]}")
        return user_input

def source_currency(user_input, user_total_currencies):
    #get base and target currency
    while True:
        try:
            source = int(
                input(f"Enter source currency index, e.g {user_input[0]} index = 0, {user_input[1]} index = 1\n"))
            target = int(
                input(f"Enter target currency index, e.g {user_input[0]} index = 0, {user_input[1]} index = 1\n"))
            #Try these as ints if not then print error msg and retry
        except ValueError:
            print(f"Error: Enter a whole number within the range 0 - {user_total_currencies - 1}")
            continue
        if source == target:
            print("Error: Source and Target cannot be the same")
            continue
            #if the source and target are the same print error msg and retry
#if the source of target are out of range print error msg and retry
        if source < 0 or source > user_total_currencies - 1:
            print("Error: Source currency index out of range")
        if target < 0 or target > user_total_currencies - 1:
            print("Error: Target currency index out of range")
        return source, target

def get_currency():
    #Get currency from the api
    global current
    current = {}
    for currency in user_input:
        result = client.latest(base_currency=currency, currencies=user_input)
        #Result comes in a dictionary so we create a list to store it in
        current[currency] = result["data"]
        #set currency to a list
    return current
#return currency list

#this is for test cases for the user to manually enter currency rates
def user_graph():
    while True:
        #set loop and ask for total currencies
        user_total_currencies = input("Input total Number of currencies (5 - 8): \n")
        try:
            user_total_currencies = int(user_total_currencies)
            #try as int if error, then print error msg and retry
        except ValueError:
            print("Error: Enter a whole number")
            continue
        if (user_total_currencies >= 5 and user_total_currencies <= 8):
            print(f"You have selected to choose {user_total_currencies} different currencies")
            break
            #if within range break loop
        else:
            print("Error, Please Enter a number between 5 and 8")
        # print error if input out of range

    user_input = []
    while True:
        #enter user currencies check if theyre string
        try:
            str_input = str(input(f"Please enter {user_total_currencies} currency labels with a comma after each one: \n"))
        except ValueError:
            print(f"\nError: Choose {user_total_currencies} currencies\n")
            #print error msg if not a string
        user_input = str_input.split(',')  # split the inputs by comma
        user_input = [i.strip(' ') for i in user_input]  # Remove Whitespace
        user_input = [i.upper() for i in user_input]  # Make everything uppercase
        if len(user_input) != user_total_currencies:
            print(f"\nError: Please select a total of {user_total_currencies} currencies\n")
            continue
            #if length of currencies are not equal to total currencies they entered print error msg and retry
        for i in range(user_total_currencies):
            if user_input[i] == '':
                print("Error: empty currency name")
                continue
        else:
            break

    currency_exchange_graph = [['inf'] * user_total_currencies for i in range(user_total_currencies)]
    #create currency exchange graph
    for i in range(user_total_currencies):
        while True:
            #set loop and ask for exchange rates
            holding = []
            try:
                hold = input(f"Enter first row of {user_total_currencies} exchange rates for [{user_input[i]}] (Separate via Commas):\n")
                holding = [float(item.strip()) for item in hold.split(",")]
                #so ask for input and convert to float and store in holding list
                if len(holding) != user_total_currencies:
                    print(f" Please enter a total of {user_total_currencies} numbers.")
                    continue
                    #if the amount is differnt print error msg and retry
                if any(item <= 0 for item in holding):
                    print("Exchange rates cannot be 0 or negative")
                    continue
                    #if items are negative or 0 error
                break
            except ValueError:
                print("Please enter numbers only")
                #only floats allowed
        for j in range(user_total_currencies):
            currency_exchange_graph[i][j] = holding[j]
            #set exchange rate to holding list
    initial_log_graph = [row[:] for row in currency_exchange_graph]
    #copy currency exchange graph to initial log graph
    for i in range(user_total_currencies):
        for j in range(user_total_currencies):
            initial_log_graph[i][j] = -math.log(currency_exchange_graph[i][j])
            #make all values in initial log graph negative logs

    print(user_input)
    #ask for source and target currencies
    while True:
        try:
            source = int(input(f"Enter source currency index, e.g {user_input[0]} index = 0, {user_input[1]} index = 1\n"))
            target = int(input(f"Enter target currency index, e.g {user_input[0]} index = 0, {user_input[1]} index = 1\n"))
            #ask for int input
        except ValueError:
            print(f"Error: Enter a whole number within the range 0 - {user_total_currencies - 1}")
            continue
            #if not int error msg
        if source == target:
            print("Error: Source and Target cannot be the same")
            continue
            #if source and target are the same error msg
        if source < 0 or source > user_total_currencies - 1:
            print("Error: Source currency index out of range")
        if target < 0 or target > user_total_currencies - 1:
            print("Error: Target currency index out of range")
        break
    return currency_exchange_graph, initial_log_graph, user_input, user_total_currencies, source, target

def graph_create():
    #create currency exchange graph
    global graph, log_graph, paths
    graph = [[float('inf')] * user_total_currencies for _ in range(user_total_currencies)]
    #create graph with infinity values
    for i in range(user_total_currencies):
        for j in range(user_total_currencies):
            if i == j:
                graph[i][j] = 1
            #if source and target are the same set the exchange rate to 1

            else:
                base_currency = user_input[i]
                conversions = user_input[j]
                graph[i][j] = current[base_currency][conversions]
                #set the value to the conversion rate of the correct currency
    for i in range(user_total_currencies):
        for j in range(user_total_currencies):
            if i != j:
                graph[i][j] = graph[i][j]*0.97
                #give a 3% commission on all rates to simulate transaction fees
    log_graph = [row[:] for row in graph]
    #set duplicate of graph to log_graph
    for i in range(user_total_currencies):
        for j in range(user_total_currencies):
                log_graph[i][j] = -math.log(graph[i][j])
            #convert every exchange rate to log
    return log_graph, graph

def floyd_warshall(log_graph, user_total_currencies, currency_exchange_graph):
    #Function to find shortest path through graph
    negative_cycle_nodes = []
    Next = [[None] * user_total_currencies for _ in range(user_total_currencies)]
    #create matrix for next graph
    for i in range(user_total_currencies):
        for j in range(user_total_currencies):
            if currency_exchange_graph[i][j] != float('inf'):
                Next[i][j] = j
                #check if currency exchange graph values are infinity, if not then set the value to the target currency
            else:
                Next[i][j] = None
    for k in range(user_total_currencies):
        for i in range(user_total_currencies):
            for j in range(user_total_currencies):
                #create loop for each node and if going thru intermediary node is shorter than going from source to target set the exchange rate to the smaller exchange rate
                if round(log_graph[i][j], 9) > round(log_graph[i][k] + log_graph[k][j], 9):
                    log_graph[i][j] = log_graph[i][k] + log_graph[k][j]
                    Next[i][j] = Next[i][k]
        #set the updated graph to the original graph
    for i in range(user_total_currencies):
        if round(log_graph[i][i], 9) < 0:
            #if each currency to itself is less that 0, then it has arbitrage
             negative_cycle_nodes.append(i)
            #add node to list of nodes with arbitrage
    return log_graph, negative_cycle_nodes, Next

def convert_back(graph, n):
    return [[math.exp(-graph[i][j]) for j in range(n)] for i in range(n)]
#convert back to currency exchange graph by taking the exponential of the negative logs for each edge

def print_graph(user_input, total_currencies, currency_exchange_graph, initial_log_graph, distances, final_currency_exchange_graph, negative_cycles):
    #function to print graphs
    print("\nCurrency Exchange Graph")
    print(" " * 4, end="")
    #print 4 spaces at the beginning
    for currency in user_input:
        #for each currency in the user input
        print(f"{currency:>15}", end="")
        #print each currency within a 15 space column being set to the right
    print()
    #print a line


    for i in range(total_currencies):
        print(f"{user_input[i]:>4}", end="")
        #print each currency name within a 4 space column being set to the right
        for j in range(total_currencies):
            print(f"{currency_exchange_graph[i][j]:15.9f}", end="")
            #print each currency rate within a 15 space column and have 9 decimal places
        print()

    print("\nInitial Negative Log Graph")
    print(" " * 4, end="")
    #print 4 spaces at the beginning
    for currency in user_input:
        print(f"{currency:>15}", end="")
        #print each currency within a 15 space column being set to the right
    print()
    for i in range(total_currencies):
        print(f"{user_input[i]:>4}", end="")
        # print each currency name within a 4 space column being set to the right
        for j in range(total_currencies):
            print(f"{initial_log_graph[i][j]:15.9f}", end="")
            #print each currency rate within a 15 space column and have 9 decimal places
        print()

    print("\nFinal Negative Log Graph")
    print(" " * 4, end="")
    #print 4 spaces at the beginning
    for currency in user_input:
        print(f"{currency:>15}", end="")
        #print each currency within a 15 space column being set to the right
    print()

    for i in range(total_currencies):
        print(f"{user_input[i]:>4}", end="")
        # print each currency name within a 4 space column being set to the right
        for j in range(total_currencies):
            print(f"{distances[i][j]:15.9f}", end="")
            #print each currency rate within a 15 space column and have 9 decimal places
        print()

    print("\nFinal Currency Exchange Graph")
    print(" " * 4, end="")
    # print 4 spaces at the beginning
    for currency in user_input:
        print(f"{currency:>17}", end="")
        # print each currency within a 17 space column being set to the right
    print()

    for i in range(total_currencies):
        print(f"{user_input[i]:>6}", end="")
        # print each currency name within a 6 space column being set to the right
        for j in range(total_currencies):
            print(f"{final_currency_exchange_graph[i][j]:17.9f}", end="")
            # print each currency rate within a 17 space column and have 9 decimal places
        print()
    print()

#for finding negative cycles and shortest paths
def path_reconstruction(source, target, Next):
    path = []
    visited = []
    current = source
    #create path and visited list and set current to source

    if Next[source][target] == None:
        return []
    #if there is not path then return empty list

    if source == target:
        #if we are trying to find negative cycle
        while current not in visited:
            #while current is not in visited list, append current to visited list and set current to next node in path
            visited.append(current)
            path.append(current)
            current = Next[current][target]
        path.append(current)
        return path

    else:
        while current not in visited:
            #while current is not in visited list, append current to visited list and set current to next node in path
            visited.append(current)
            path.append(current)
            if current == target:
                break
            current = Next[current][target]
        #path.append(target)
        return path

def main():
    answer = choice()
    #this is for asking the user whether they want to use api currencies or manually enter currency rates
    negative_cycles = [[]]

    #this is for manually entering currency rates
    if answer == 1:
        #call all these functions and store in variables
        currency_exchange_graph, initial_log_graph, user_input, user_total_currencies, source, target = user_graph()
        initial_log_graph_real = [row[:] for row in initial_log_graph]
        shortest_log, negative_nodes, Next = floyd_warshall(initial_log_graph, user_total_currencies, currency_exchange_graph)
        final_currency_exchange_graph = convert_back(shortest_log, user_total_currencies)
        print_graph(user_input, user_total_currencies, currency_exchange_graph, initial_log_graph_real, shortest_log, final_currency_exchange_graph, negative_cycles)

        #if there are nodes that have negative paths then arbitrage is detected
        if negative_nodes != []:
            print("Arbitrage Detected")
            for node in negative_nodes:
                path = path_reconstruction(node, node, Next)
                #for every negative node, find a negative cycle
                if path[0] == path[-1]:
                    print("Arbitrage Cycle: " + " -> ".join(user_input[i] for i in path))
                    profit = 1.0
                    #print the cycle and find profit
                    for i in range(len(path) - 1):
                        profit *= currency_exchange_graph[path[i]][path[i + 1]]
                    print(f"Total Profit: {(profit - 1) * 100}%")
        else:
            print("No Arbitrage Detected")
            path = path_reconstruction(source, target, Next)
            rate = 1.0
            #if no negative nodes, arbitrage is not there and find shortest path
            for i in range(len(path) - 1):
                rate *= currency_exchange_graph[path[i]][path[i + 1]]
                #find the best rate for the path
            print(f"Best Conversion Rate from {user_input[source]} -> {user_input[target]} = {rate}")
            print("Best Path: " + " -> ".join(user_input[i] for i in path))
            #print best rate and path
    #for using api currencies
    elif answer == 2:
        user_total_currencies = user_amount()
        user_input = user()
        #call currencies and get currencies from user
        current = get_currency()
        #create matrix for currency conversion
        source, target = source_currency(user_input, user_total_currencies)
        #get and store source and target currency
        log_graph, currency_exchange_graph = graph_create()
        #get log graph
        log_graph_initial = [row[:] for row in log_graph]
        #create duplicate of log graph, store for later
        shortest_log, negative_nodes, Next = floyd_warshall(log_graph_initial, user_total_currencies, currency_exchange_graph)
        #compute floyd warshall algorithm
        final_currency_exchange_graph = convert_back(shortest_log, user_total_currencies)
        print_graph(user_input, user_total_currencies, currency_exchange_graph, log_graph_initial, shortest_log, final_currency_exchange_graph, negative_cycles)
        #print graphs
        if negative_nodes != []:
            print("Arbitrage Detected")
            for node in negative_nodes:
                #find negative cycles if there are negative nodes found
                path = path_reconstruction(node, node, Next)
                if path[0] == path[-1]:
                    print("Arbitrage Cycle: " + " -> ".join(user_input[i] for i in path))
                    profit = 1.0
                    #find profit and print cycle
                    for i in range(len(path) - 1):
                        profit *= final_currency_exchange_graph[path[i]][path[i + 1]]
                    print(f"Total Profit: {(profit - 1) * 100}%")
        else:
            print("No Arbitrage Detected")
            path = path_reconstruction(source, target, Next)
            rate = 1.0
            #if no negative nodes, arbitrage is not there and find shortest path
            for i in range(len(path) - 1):
                rate *= final_currency_exchange_graph[path[i]][path[i + 1]]
                #find the best rate for the path
            print(f"Best Conversion Rate from {user_input[source]} -> {user_input[target]} = {rate}")
            print("Best Path: " + " -> ".join(user_input[i] for i in path))#print best rate and path

if __name__ == "__main__":
    main()
