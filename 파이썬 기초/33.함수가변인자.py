# def profile(name, age , lang1, lang2, lang3, lang4, lang5):
#     print("이름 :{0} \t나이 : {1}\t".format(name,age), end=" ")
#     print(lang1, lang2, lang3, lang4,lang5)


    #end=" " 프린트 문이 끝날 때 줄바꿈을 하지 않고 끝냄

def profile(name, age ,*language):
    print("이름 :{0} \t나이 : {1}\t".format(name,age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()



profile("유재석",20,"python","java","C","C++","C#","JavaScript")
profile("김태호",25,"Kotlin","Swift","","","")
