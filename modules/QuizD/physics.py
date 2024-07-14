from .prompt import Prompt


class Physics(Prompt):
    SUBJECT = "물리학I"
    UNITS = """
    1. 역학과 에너지
        - 여러 가지 운동, 힘과 운동, 힘의 상호 작용, 운동량 보존, 충격량, 역학적 에너지 보존, 열기관과 내부 에너지, 열효율, 특수 상대성 이론, 질량과 에너지
    2. 물질과 전자기장
        - 전기력과 원자, 에너지 준위, 에너지띠, 반도체와 다이오드, 전류의 자기 작용, 물질의 자성, 전자기 유도
    3. 파동과 정보통신
        - 파동의 성질, 전반사와 광통신, 전자기파, 파동의 간섭, 빛의 이중성, 물질의 이중성
    """.rstrip()

    def __call__(self, UNIT: str, KEYWORD: str, N: int = 5) -> str:
        self.CONDITIONS.append(
            (
                "1단원을 선택하고, 여러가지 운동, 힘과 운동, 힘의 상호작용, 운동량 보존, 충격량을 선택할 경우, 물리량을 선택하라는 질문을 추가로 진행하며, "
                "이때 가속도, 평균속도, 운동에너지, 퍼텐셜 에너지, 역학적 에너지, 운동량, 충격량, 비보존력, 보존력이라는 선택지를 추가로 부여한다. "
                "이때 사용자가 선택할 물리량을 최소 한번 이상 사용하는 문제를 만든다."
            )
        )
        self.CONDITIONS.append(
            (
                "해설을 작성할 때 최소한의 계산식을 사용하도록 하며, "
                "미지수(문제를 해결하기 위해 사용하는 문자)에는 사용자가 이해할 수 있도록 주석을 필수적으로 첨부한다."
            )
        )
        return self.generate(
            SUBJECT=self.SUBJECT,
            UNITS=self.UNITS,
            UNIT=UNIT,
            KEYWORD=KEYWORD,
            COUNT=N,
        )
