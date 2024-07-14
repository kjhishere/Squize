from .prompt import Prompt


class Biology(Prompt):
    SUBJECT = "생명과학I"
    UNITS = """
    1. 생명 과학의 이해
        - 생물의 특성, 귀납적 탐구 방법, 연역적 탐구 방법, 변인 통제, 대조 실험
    2. 사람의 물질대사
        - 물질대사, 기관계의 통합작용, 세포 호흡, ATP, 노폐물의 배설 과정, 대사성 질환
    3. 항상성과 몸의 조절
        - 뉴런의 종류, 활동 전위, 흥분의 전도와 전달, 시냅스, 근수축, 활주설, 호르몬 질환, 신경계 질환, 항상성, 내분비계와 호르몬의 특성, 질병의 원인, 특이적 방어 작용, 비특이적 방어 작용, 백신의 작용 원리, 항원 항체 반응
    4. 유전
        - 염색체 구조, DNA와 유전자, 유전체, 염색체 조합, 생식세포의 다양성, 상염색체 유전, 성염색체 유전, 가계도 분석, 유전병의 종류와 특징
    5. 생태계와 상호 작용
        - 생태계의 구성, 군집의 특성, 개체군의 특성, 군집 조사 방법, 천이, 에너지 흐름, 물질 순환
    """.rstrip()

    def __call__(self, UNIT: str, KEYWORD: str, N: int = 5) -> str:
        return self.generate(
            SUBJECT=self.SUBJECT,
            UNITS=self.UNITS,
            UNIT=UNIT,
            KEYWORD=KEYWORD,
            COUNT=N,
        )
