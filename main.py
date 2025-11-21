def open_file():
    ''' Remember the docstring'''
    while True:
        file_name = input("\nEnter a filename: ")
        try:
            fp = open(file_name, 'r')
            return fp 
        except FileNotFoundError:
            print("\nError in filename.")
            continue 


def read_file(fp):
    network = []
    is_first_line = True

    for line in fp:
        line = line.strip()

        if is_first_line:
            n = int(line)
            #network = [[] for i in range(n)]
            for i in range(n):
                network.append([])
            is_first_line = False
        else:
            u, v = [], []
            for x in line.split():
                u.append(int(x))
            
            if len(u) == 2:
                u, v = u[0], u[1]
            network[u].append(v)
            network[v].append(u)

    return network

def num_in_common_between_lists(list1, list2):
    common_num = 0
    for i in list1:
        for j in list2:
            if i == j:
                common_num += 1
    
    return common_num


def calc_similarity_scores(network):
    ''' Remember the docstring'''
    n = len(network)
    similarity_matrix = []
    for var in range(n):
        similarity_matrix.append(n*[0])
    
    for i in range(n):
        for j in range(n):
            num_in_common = num_in_common_between_lists(network[i], network[j])
            similarity_matrix[i][j] = num_in_common
            similarity_matrix[j][i] = num_in_common
    
    return similarity_matrix



def recommend(user_id, network, similarity_matrix):
    similarity_scores = similarity_matrix[user_id]
    similarity_scores[user_id] = -1
    current_friends = network[user_id]
    
    for friend_id in current_friends:
        similarity_scores[friend_id] = -1

    max_similarity = max(similarity_scores)
    
    if max_similarity == -1:
        return None

    recommended_user = similarity_scores.index(max_similarity)

    return recommended_user

def main():
    print("Facebook friend recommendation.\n")
    fp = open_file()
    network = read_file(fp)
    similarity_matrix = calc_similarity_scores(network)
    end_game = ''
    while end_game.lower() != 'no':
        while True:
            user_id = input("\nEnter an integer in the range 0 to {}:".format(len(network) - 1))
            try:
                user_id = int(user_id)
                if user_id >= len(network) or user_id < 0:
                    print("\nError: input must be an int between 0 and {}".format(len(network) - 1))
                    continue
                break
            except ValueError:
                print("\nError: input must be an int between 0 and {}".format(len(network) - 1))

        recommended_friend = recommend(user_id, network, similarity_matrix)
        print("\nThe suggested friend for {} is {}".format(user_id,recommended_friend))
        end_game = input("\nDo you want to continue (yes/no)? ")

main()
    
