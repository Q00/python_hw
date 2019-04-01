def make_matrix():
    row_list = []
    cell_list = []
    MAX = int(input("행렬 크기를 입력해주세요"))
   
    def check_one(a,b):
        if a == b:
            return 1
        else:
            return 0 
    reverse_matrix = [[check_one(a,b)  for a in range(0, MAX)] for b in range(0, MAX)]
    print(reverse_matrix)
    matrix = []
    for count in range(0, MAX):
        input_list = input(f"{count} 행을 입력해주세요. ex) 1 2 3 ...\n").split()
        matrix.append(list(map(lambda x: int(x),input_list)))
    if len(matrix) != MAX:
        print('잘못입력하였습니다.')
        return
    print(matrix)
    # process_count 는 cell의 인덱스
    def process(matrix, row_index, process_count):
    
        if matrix[process_count][process_count] != 1:
            print('이상은',process_count)
            devide = matrix[process_count][process_count]
            matrix[process_count] = list(map(lambda x: float(x/devide), matrix[process_count]))
            reverse_matrix[process_count] = list(map(lambda x: float(x/devide), reverse_matrix[process_count]))
            return process(matrix, process_count+1, process_count)
        else:
            if process_count == row_index:
                row_index = row_index + 1
    
        if row_index < MAX:
            if matrix[row_index][process_count] != 0:

                devide = float(matrix[row_index][process_count] / matrix[process_count][process_count])
                print('devide : ',devide)
                temp_list = list(map(lambda x:float(x*devide), matrix[process_count]))
                print('templist')
                print(temp_list)
                temp_reverse_list = list(map(lambda x: float(x*devide), reverse_matrix[process_count]))
                print('row_index', row_index)
                print(matrix[row_index])
                process_list = list(map(lambda x,y : x-y, matrix[row_index], temp_list))
                process_reverse_list = list(map(lambda x,y : x-y, reverse_matrix[row_index], temp_reverse_list))

                matrix[row_index] = process_list
                reverse_matrix[row_index] = process_reverse_list
                print(temp_reverse_list)
                print(process_list)

                print(matrix)
                print(reverse_matrix)
                
                return process(matrix, row_index+1, process_count)
            else:
                return process(matrix, row_index+1, process_count)
            
        else:
            process_count = process_count + 1
            if process_count == MAX:
                return matrix

            return process(matrix, process_count, process_count)
        

    process(matrix, 0,0)
    print(matrix)
    print(len(zip(*matrix)))
    
    



make_matrix()



