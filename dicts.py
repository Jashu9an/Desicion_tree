class Codes:
    first: str
    second: str

    def __init__(self, f, s):
        self.first = f
        self.second = s


class Model:
    id: int
    name: str
    conclusion: str
    comment: str
    codes: Codes

    def __init__(self, uuid: int, name: str, con: str, com: str, codes: Codes):
        self.id = uuid
        self.name = name
        self.conclusion = con
        self.comment = com
        self.codes = codes


MAIN_DICT = dict(
    {
        0: Model(uuid=0, name="Прочие случаи", com="Целесообразно динамическое наблюдение и при необходимости "
                                                   "повторное выполнение илеоколоноскопии и мультифокальной биопсии",
                 con="Убедительные клинические и инструментальные диагностические данные за наличие у пациента ВЗК "
                     "отсутствуют", codes=Codes("МКБ-10/null", "МКБ-11/null")),
        1: Model(uuid=1, name="Болезнь Крона точно",
                 com="Следует учесть, что гранулёмы могут выявляться при туберкулёзе кишечника."
                     "Целесообразно проведение дообследования для исключения поражения верхних отделов "
                     "желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, КТ брюшной полости с двойным "
                     "контрастированием, УЗИ кишечника и др.)",
                 con="Высокая вероятность наличия болезни Крона",
                 codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        2: Model(uuid=2, name="Болезнь Крона точно",
                 com="Целесообразно проведение дообследования для исключения поражения верхних отделов "
                     "желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, КТ брюшной полости с двойным "
                     "контрастированием, УЗИ кишечника и др.). Следует учесть, что в случае обнаружения интактной "
                     "слизистой оболочки прямой кишки на фоне измененной слизистой оболочки толстой кишки "
                     "проксимальнее прямой кишки следует учесть, что данная ситуация возможна на фоне лечения "
                     "суппозиториями с месалазином или глюкокортикоидами ректально и не может рассматриваться как "
                     "истинное сегментарное (очаговое) поражения кишечника в дебюте заболевания. Поражение "
                     "терминального отдела подвздошной кишки в форме ретроградного илеита возможно при активном "
                     "язвенном колите с поражением всей толстой кишки",
                 con="Высокая вероятность наличия болезни Крона",
                 codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        3: Model(uuid=3, name="Болезнь Крона точно",
                 com="Целесообразно проведение дообследования для исключения поражения верхних отделов "
                     "желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, КТ брюшной полости с двойным "
                     "контрастированием, УЗИ кишечника и др.). Следует учесть, что в случае обнаружения интактной "
                     "слизистой оболочки прямой кишки на фоне измененной слизистой оболочки толстой кишки "
                     "проксимальнее прямой кишки следует учесть, что данная ситуация возможна на фоне лечения "
                     "суппозиториями с месалазином или глюкокортикоидами ректально и не может рассматриваться как "
                     "истинное сегментарное (очаговое) поражение кишечника в дебюте заболевания",
                 con="Высокая вероятность наличия болезни Крона",
                 codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        4: Model(uuid=4, name="Болезнь Крона точно",
                 com="Целесообразно проведение дообследования для исключения поражения верхних отделов "
                     "желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, КТ брюшной полости с двойным "
                     "контрастированием, УЗИ кишечника и др.). Следует учесть, что в случае обнаружения интактной "
                     "слизистой оболочки прямой кишки на фоне измененной слизистой оболочки толстой кишки "
                     "проксимальнее прямой кишки следует учесть, что данная ситуация возможна на фоне лечения "
                     "суппозиториями с месалазином или глюкокортикоидами ректально и не может рассматриваться как "
                     "истинное сегментарное (очаговое) поражение кишечника в дебюте заболевания",
                 con="Высокая вероятность наличия болезни Крона",
                 codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        5: Model(uuid=5, name="Болезнь Крона точно",
                 com="Целесообразно проведение дообследования для исключения поражения верхних отделов "
                     "желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, КТ брюшной полости с двойным "
                     "контрастированием, УЗИ кишечника и др.). Следует учесть, что в случае обнаружения интактной "
                     "слизистой оболочки прямой кишки на фоне измененной слизистой оболочки толстой кишки "
                     "проксимальнее прямой кишки следует учесть, что данная ситуация возможна на фоне лечения "
                     "суппозиториями с месалазином или глюкокортикоидами ректально и не может рассматриваться как "
                     "истинное сегментарное (очаговое) поражение кишечника в дебюте заболевания",
                 con="Высокая вероятность наличия болезни Крона",
                 codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        6: Model(uuid=6, name="Болезнь Крона точно",
                 com="Целесообразно проведение дообследования для исключения поражения верхних отделов "
                     "желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, КТ брюшной полости с двойным "
                     "контрастированием, УЗИ кишечника и др.). Следует учесть, что в случае обнаружения интактной "
                     "слизистой оболочки прямой кишки на фоне измененной слизистой оболочки толстой кишки "
                     "проксимальнее прямой кишки следует учесть, что данная ситуация возможна на фоне лечения "
                     "суппозиториями с месалазином или глюкокортикоидами ректально и не может рассматриваться как "
                     "истинное сегментарное (очаговое) поражение кишечника в дебюте заболевания",
                 con="Высокая вероятность наличия болезни Крона",
                 codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        7: Model(uuid=7, name="Язвенный колит точно", com="нет", con="Высокая вероятность наличия язвенного колита",
                 codes=Codes("МКБ-10;К51", "МКБ-11;DD71")),
        8: Model(uuid=8, name="Язвенный колит точно", com="нет", con="Высокая вероятность наличия язвенного колита",
                 codes=Codes("МКБ-10;К51", "МКБ-11;DD71")),
        9: Model(uuid=9, name="Язвенный колит точно", com="нет", con="Высокая вероятность наличия язвенного колита",
                 codes=Codes("МКБ-10;К51", "МКБ-11;DD71")),
        10: Model(uuid=10, name="Язвенный колит подозрение",
                  com="Целесообразно повторить илеколоноскопию и выполнить мультифокальную биопсию для уточнения "
                      "наличия гистологических признаков ВЗК",
                  con="Нельзя исключить наличие язвенного колита",
                  codes=Codes("МКБ-10;К51", "МКБ-11;DD71")),
        11: Model(uuid=11, name="Язвенный колит подозрение",
                  com="Целесообразно повторить илеколоноскопию и выполнить мультифокальную биопсию для уточнения "
                      "наличия гистологических признаков ВЗК",
                  con="Нельзя исключить наличие язвенного колита",
                  codes=Codes("МКБ-10;К51", "МКБ-11;DD71")),
        12: Model(uuid=12, name="Язвенный колит НК.ОБ",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК",
                  con="Нельзя исключить наличие ВЗК (язвенный колит)",
                  codes=Codes("МКБ-10;К51", "МКБ-11;DD71")),
        13: Model(uuid=13, name="Язвенный колит НК.ОБ",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК",
                  con="Нельзя исключить наличие ВЗК (язвенный колит)",
                  codes=Codes("МКБ-10;К51", "МКБ-11;DD71")),
        14: Model(uuid=14, name="Язвенный колит НК.ОБ",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК",
                  con="Нельзя исключить наличие ВЗК (язвенный колит)",
                  codes=Codes("МКБ-10;К51", "МКБ-11;DD71")),
        15: Model(uuid=15, name="Язвенный колит НК.ОБ",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК",
                  con="Нельзя исключить наличие ВЗК (язвенный колит)",
                  codes=Codes("МКБ-10;К51", "МКБ-11;DD71")),
        16: Model(uuid=16, name="Возможна Болезнь Крона тер.илеит",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК. Целесообразно проведение дообследования для исключения "
                      "поражения верхних отделов желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, "
                      "КТ брюшной полости с двойным контрастированием, УЗИ кишечника и др.)",
                  con="Нельзя исключить наличие ВЗК (болезнь Крона)", codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        17: Model(uuid=17, name="Возможна Болезнь Крона тер.илеит",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК. Целесообразно проведение дообследования для исключения "
                      "поражения верхних отделов желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, "
                      "КТ брюшной полости с двойным контрастированием, УЗИ кишечника и др.)",
                  con="Нельзя исключить наличие ВЗК (болезнь Крона)", codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        18: Model(uuid=18, name="Возможна Болезнь Крона ИЛЕОКОЛИТ",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК. Целесообразно проведение дообследования для исключения "
                      "поражения верхних отделов желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, "
                      "КТ брюшной полости с двойным контрастированием, УЗИ кишечника и др.)",
                  con="Нельзя исключить наличие ВЗК (болезнь Крона)", codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        19: Model(uuid=19, name="Возможна Болезнь Крона ИЛЕОКОЛИТ",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК. Целесообразно проведение дообследования для исключения "
                      "поражения верхних отделов желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, "
                      "КТ брюшной полости с двойным контрастированием, УЗИ кишечника и др.)",
                  con="Нельзя исключить наличие ВЗК (болезнь Крона)", codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        20: Model(uuid=20, name="Возможна Болезнь Крона ИЛЕОКОЛИТ",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК. Целесообразно проведение дообследования для исключения "
                      "поражения верхних отделов желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, "
                      "КТ брюшной полости с двойным контрастированием, УЗИ кишечника и др.)",
                  con="Нельзя исключить наличие ВЗК (болезнь Крона)", codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        21: Model(uuid=21, name="Возможна Болезнь Крона ИЛЕОКОЛИТ",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК. Целесообразно проведение дообследования для исключения "
                      "поражения верхних отделов желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, "
                      "КТ брюшной полости с двойным контрастированием, УЗИ кишечника и др.)",
                  con="Нельзя исключить наличие ВЗК (болезнь Крона)", codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        22: Model(uuid=22, name="Возможна Болезнь Крона ИЛЕОКОЛИТ",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК. Целесообразно проведение дообследования для исключения "
                      "поражения верхних отделов желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, "
                      "КТ брюшной полости с двойным контрастированием, УЗИ кишечника и др.)",
                  con="Нельзя исключить наличие ВЗК (болезнь Крона)", codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        23: Model(uuid=23, name="Возможна Болезнь Крона ИЛЕОКОЛИТ",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК. Целесообразно проведение дообследования для исключения "
                      "поражения верхних отделов желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, "
                      "КТ брюшной полости с двойным контрастированием, УЗИ кишечника и др.)",
                  con="Нельзя исключить наличие ВЗК (болезнь Крона)", codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        24: Model(uuid=24, name="Возможна Болезнь Крона ИЛЕОКОЛИТ",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК. Целесообразно проведение дообследования для исключения "
                      "поражения верхних отделов желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, "
                      "КТ брюшной полости с двойным контрастированием, УЗИ кишечника и др.)",
                  con="Нельзя исключить наличие ВЗК (болезнь Крона)", codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        25: Model(uuid=25, name="Возможна Болезнь Крона ИЛЕОКОЛИТ",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК. Целесообразно проведение дообследования для исключения "
                      "поражения верхних отделов желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, "
                      "КТ брюшной полости с двойным контрастированием, УЗИ кишечника и др.)",
                  con="Нельзя исключить наличие ВЗК (болезнь Крона)", codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        26: Model(uuid=26, name="Возможна Болезнь Крона ИЛЕОКОЛИТ",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК. Целесообразно проведение дообследования для исключения "
                      "поражения верхних отделов желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, "
                      "КТ брюшной полости с двойным контрастированием, УЗИ кишечника и др.)",
                  con="Нельзя исключить наличие ВЗК (болезнь Крона)", codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        27: Model(uuid=27, name="Возможна Болезнь Крона ИЛЕОКОЛИТ",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК. Целесообразно проведение дообследования для исключения "
                      "поражения верхних отделов желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, "
                      "КТ брюшной полости с двойным контрастированием, УЗИ кишечника и др.)",
                  con="Нельзя исключить наличие ВЗК (болезнь Крона)", codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        28: Model(uuid=28, name="Возможна Болезнь Крона ИЛЕОКОЛИТ",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК. Целесообразно проведение дообследования для исключения "
                      "поражения верхних отделов желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, "
                      "КТ брюшной полости с двойным контрастированием, УЗИ кишечника и др.)",
                  con="Нельзя исключить наличие ВЗК (болезнь Крона)", codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        29: Model(uuid=29, name="Возможна Болезнь Крона ИЛЕОКОЛИТ",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК. Целесообразно проведение дообследования для исключения "
                      "поражения верхних отделов желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, "
                      "КТ брюшной полости с двойным контрастированием, УЗИ кишечника и др.)",
                  con="Нельзя исключить наличие ВЗК (болезнь Крона)", codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        30: Model(uuid=30, name="Возможна Болезнь Крона ИЛЕОКОЛИТ",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК. Целесообразно проведение дообследования для исключения "
                      "поражения верхних отделов желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, "
                      "КТ брюшной полости с двойным контрастированием, УЗИ кишечника и др.)",
                  con="Нельзя исключить наличие ВЗК (болезнь Крона)", codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        31: Model(uuid=31, name="Возможна Болезнь Крона ИЛЕОКОЛИТ",
                  com="Убедительные гистологические признаки ВЗК не обнаружены. Возможно требуется пересмотр биопсии "
                      "другим патоморфологом или повторная мультифокальная биопсия для поиска специфических "
                      "гистологических признаков ВЗК. Целесообразно проведение дообследования для исключения "
                      "поражения верхних отделов желудочно-кишечного тракта и тонкой кишки (ФГДС, гидроМРТ, "
                      "КТ брюшной полости с двойным контрастированием, УЗИ кишечника и др.)",
                  con="Нельзя исключить наличие ВЗК (болезнь Крона)", codes=Codes("МКБ-10;K50", "МКБ-11;DD70")),
        32: Model(uuid=32, name="Ишемический колит или поражение кишечника НСП",
                  com="Целесообразно исключить ишемический колит или поражение толстой кишки, ассоциированное с "
                      "приемом нестероидных противовоспалительных препаратов",
                  con="Убедительные клинические и инструментальные диагностические данные за наличие у пациента ВЗК "
                      "отсутствуют",
                  codes=Codes("МКБ-10/null", "МКБ-11/null")),
        33: Model(uuid=33, name="Геморрой",
                  com="Требуется динамическое наблюдение, целесообразно исключить геморрой или анальную трещину как "
                      "источник появления крови в стуле",
                  con="Убедительные клинические и инструментальные диагностические данные за наличие у пациента ВЗК "
                      "отсутствуют",
                  codes=Codes("МКБ-10/null", "МКБ-11/null")),
        34: Model(uuid=34, name="Возможна опухолевая стриктура",
                  com="Необходимо исключить опухолевую природу стриктуры",
                  con="Убедительные клинические и инструментальные диагностические данные за наличие у пациента ВЗК "
                      "отсутствуют. Пациент диагностически неясен, генез стриктуры требует уточнения",
                  codes=Codes("МКБ-10/null", "МКБ-11/null")),
        35: Model(uuid=35, name="Синдром раздраженой кишки",
                  com="Характерная клиническая картина на фоне отсутствия эндоскопических и гистологических изменений "
                      "позволяет заподозрить синдром раздраженной кишки",
                  con="Убедительные клинические и инструментальные диагностические данные за наличие у пациента ВЗК "
                      "отсутствуют",
                  codes=Codes("МКБ-10/null", "МКБ-11/null")),
        36: Model(uuid=36, name="Синдром раздраженой кишки",
                  com="Характерная клиническая картина на фоне отсутствия эндоскопических и гистологических изменений "
                      "позволяет заподозрить синдром раздраженной кишки",
                  con="Убедительные клинические и инструментальные диагностические данные за наличие у пациента ВЗК "
                      "отсутствуют",
                  codes=Codes("МКБ-10/null", "МКБ-11/null")),
        37: Model(uuid=37, name="Синдром раздраженой кишки",
                  com="Характерная клиническая картина на фоне отсутствия эндоскопических и гистологических изменений "
                      "позволяет заподозрить синдром раздраженной кишки",
                  con="Убедительные клинические и инструментальные диагностические данные за наличие у пациента ВЗК "
                      "отсутствуют",
                  codes=Codes("МКБ-10/null", "МКБ-11/null")),
        38: Model(uuid=38, name="Микроскопический колит",
                  com="С учетом клинической картины заболевания и отсутствия характерных для ВЗК эндоскопических и "
                      "гистологических признаков необходимо исключить микроскопический колит",
                  con="Убедительные клинические и инструментальные диагностические данные за наличие у пациента ВЗК "
                      "отсутствуют",
                  codes=Codes("МКБ-10/null", "МКБ-11/null")),

    }
)
