import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def 노가다(user_import, a, b):
    if user_import == a:
        # 이미지 파일 읽기
        img = mpimg.imread(f'무들_이미지/img_{b}.png')

        # 이미지 표시
        plt.imshow(img)
        plt.show()

while True:
    print("무들의 기본정보를 알고싶으면 (무들 기본정보)이렇게 입력")
    print("무들의 목록를 알고싶으면 (무들 목록)이렇게 입력")
    print("종료를 하고싶으면  'enter'키를 치세요")
    print("항상 figure창을 끄고 입력하게요")
    print("-"*50)

    user_import = input()

    노가다(user_import, "출혈 기본정보", 2)
    노가다(user_import,"과다출혈",3)
    노가다(user_import,"심각한 출혈",3)
    노가다(user_import,"출혈",3)
    노가다(user_import,"출혈 목록",3)
    노가다(user_import,"사소한 출혈",3)
    노가다(user_import, "부상 기본정보",4 )
    노가다(user_import,"경상",5)
    노가다(user_import,"부상",5)
    노가다(user_import,"심각한 부상",5)
    노가다(user_import,"치명적인 부상",5)
    노가다(user_import,"부상 목록",5)
    노가다(user_import, "지침",6 )
    노가다(user_import,"약간 지침",7)
    노가다(user_import,"많이 지침",7)
    노가다(user_import,"매우 지침",7)
    노가다(user_import,"기진맥진",7)
    노가다(user_import,"지침 목록",7)
    노가다(user_import,"배부름",8)
    노가다(user_import,"배고픔",8)
    노가다(user_import,"밥",8)
    노가다(user_import,"어머니의 밥상",9)
    노가다(user_import,"배가 든든함",9)
    노가다(user_import,"적당한 포만감",9)
    노가다(user_import,"요기는 떄움",9)
    노가다(user_import,"배부름 목록",9)
    노가다(user_import,"밥 목록",9)
    노가다(user_import,"출출함",9)
    노가다(user_import,"배고픔",9)
    노가다(user_import,"매우 배고픔",9)
    노가다(user_import,"굶주림",9)
    노가다(user_import,"배고픔 목록",9)
    노가다(user_import, "감기",11 )
    노가다(user_import,"콧물이 남",12)
    노가다(user_import,"두통이 동반된 콧물",12)
    노가다(user_import,"감기",12)
    노가다(user_import,"지독한 감기",12)
    노가다(user_import,"감기 목록",12)
    노가다(user_import,"약간 술기운",14)
    노가다(user_import,"조금 취함",14)
    노가다(user_import,"많이 취함",14)
    노가다(user_import,"꽐라",14)
    노가다(user_import,"술 목록",14)
    노가다(user_import, "무거움",15 )
    노가다(user_import,"약간 무거움",16)
    노가다(user_import,"많이 무거움",16)
    노가다(user_import,"매우 무거움",16)
    노가다(user_import,"용량초과",16)
    노가다(user_import,"무거움 목록",16)
    노가다(user_import, "더움",18 )
    노가다(user_import,"약간 더움",19)
    노가다(user_import,"지나치게 더움",19)
    노가다(user_import,"찜통",19)
    노가다(user_import,"열사병",19)
    노가다(user_import,"더움 목록",19)
    노가다(user_import, "추움",20 )
    노가다(user_import,"쌀쌀함",21)
    노가다(user_import,"추움",21)
    노가다(user_import,"매우 더움",21)
    노가다(user_import,"저체온증",21)
    노가다(user_import,"추움 목록",21)
    노가다(user_import,"가벼운 찬 바람",23)
    노가다(user_import,"성가신 찬 바람",23)
    노가다(user_import,"얼어같은 찬 바람",23)
    노가다(user_import,"엄청나게 추운 바람",23)
    노가다(user_import,"바람 목록",23)
    노가다(user_import,"찬 바람",23)
    노가다(user_import,"윈드칠",23)
    노가다(user_import,"바람",23)
    노가다(user_import,"고통",24)
    노가다(user_import,"약간 아픔",25)
    노가다(user_import,"고통",25)
    노가다(user_import,"심한 고통",25)
    노가다(user_import,"극도의 고통",25)
    노가다(user_import,"고통 목록",25)
    노가다(user_import,"긴장",26)
    노가다(user_import,"패닉",26)
    노가다(user_import,"긴장 목록",27)
    노가다(user_import,"패닉 목록",27)
    노가다(user_import,"살짝 긴장됨",27)
    노가다(user_import,"긴장됨",27)
    노가다(user_import,"심하게 긴장됨",27)
    노가다(user_import,"공황상태",27)
    노가다(user_import,"질병",28)
    노가다(user_import,"질병 목록",29)
    노가다(user_import,"속이 안 좋음",29)
    노가다(user_import,"매스꺼움",29)
    노가다(user_import,"아픔",29)
    노가다(user_import,"고열",29)
    노가다(user_import,"목마름",30)
    노가다(user_import,"목마름 목록",31)
    노가다(user_import,"살짝 목마름",31)
    노가다(user_import,"많이 목마름",31)
    노가다(user_import,"심한 갈증",31)
    노가다(user_import,"말라죽기 직전",31)
    노가다(user_import,"피곤함",32)
    노가다(user_import,"피곤함",33)
    노가다(user_import,"졸림",33)
    노가다(user_import,"심한 졸림",33)
    노가다(user_import,"비몽사몽",33)
    노가다(user_import,"졸림 목록",33)
    노가다(user_import,"피곤함 목록",33)
    노가다(user_import,"불행함",34)
    노가다(user_import,"불행함 목록",35)
    노가다(user_import,"슬퍼짐",35)
    노가다(user_import,"울고 싶음",35)
    노가다(user_import,"우울함",35)
    노가다(user_import,"극심한 우울함",35)
    노가다(user_import,"축축함",37)
    노가다(user_import,"젖음",37)
    노가다(user_import,"많이 젖음",37)
    노가다(user_import,"흠뻑 젖움",37)
    노가다(user_import,"젖음 목록",37)
    노가다(user_import,"스트레스",38)
    노가다(user_import,"불안함",39)
    노가다(user_import,"동요함",39)
    노가다(user_import,"심한 스트레스",39)
    노가다(user_import,"신경과민",39)
    노가다(user_import,"스트레스 목록",39)
    노가다(user_import,"지루함",40)
    노가다(user_import,"심심함",41)
    노가다(user_import,"지루함",41)
    노가다(user_import,"매우 지루함",41)
    노가다(user_import,"극심한 지루함",41)
    노가다(user_import,"지루함 목록",41)
    노가다(user_import,"화남 목록",45)
    노가다(user_import,"짜증남",45)
    노가다(user_import,"화남",45)
    노가다(user_import,"매우 화남",45)
    노가다(user_import,"격노",45)
    노가다(user_import,"전력질주 할 수 없음",46)
    노가다(user_import,"전력질주 불가",47)

    if user_import == "":
        print("ㅃ2")
        break
    
#노가다(user_import,"",)





