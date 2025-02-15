import sys

N = int(sys.stdin.readline().rstrip())
num_list = [sys.stdin.readline().rstrip() for _ in range(N)]

for i in range(1, len(num_list)) :
    for j in range(i, 0, -1) :
        try :
            int_part1, dec_part1 = num_list[j].split(".")
            int_part2, dec_part2 = num_list[j-1].split(".")

            # 정수 부분 비교
            if int(int_part1) < int(int_part2):
                num_list[j], num_list[j-1] = num_list[j-1], num_list[j]

            elif int(int_part1) == int(int_part2):
                if int(dec_part1) < int(dec_part2):
                    num_list[j], num_list[j-1] = num_list[j-1], num_list[j]

        except :
            if '.' in num_list[j] :
                if float(num_list[j]) < int(num_list[j-1]) :
                    num_list[j], num_list[j-1] = num_list[j-1], num_list[j]
            else :
                if int(num_list[j]) <= float(num_list[j-1]) :
                    num_list[j], num_list[j-1] = num_list[j-1], num_list[j]

for k in range(len(num_list)) :
    print(num_list[k])

                