import random

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["그거 흥미롭군요, 저에게 더 말해주세요.",
                    "알겠습니다. 계속하세요.",
                    "왜 그렇게 말하세요?",
                    "이상한 날씨에요, 그렇지 않나요?",
                    "주제를 바꿉시다.",
                    "어젯 밤에 게임을 완료했나요?"]

print("안녕하세요, 저는 간단한 로봇 Marvin입니다.")
print("당신은 'bye'라고 치면 아무 때나 이 대화를 마칠 수 있습니다.")
print("각 답변을 입력한 후 'enter'를 누르세요.")
print("오늘 어떠세요?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input.lower() == "bye":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("얘기하게 되어서 즐거웠습니다, 안녕히가세요!")
