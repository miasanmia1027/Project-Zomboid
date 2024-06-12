import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def 노가다(user_import, a, b):
    if user_import == a:
        # 이미지 파일 읽기
        img = mpimg.imread(f'images_1/img_{b}.png')

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
    노가다(user_import, "사소한 출혈"or"과다출혈"or"심각한 출혈"or"출혈"or "출혈 목록", 3)
    노가다(user_import, "부상 기본정보",4 )
    노가다(user_import, "경상"or'부상'or'심각한 부상'or"치명적인 부상"or"부상 목록", 5)
    노가다(user_import, "지침",6 )
    노가다(user_import, "약간 지침"or"많이 지침"or"매우 지침"or"기진맥진"or"지침 목록",7 )
    노가다(user_import, "배부름"or "배고픔"or"밥",8 )
    노가다(user_import, "어머니의 밥상"or"배가 든든함"or"적당한 포만감"or"뇨기는 때움"or"배부름 목록"or"밥 목록",9 )
    노가다(user_import, "출출함"or"배고픔"or "매우 배고픔"or"굶주림"or"배고츰 목록",9 )
    노가다(user_import, "감기",11 )
    노가다(user_import, "콧물이 남"or"두통이 동반된 콧물"or "감기"or"지독한 감기"or"감기 목록",12 )
    노가다(user_import, "약간 술기운"or "조금 취함"or"많이 취함"or"꽐라"or "술 목록",14 )
    노가다(user_import, "무거움",15 )
    노가다(user_import, "약간 무거움"or"많이 무거움"or"매우 무거움"or"용량초과"or "무거움 목록",16 )
    노가다(user_import, "더움",18 )
    노가다(user_import, "약간 더움"or"지나치게 더움"or"찜통"or"열사병"or"더움 목록",19 )
    노가다(user_import, "추움",20 )
    노가다(user_import, "쌀쌀함"or"추움"or"매우 추움"or"저체온증"or"추움 목록",21 )
    노가다(user_import, "가벼운 찬 바람"or"성가신 찬 바람"or"얼어같은 찬 바람"or"엄청나게 추운 바람"or"바람 목록"or"찬 바람"or"윈드칠"or"바람",23 )

    if user_import == "":
        break
    
#노가다(user_import,"",)
