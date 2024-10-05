from NN import *
from result_window import *

class Questionnaire(QWidget):
    def __init__(self):
        super().__init__()

        self.result_window = None

        self.setWindowTitle("Анкета")
        # self.setGeometry(0, 0, 1920, 1000)

        self.layout = QVBoxLayout()     
        self.grid_layout = QGridLayout()
        
        self.questions = []
        for i in df_transposed.columns:
            question_layout = QHBoxLayout()
            label = QLabel(f"{i}:")
            question_layout.addWidget(label)
            label.setFixedSize(1600, 50)
            label.setWordWrap(True)

            yes_checkbox = QCheckBox("Да")
            no_checkbox = QCheckBox("Нет")
            unknown_checkbox = QCheckBox("Неизвестно")

            # Добавление чекбоксов в горизонтальный layout
            question_layout.addWidget(yes_checkbox)
            question_layout.addWidget(no_checkbox)
            question_layout.addWidget(unknown_checkbox)

            # Добавление горизонтального layout в вертикальный
            self.layout.addLayout(question_layout)
            self.questions.append((yes_checkbox, no_checkbox, unknown_checkbox))

        self.layout.addLayout(self.grid_layout)

        # Кнопка отправки
        submit_button = QPushButton("Отправить")
        submit_button.clicked.connect(self.submit)
        self.layout.addWidget(submit_button)

        self.setLayout(self.layout)
        self.showMaximized()
        self.setWindowIcon(QIcon('window_icon.png'))

    def submit(self):
        results = []
        for i, (yes, no, unknown) in enumerate(self.questions):
            if yes.isChecked():
                results.append(1)
            elif no.isChecked():
                results.append(0)
            elif unknown.isChecked():
                results.append(0.5)
            else:
                results.append(0.5)

        results = np.array(results)
        new_data_df = pd.DataFrame(results.reshape(1, -1), columns=df_transposed.columns)
        new_data_df = new_data_df[clf.feature_names_in_]

        # Получаем предсказание
        prediction = clf.predict(new_data_df)
        prediction_value = prediction[0]
        
        disease = int(prediction_value.split('№')[1])
        # Получаем данные из MAIN_DICT
        conclusion = MAIN_DICT[disease].conclusion
        comment = MAIN_DICT[disease].comment
        ident = MAIN_DICT[disease].id

        # print(f'{ident}, {conclusion}, {comment}')

        self.result_window = ResultWindow(conclusion, ident, comment)
        self.result_window.show()
        self.result_window.raise_()