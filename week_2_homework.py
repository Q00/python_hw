##### gaussian elimination
import sys

#행렬식
def determinant(matrix, mul): 
    width = len(matrix) 
    if width == 1: 
        return mul * matrix[0][0] 
    else: 
        sign = -1 
        sum = 0 
        for i in range(width): 
            m = [] 
            for j in range(1, width): 
                buff = [] 
                for k in range(width): 
                    if k != i: 
                        buff.append(matrix[j][k]) 
                m.append(buff) 
            sign =sign*-1 
            sum =sum +mul*determinant(m, sign * matrix[0][i]) 
        return sum 

def make_matrix():
    row_list = []
    cell_list = []
    try:
        MAX = int(input("행렬 크기를 입력해주세요"))
    except:
        print('값이 옳지 않습니다.')
        sys.exit()

    def check_one(a,b):
        if a == b:
            return 1
        else:
            return 0 
    reverse_matrix = [[check_one(a,b)  for a in range(0, MAX)] for b in range(0, MAX)]
    matrix = []
    for count in range(0, MAX):
        input_list = input(f"{count} 행을 입력해주세요. ex) 1 2 3 ...\n").split()
        if len(input_list) != MAX:
            print('잘못입력하였습니다.')
            return

        matrix.append(list(map(lambda x: int(x),input_list)))
    if len(matrix) != MAX:
        print('잘못입력하였습니다.')
        return

    det = determinant(matrix, 1)
    if det == 0:
        print('해가 없습니다. 가역행렬이 아닙니다.')
        sys.exit()
    def add_rows(matrix, process_count):
        if process_count < MAX:
            if matrix[process_count][process_count] != 0:
                process_count = process_count + 1
                return add_rows(matrix, process_count) 
            else:
                #가역행렬이나 matrix[process_count][process_count]이 0일때는 행을 더해줌
                for l in range(process_count+1, MAX):
                    matrix[process_count] = list(map(lambda x,y: x+y, matrix[process_count],matrix[l]))
                    reverse_matrix[process_count] = list(map(lambda x,y: x+y, reverse_matrix[process_count],reverse_matrix[l]))
                process_count = process_count+1
                return add_rows(matrix, process_count)
        else:
            return matrix
    add_rows(matrix,0)
     
    # process_count 는 cell의 인덱스
    def process(matrix, row_index, process_count):
        try: 
            if matrix[process_count][process_count] != 1:
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
                    temp_list = list(map(lambda x:float(x*devide), matrix[process_count]))
                    temp_reverse_list = list(map(lambda x: float(x*devide), reverse_matrix[process_count]))
                    process_list = list(map(lambda x,y : x-y, matrix[row_index], temp_list))
                    process_reverse_list = list(map(lambda x,y : x-y, reverse_matrix[row_index], temp_reverse_list))

                    matrix[row_index] = process_list
                    reverse_matrix[row_index] = process_reverse_list
                    
                    return process(matrix, row_index+1, process_count)
                else:
                    return process(matrix, row_index+1, process_count)
                
            else:
                process_count = process_count + 1
                if process_count == MAX:
                    return matrix

                return process(matrix, process_count, process_count)
        except ZeroDivisionError as e:
            print(e)
            sys.exit()

        

    process(matrix, 0,0)
    zip_reverse_matrix = [ list(a) for a in zip(*reverse_matrix)]
    #print(zip_reverse_matrix)
    
    # 연립방정식 해 구하기
    final_matrix = []
    ans = [] 
    def simultaneous(key, process, ans):
        if abs(key)<=MAX:
            if len(ans) ==0:
                ans.append(float(zip_reverse_matrix[process][-key]))
            else:
                temp = list(reversed(matrix[-key]))
                k = 0
                for v in ans:
                    temp[k] = float(temp[k]*v)
                    k = k+1
                sum_simul = zip_reverse_matrix[process][-key] 
                #print('@@@@@@@@',sum_simul)
                for index in range(0,k):
                    sum_simul = sum_simul-temp[index]
                ans.append(sum_simul)
            key = key + 1
            #print(ans)
            
        else:
            process = process + 1
            key = 1 
            final_matrix.append(ans[::-1])
            ans = []
            if process ==  MAX:
                #print('finish')
                return
            
        return simultaneous(key, process, ans)

    simultaneous(1,0, ans)
    #print([a for a in zip(*final_matrix)])
    for alist in list(zip(*final_matrix)):
        for a in alist:
            print('%8.3f' % a, end= '')
        print()

            

make_matrix()



