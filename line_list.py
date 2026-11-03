# 라인 번호 연결 리스트


class LineNode:  # 라인 번호 노드
    def __init__(self, line_num):
        self.line_num = line_num  # 라인 번호
        self.next = None  # 다음 라인 번호 노드


class LineList:
    def __init__(self):
        self.head = None  # 리스트의 첫 번째 노드
        self.tail = None  # 리스트의 마지막 노드

    def Add(self, line_num):  # 라인 번호를 리스트 뒤에 추가
        if self.tail is not None and self.tail.line_num == line_num:
            return  # 같은 줄에 단어가 여러 번 나오면 한 번만 저장
        node = LineNode(line_num)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def GetLines(self):  # "1, 2, 3" 형식의 문자열 반환
        nums = []
        cur = self.head
        while cur is not None:
            nums.append(str(cur.line_num))
            cur = cur.next
        return ", ".join(nums)
