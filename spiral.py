#Practice ng coding skills
def spiral(size):
    #Create empty matrix of same size
    out = np.zeros((size, size))

    #Starting position
    row = size//2 - 1 + size % 2 #yung -1+size%2 is just a trick to 
    col = size//2 - 1 + size % 2 # accommodate odd and even sizes
    counter = 1 #yung mismong number sa array
    steps = 1 #steps = ilang steps on current direction bago lumiko
    out[row, col] = counter #assign center value to 1

    #Direction tracker vector: 'right' -> down -> left -> up
    direction = [[0,1], [1,0], [0,-1], [-1,0]]
    dir_index = 0 #tracks direction based sa direction array

    while counter <= size*size:
        for j in range(2): #2 kasi yung pattern ng steps is 1,1,2,2,3,3,4,4,...
            for i in range(steps):
                row += direction[dir_index][0] #iterate row
                col += direction[dir_index][1] #iterate column

                counter += 1
                if counter > size*size: #terminate pag sobra sa max value
                    break

                out[row, col] = counter #store value to correct position

            if dir_index == 3:
                dir_index = 0 #cycle lang balik sa start
            else:
                dir_index += 1
        steps += 1 #iterate level
    print(out)
#spiral(14)
