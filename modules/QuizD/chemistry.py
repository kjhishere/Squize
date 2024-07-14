from .prompt import Prompt


class Chemistry(Prompt):
    SUBJECT = "화학I"
    UNITS = """
    1. 화학의 첫걸음
        - 화학의 유용성, 탄소 화합물의 유용성, 몰, 화학 반응식, 몰 농도
    2. 원자의 세계
        - 원자의 구성 입자, 오비탈, 전자 배치, 주기율표, 유효 핵전하, 원자 반지름, 이온화 에너지의 주기성
    3. 화학 결합과 분자의 세계
        - 화학 결합의 전기적 성질, 이온 결합, 공유 결합, 금속 결합, 전기 음성도, 쌍극자 모멘트, 결합의 극성, 전자점식, 전자쌍 반발 이론, 분자 구조
    4. 역동적인 화학 반응
        - 가역 반응, 동적 평형, pH, 중화 반응의 양적 관계, 산화, 환원, 산화수, 발열 반응, 흡열 반응
    """.rstrip()

    def __call__(self, UNIT: str, KEYWORD: str, N: int = 5) -> str:
        return self.generate(
            SUBJECT=self.SUBJECT,
            UNITS=self.UNITS,
            UNIT=UNIT,
            KEYWORD=KEYWORD,
            COUNT=N,
        )
