# 파일 열기 버튼, 파일 선택 창, 결과 영역, 안내 창
import tkinter as tk
from tkinter import filedialog  # 블로그 참고 : 파일 선택 창
from tkinter import messagebox  # 블로그 참고 : 안내 창
from word_index import WordIndex


class IndexFrame:
    def __init__(self, window):
        self.window = window
        self.word_index = WordIndex()

        window.title("텍스트파일 단어 인덱스 생성기")  # 창 제목
        window.geometry("600x500")  # 가로x세로

        top = tk.Frame(window)  # 블로그 참고 : 버튼과 파일명 칸을 한 줄로 묶는 판
        top.pack(fill=tk.X)
        self.open_button = tk.Button(
            top, text="파일 열기", command=self.OpenFile
        )  # 파일 열기 버튼
        self.open_button.pack(
            side=tk.LEFT, padx=10, pady=5
        )  # 블로그 참고 : padx, pady 여백
        self.file_label = tk.Label(
            top, text="선택된 파일 없음"
        )  # 블로그 참고 : 선택한 파일을 보여주는 칸
        self.file_label.pack(side=tk.LEFT)

        self.info_label = tk.Label(
            window, text="", anchor=tk.W
        )  # 블로그 참고 : 처리 결과 안내 칸
        self.info_label.pack(fill=tk.X, padx=10)

        scroll = tk.Scrollbar(window)  # 블로그 참고 : 스크롤바
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_area = tk.Text(
            window, font=("Consolas", 12), yscrollcommand=scroll.set
        )  # 블로그 참고 : 결과 영역
        self.result_area.pack(expand=1, fill=tk.BOTH)
        scroll.config(
            command=self.result_area.yview
        )  # 블로그 참고 : 스크롤바와 결과 영역 연결
        self.result_area.config(state=tk.DISABLED)  # 블로그 참고 : 결과 영역 수정 금지

    def OpenFile(self):  # 1. 파일 선택 창 → 고른 파일을 WordIndex에 넘기기
        file_name = filedialog.askopenfilename(
            title="텍스트 파일 선택",  # 블로그 참고 : 파일 선택 창 띄우기
            filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")],
        )
        if not file_name:
            return  # 취소 → 메인 화면 유지

        if not self.word_index.Build(file_name):
            self.ShowMessage("잘못된 파일입니다. 다시 확인해 주세요.")
            return

        self.file_label.config(
            text=file_name.split("/")[-1]
        )  # 블로그 참고 : config로 라벨 글자 변경
        if self.word_index.IsEmpty():
            self.info_label.config(text="")  # 블로그 참고
            self.SetResult("")
            self.ShowMessage("인덱스 할 단어가 존재하지 않습니다.")
            return
        self.ShowResult()

    def ShowResult(self):  # 2. 인덱스를 결과 영역에, 줄 수·단어 수를 안내 칸에 표시
        wi = self.word_index
        self.info_label.config(
            text=f"총 {wi.total_line}줄, 단어 {wi.total_word}개, "
            f"인덱스 {wi.unique_word}개 생성 완료"
        )  # 블로그 참고
        self.SetResult("\n".join(wi.GetResult()))

    def SetResult(self, text):  # 결과 영역 내용 바꾸기 : 블로그 참고
        self.result_area.config(state=tk.NORMAL)
        self.result_area.delete("1.0", tk.END)
        self.result_area.insert(tk.END, text)
        self.result_area.config(state=tk.DISABLED)

    def ShowMessage(self, message):  # 3. "잘못된 파일입니다" 같은 안내 창 띄우기
        messagebox.showwarning("안내", message)  # 블로그 참고 경고 안내 창
