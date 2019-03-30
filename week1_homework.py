import math
#카드 개수 받아서 제곱해서 값 구해주는 함수
# 앞에있는 숫자 - 1 : 1의 개수( 1이 얼마나 더해지냐)
# 앞에있는 숫자 + 1 : 더해지는 값
def makeCard():
    count :int = int(input("카드 개수를 정해주세요~"))
    final = pow(2, count) -1
    card_list = []
    #결과 값 합산
    res = []
    for a in range(0, count):
        #카드 값 리스트
        card_value_list = []
        
        first = pow(2, a)
        one_count = first -1
        _count = first +1
        card_value_list.append(first)
        
        while True:
            for one in range(0,one_count):
                first = first+1
                card_value_list.append(first)
            if first == final:
                break
            first= first + _count
            card_value_list.append(first) 
            if first == final:
                break
        card_list.append(card_value_list)
    devide = int(final/2)+1
    #지수 변수
    p = 0 
    #결과값
    res = 0
    #반복문 돌면서 res 계산
    for c in range(0,count):
        get_bi = my_card(c, card_list, devide)
        pp = pow(2,p)
        res = res + get_bi * pp 
        p = p+1
    if res != 0:
        print(f"당신이 마음에 드는 숫자는 {res}입니다. \n\n\n")
        print("어때요 신기하죠!! \n")
        print("지금까지 마술의 세계였습니다. \n\n");
    else:
        print("맘에 드는 숫자가 없네요")

def my_card(index, card, count ):
    cardname = chr(ord('A') + index)
    while True:
        print(f"  ------------ {cardname} 카드 ------------\n" )
        # 카드 배열 결정 제곱수이면 정사각형 아니면 4로 나눠서 결정함 
        root_num = math.sqrt(count)
        loop = 0
        cell_loop = 0
        if root_num == round(root_num): 
            loop =  int(root_num)
            cell_loop = int(root_num)
        else:
            sep_count = int(count/2)
            #무조건 제곱수로 떨어짐
            root_count = int(math.sqrt(sep_count))
            loop = root_count 
            cell_loop = root_count *2 
        arr_index = 0
        for i in range(0,loop):
            for j in range(0,cell_loop):
                print('%7d'% card[index][arr_index], end ='')
                arr_index = arr_index +1 
            print("\n")
        print(" ---------------------------------\n")
        print("\n\n")
        print(f"{cardname} 카드에 생각한 숫자가 있다면 YES(1번), \n")
        print("없다면 NO(0번)을 선택하여 주시기 바랍니다. : ")
        result = int(input())
        print("\n\n")
        if result>-1 and result <2:
            return result

makeCard()
