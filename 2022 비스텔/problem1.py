import sys
input = sys.stdin.readline

button_pressed = input().strip()
def solution(button_pressed):
    keypad = {
        '1': ['.', 'Q', 'Z'],
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y'],
        '0': [' ']
    }

    result = [] # 최종 메시지를 저장할 리스트
    current_char = None # 현재 입력 중인 버튼
    count = 0 # 같은 버튼을 누른 횟수

    for char in button_pressed:
        if char == '0':  # 구분자 0 을 만났을 때
            if current_char: 
                # 현재 버튼의 문자 결정
                letter = keypad[current_char][(count-1) % len(keypad[current_char])]
                result.append(letter)
                current_char = None # 버튼 리셋
                count = 0 # 카운트 리셋
        elif char == current_char:  # 같은 버튼이 반복된 경우
                count += 1
        else:
            if current_char:
                # 이전 버튼 처리
                letter = keypad[current_char][(count-1) % len(keypad[current_char])]
                result.append(letter)
            # 새 버튼 변경
            current_char = char
            count = 1
            
    # 마지막 문자 처리
    if current_char:
        letter = keypad[current_char][(count - 1) % len(keypad[current_char])]
        result.append(letter)

    return ''.join(result)

# 결과 출력
print(solution(button_pressed))