# 파일 읽기, BST 실행
from tokenizer import Tokenizer
from line_list import LineList


class TreeNode:  # BST 노드
    def __init__(self, word):
        self.word = word  # 노드에 저장된 단어
        self.lines = LineList()  # 단어가 나온 라인 번호 리스트
        self.left = None  # 알파벳 순서가 빠른 단어 자식 노드
        self.right = None  # 알파벳 순서가 느린 단어 자식 노드


class WordIndex:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.Clear()

    def Clear(self):  # 기존 인덱스 비우기
        self.root = None  # BST의 루트 노드
        self.total_line = 0  # 파일의 전체 줄 수
        self.total_word = 0  # 읽은 단어의 총 개수 (제외어 포함)
        self.unique_word = 0  # 서로 다른 단어의 개수

    def Build(self, file_name):  # 1. 파일을 한 줄씩 읽어 제외어가 아니면 저장
        try:  # 블로그 참고 : 없는 파일, 텍스트 파일이 아닌 파일이면 False 반환
            file = open(file_name, "r", encoding="UTF-8")
            lines = file.readlines()
            file.close()
        except (
            OSError,
            UnicodeDecodeError,
        ):  # 블로그 참고 : 파일 열기 오류, 텍스트가 아닌 파일 오류
            return False

        self.Clear()
        for line in lines:
            self.total_line += 1
            for word in self.tokenizer.Split(line):
                self.total_word += 1
                if not self.tokenizer.IsUnused(word):
                    self.Insert(word, self.total_line)
        return True

    def Insert(self, word, line_num):  # 2. BST에 넣기 (이미 있으면 라인 번호만 추가)
        if self.root is None:
            self.root = self.NewNode(word, line_num)
            return
        cur = self.root
        while True:
            if word == cur.word:
                cur.lines.Add(line_num)
                return
            elif word < cur.word:
                if cur.left is None:
                    cur.left = self.NewNode(word, line_num)
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = self.NewNode(word, line_num)
                    return
                cur = cur.right

    def NewNode(self, word, line_num):
        node = TreeNode(word)
        node.lines.Add(line_num)
        self.unique_word += 1
        return node

    def Inorder(self, node, result):  # 3. 중위 순회(왼쪽 → 자신 → 오른쪽)로 결과 만들기
        if node is None:
            return
        self.Inorder(node.left, result)
        result.append(f"{node.word} | {node.lines.GetLines()}")
        self.Inorder(node.right, result)

    def GetResult(self):  # 4. 결과를 화면에 넘겨주기
        result = []
        self.Inorder(self.root, result)
        return result

    def IsEmpty(self):
        return self.root is None
