from .prompt import Prompt


class Earth(Prompt):
    SUBJECT = "지구과학I"
    UNITS = """
    1. 지권의 변동
        - 판 구조론의 정립, 대륙 분포의 변화, 맨틀 대류와 플룸 구조론, 변동대와 화성암
    2. 지구의 역사
        - 퇴적암과 퇴적 구조, 여러 가지 지질 구조, 지층의 생성순서, 지질연대 측정, 지질시대의 환경과 생물
    3. 대기와 해양의 변화
        - 날씨의 변화, 태풍과 날씨, 우리나라의 주요 악기상, 해수의 성질
    4. 대기와 해양의 상호작용
        - 해수의 표층순화, 해수의 심층순화, 대기와 해양의 상호 작용, 지구의 기후 변화
    5. 별과 외계 행성계
        - 별의 표면온도와 크기, H-R도와 별의 분류, 별의 진화, 별의 에너지원과 내부 구조, 외계 행성계 탐사, 외계 생명체 탐사
    6. 외부 은하와 우주 팽창
        - 외부 은하, 빅뱅우주론, 암흑물질과 암흑에너지
    """.rstrip()

    def __call__(self, UNIT: str, KEYWORD: str, N: int = 5) -> str:
        self.CONDITIONS.append(
            "2단원 문제를 선택할 경우 문제의 선지에 정답과 유사한 것을 많이 배치하거나 유사한 개념을 많이 넣어 문제의 난이도를 올린다."
        )
        self.CONDITIONS.append(
            "4단원에서 엘니뇨와 라니냐등을 사용한 문제를 많이 출제하고 바람의 방향과 관련한 문제를 출제할 경우 그림을 꼭 첨부하도록 한다."
        )
        self.CONDITIONS.append(
            "5단원 문제에선 주로 계산 문제를 첨부하도록 하며, 개념을 묻는 문제의 빈도수를 줄인다."
        )
        self.CONDITIONS.append(
            "해설을 진행할 때 해당 단원에서 사용자가 또 어떤 개념을 함께 학습하면 좋은지 단원과 그 이름을 함께 알려준다."
        )
        return self.generate(
            SUBJECT=self.SUBJECT,
            UNITS=self.UNITS,
            UNIT=UNIT,
            KEYWORD=KEYWORD,
            COUNT=N,
        )
