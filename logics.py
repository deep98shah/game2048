import random

def start_game():
    mat = []
    for _ in range(4):
        mat.append([0 for j in range(4)])
    return mat

def add_new_2(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2

def get_current_state(mat):
    # Check if won
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'Won!'
    
    # Check if game still goes on if 0 is present
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'Game goes on!'
        
    # Check if any consecutive duplicate numbers are present
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] or mat[i][j] == mat[i+1][j]:
                return 'Game goes on!'
    # Check for last row
    for i in range(3):
        if mat[3][i] == mat[3][i+1]:
            return 'Game goes on!'
    
    for j in range(3):
        if mat[j][3] == mat[j+1][3]:
            return 'Game goes on!'
    
    return 'Game over!'

def compress(mat):
    changed = False
    newMat = []
    for _ in range(4):
        newMat.append([0]*4)
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                if pos != j:
                    changed = True
                newMat[i][pos] = mat[i][j]
                pos += 1
    return newMat, changed

def merge(mat):
    changed = False
    # print('before merge')
    # print_mat(mat)
    for i in range(4):
        for j in range(3):
            if (mat[i][j] == mat[i][j+1]) and mat[i][j] != 0:
                changed = True
                mat[i][j] = mat[i][j] * 2
                mat[i][j+1] = 0
    # print('after merge')
    # print_mat(mat)
    return mat, changed

def reverse(mat):
    newMat = []
    for i in range(4):
        newMat.append([])
        for j in range(4):
            newMat[i].append(mat[i][4-j-1])
    return newMat

def transpose(mat):
    newMat = []
    for i in range(4):
        newMat.append([])
        for j in range(4):
            newMat[i].append(mat[j][i])
    return newMat

def move_up(mat):
    #Implement This Function
    mat = transpose(mat)
    mat, changed1 = compress(mat)
    mat, changed2 = merge(mat)
    changed = changed1 or changed2
    mat, _ = compress(mat)
    mat = transpose(mat)
    return mat, changed

def move_down(mat):
    #Implement This Function
    mat = transpose(mat)
    mat = reverse(mat)
    mat, changed1 = compress(mat)
    mat, changed2 = merge(mat)
    changed = changed1 or changed2
    mat, _ = compress(mat)
    mat = reverse(mat)
    mat = transpose(mat)
    return mat, changed

def move_right(mat):
    #Implement This Function
    mat = reverse(mat)
    mat, changed1 = compress(mat)
    mat, changed2 = merge(mat)
    changed = changed1 or changed2
    mat, _ = compress(mat)
    mat = reverse(mat)
    return mat, changed

def move_left(mat):
    #Implement This Function
    mat, changed1 = compress(mat)
    mat, changed2 = merge(mat)
    changed = changed1 or changed2
    mat, _ = compress(mat)
    return mat, changed

def print_mat(mat):
    for i in range(4):
        print(mat[i])

# mat = start_game()
# mat[1][3] = 2
# mat[2][2] = 2
# mat[3][0] = 4
# mat[3][1] = 8
# mat[2][1] = 4
# print_mat(mat)
# elem = int(input())
# while elem != 0:
#     if elem == 1:
#         mat, changed = move_up(mat)
#         if changed:
#             add_new_2(mat)
#     elif elem == 2:
#         mat, changed = move_down(mat)
#         if changed:
#             add_new_2(mat)
#     elif elem == 3:
#         mat, changed = move_left(mat)
#         if changed:
#             add_new_2(mat)
#     elif elem == 4:
#         mat, changed = move_right(mat)
#         if changed:
#             add_new_2(mat)
#     print_mat(mat)
#     currentState = get_current_state(mat)
#     if currentState == 'Won!':
#         print('You\'ve won!')
#     elif currentState == 'Game over!':
#         print(currentState)
#         break
#     elem = int(input())
    
    