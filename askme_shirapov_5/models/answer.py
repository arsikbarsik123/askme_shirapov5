class Answer:
    def __init__(self, iden, author, upvotes, text, is_correct, question):
        self._id = iden
        self._author = author
        self._upvotes = upvotes
        self._text = text
        self._is_correct = is_correct
        self._question = question

    def __repr__(self):
        return f"Answer(id={self.id}, author={self._author}, upvotes={self._upvotes}, is_correct={self._is_correct}, question={self._question})"

    def id(self):
        return self._id

    def author(self):
        return self._author

    def upvotes(self):
        return self._upvotes

    def text(self):
        return self._text

    def is_correct(self):
        return self._is_correct

    def question(self):
        return self._question

mock_answers = [
    Answer(
        iden=1,
        author='John',
        upvotes=5,
        text='Переменная — это именованная область памяти, в которой хранится значение. В Python переменная объявляется просто присваиванием: my_variable = 10.',
        is_correct=True,
        question=1,
    ),

    Answer(
        iden=2,
        author='Sophia',
        upvotes=4,
        text='int — это целые числа (например, 10), float — числа с плавающей запятой (например, 10.5), string — строки текста (например, "Привет").',
        is_correct=True,
        question=2,
    ),

    Answer(
        iden=3,
        author='Max',
        upvotes=3,
        text='if используется для выполнения кода при выполнении условия. Например: if x > 0: print("Положительное число").',
        is_correct=True,
        question=3,
    ),

    Answer(
        iden=4,
        author='Emma',
        upvotes=6,
        text='10 % 3 вернёт 1, так как это остаток от деления 10 на 3.',
        is_correct=True,
        question=4,
    ),

    Answer(
        iden=5,
        author='Oliver',
        upvotes=5,
        text='Циклы позволяют повторять выполнение кода. for используется для перебора элементов, while — для выполнения до тех пор, пока условие истинно.',
        is_correct=True,
        question=5,
    ),

    Answer(
        iden=6,
        author='Emily',
        upvotes=4,
        text='Массив (список) создаётся в Python с помощью квадратных скобок: my_list = [1, 2, 3].',
        is_correct=True,
        question=6,
    ),

    Answer(
        iden=7,
        author='Liam',
        upvotes=5,
        text='Функция — это блок кода, который выполняется при вызове. Она объявляется с помощью def: def my_function(): print("Hello").',
        is_correct=True,
        question=7,
    ),

    Answer(
        iden=8,
        author='Sophia',
        upvotes=3,
        text='Комментарии в коде используются для пояснений и начинаются с #: # Это комментарий.',
        is_correct=True,
        question=8,
    ),

    Answer(
        iden=9,
        author='James',
        upvotes=4,
        text='= используется для присваивания, а == для проверки равенства. Например, x = 5 присваивает значение, а x == 5 проверяет.',
        is_correct=True,
        question=9,
    ),

    Answer(
        iden=10,
        author='Mia',
        upvotes=3,
        text='Если выйти за пределы массива, возникнет ошибка IndexError: list index out of range.',
        is_correct=True,
        question=10,
    ),
]

def get_by_question_id(question_id):
    answer_list = []
    for answer in mock_answers:
        if answer.question() == question_id:
            answer_list.append(answer)
    return answer_list