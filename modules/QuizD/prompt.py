class Prompt:
    TARGETS = [
        "대한민국 {LEVEL} {GRADE}학년을 대상으로 다음 교육과정에서 특정부분을 주제로 문제를 만들어야 한다.",
        "{CURRICULUM}의 {SUBJECT} 선택과목에 대한 문제를 만들 것이다.",
        "{SUBJECT}의 각 단원은 다음과 같이 구성되어 있다. {UNITS}",
    ]

    CONDITIONS = [
        "문제는 객관식으로 구성한다.",
        "각 문제의 제목은 마크다운 기준 1단계 크기의 제목으로 만든다.",
        "각 문제의 제목은 단원과 연관된 내용이어야 한다."
        "각 문제의 본문은 마크다운 기준 2단계 크기의 제목으로 만든다.",
        "각 문제의 본문은 문제의 내용이 적혀있어야 한다."
        "각 문제의 선택지는 마크다운 기준 숫자 목록으로 만든다.",
        "각 문제의 선택지는 5개로 한다.",
        "각 문제의 정답은 반드시 선택지 중 하나여야 한다.",
        "문제나 선택지의 수식은 MathJax를 사용하여 표현할 수 있다.",
        (
            "각 문제의 밑에는 정답과 해설이 있어야 한다. 정답과 해설은 모두 인용문 안에서 목록 형태로 작성해야한다.\n"
            "예시: \n"
            '"> - 정답: (선택지 중 정답 문항이 들어간다.)\n> - 해설: (문제에 대한 해설 내용이 들어간다.)"\n'
            "정답 문항과 해설은 줄바꿈으로 구분되어야 한다.\n"
            "정답 문항은 숫자로 표현하며, 해설은 일반 텍스트로 표현한다."
        ),
        "2개 이상의 문제를 만드는 경우에, 각 문제는 '---'로 구분한다.",
        "2개 이상의 문제를 만드는 경우에, 각 문제의 제목에 번호가 있어야 한다.",
    ]
    
    REWRITES = [
        "위 조건에 맞지 않는 경우엔, 문제를 재작성해야한다.",
        "그래프나 이미지와 같이 추가적인 자료가 필요한 문제인 경우, 자료가 필요없는 문제로 재작성 해야한다.",
        (
            '결과에서 마크다운 기준 '
            '"##" 형태의 단원명과 관련된 제목, '
            '"###" 형태의 문제 본문, '
            '"1." 형태의 선택지, '
            '" > - " 형태의 해설 또는 정답이 없는 경우에는 재작성해야한다.'
        )
    ]

    GENERATE = [
        '각 단원 중에서 {UNIT} 단원의 "{KEYWORD}" 단어를 키워드로 문제를 {COUNT}개 만들어라.',
    ]

    def __init__(
        self,
        LEVEL: str = "고등학교",
        GRADE: int = 3,
        CURRICULUM: str = "2015 개정 교육과정",
    ) -> None:
        self.LEVEL = LEVEL
        self.GRADE = GRADE
        self.CURRICULUM = CURRICULUM

    def generate(
        self, SUBJECT: str, UNITS: str, UNIT: str, KEYWORD: str, COUNT: int
    ) -> str:
        def formatter(text: str):
            return (
                " - "
                + text.format(
                    LEVEL=self.LEVEL,
                    GRADE=self.GRADE,
                    CURRICULUM=self.CURRICULUM,
                    SUBJECT=SUBJECT,
                    UNITS=UNITS,
                    UNIT=UNIT,
                    KEYWORD=KEYWORD,
                    COUNT=COUNT,
                )
                + "\n"
            )

        prompt = ""
        for target in self.TARGETS:
            prompt += formatter(target)

        prompt += "\n"
        for cond in self.CONDITIONS:
            prompt += formatter(cond)

        prompt += "\n"
        for rewrite in self.REWRITES:
            prompt += formatter(rewrite)

        prompt += "\n"
        for gen in self.GENERATE:
            prompt += formatter(gen)

        return prompt.rstrip()
