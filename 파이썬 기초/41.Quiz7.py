for 보고서 in range(1,51) :
    f=open("{}주차.txt".format(보고서),"w",encoding="utf8")
    f.write("-{}주차 주간보고-".format(보고서))
    f.write("\n부서 :") 
    f.write("\n이름 :")
    f.write("\n업무 요약 :")

