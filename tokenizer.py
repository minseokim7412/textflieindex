# 한 줄을 단어로 분리, 소문자 변환, 전치사·관사 제외
import re  # 정규식으로 영어 알파벳 단어만 찾기


class Tokenizer:
    def __init__(self):
        # 제외할 단어 목록 (관사, 전치사, 접속사)
        self.unused_word = [
            "a",
            "an",
            "the",
            "in",
            "on",
            "at",
            "of",
            "to",
            "for",
            "by",
            "with",
            "from",
            "into",
            "and",
            "or",
            "but",
            "nor",
            "so",
            "yet",
            "as",
        ]

    def Split(self, line):  # 1. 한 줄을 단어로 나누고 소문자로 바꿈
        words = re.findall(
            "[a-zA-Z]+", line
        )  # 영어 알파벳이 이어진 부분만 추출 ("APPLE123" → "APPLE")
        return [self.ToLower(word) for word in words]

    def LowerChar(self, ch):  # 문자 하나를 소문자로 바꿈 (C의 upper_case와 같은 방식)
        res = ch
        if ch >= "A" and ch <= "Z":  # 대문자이면
            res = chr(ord(ch) + 32)  # 아스키 코드에 32를 더함 ('A'(65) → 'a'(97))
        return res

    def ToLower(self, word):  # 단어의 모든 문자를 소문자로 바꿈
        res = ""
        for ch in word:
            res += self.LowerChar(ch)
        return res

    def IsUnused(self, word):  # 2. 단어 하나가 제외 단어인지 확인
        return word in self.unused_word
