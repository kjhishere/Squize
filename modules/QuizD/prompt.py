class Prompt:
    TARGETS = [
        "대한민국 {LEVEL} {GRADE}학년을 대상으로 다음 교육과정에서 특정부분을 주제로 문제를 만들어야 한다.",
        "{CURRICULUM}의 {SUBJECT} 선택과목에 대한 문제를 만들 것이다.",
        "{SUBJECT}의 각 단원은 다음과 같이 구성되어 있다. {UNITS}",
    ]

    CONDITIONS = [
        "문제는 객관식으로 구성한다. 선택지는 5개로 한다.",
        "한 문제당 1개의 단락으로 구성한다. 1단락에는 1개의 문제만을 포함한다.",
        "1단락은 다음과 같은 구조로 이루어져야 한다. \n    - (문항번호). (문제 내용) \n    (선택지)",
        "문항번호와 문제 내용은 볼드체로 기술한다. 선택지는 기울임체로 기술한다.",
        '각 문제와 문제 사이는 "---"으로 구분하며, 반드시 선택지는 5개의, 1. 2. 3. 4. 5. 의 형태이어야 한다.',
        "문제의 정답은 반드시 선택지 중 하나여야 한다.",
        "문제에 밑에 해설을 추가해야 하며, 해설은 다음의 형식을 만족해야한다. \n    - 정답: (정답 문항) \n    - 해설: (해설)",
        "정답과 해설은 줄바꿈으로 구분되어야 한다.",
    ]
    CONDITIONS = [
        "문제는 객관식으로 구성한다. 선택지는 5개로 한다.",
        "한 문제당 1개의 단락으로 구성한다. 1단락에는 1개의 문제만을 포함한다.",
        "1단락은 다음과 같은 구조로 이루어져야 한다. \n    - (문항번호). (문제 내용) \n    (선택지)",
        "문항번호와 문제 내용은 볼드체로 기술한다. 선택지는 기울임체로 기술한다.",
        '각 문제와 문제 사이는 "---"으로 구분하며, 반드시 선택지는 5개의, 1. 2. 3. 4. 5. 의 형태이어야 한다.',
        "문제의 정답은 반드시 선택지 중 하나여야 한다.",
        "문제에 밑에 해설을 추가해야 하며, 해설은 다음의 형식을 만족해야한다. \n    - 정답: (정답 문항) \n    - 해설: (해설)",
        "정답과 해설은 줄바꿈으로 구분되어야 한다.",
    ]

    GENERATE = [
        "각 단원 중에서 {UNIT} 단원의 {KEYWORD} 키워드를 중심으로 문제를 {COUNT}개 만들어라.",
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
        for gen in self.GENERATE:
            prompt += formatter(gen)

        return prompt.rstrip()
