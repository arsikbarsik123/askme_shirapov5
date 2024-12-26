class Question:
    def __init__(self, title, text, tags, id, author, upvotes):
        self._id = id
        self._title = title
        self._author = author 
        self._text = text
        self._tags = tags
        self._upvotes = upvotes

    def __repr__(self):
        return f"Question(id={self._id}, title={self._title}, author={self._author}, upvotes={self._upvotes})"

    def id(self):
        return self._id

    def title(self):
        return self._title

    def author(self):
        return self._author

    def text(self):
        return self._text

    def tags(self):
        return self._tags

    def upvotes(self):
        return self._upvotes


def get_by_id(question_id):
    for question in mock_questions:
        if question.id() == question_id:
            return question

def get_by_tag(question_tag):
    result = []
    for question in mock_questions:
        for tag in question.tags():
            print(tag)
            if tag == question_tag:
                result.append(question)
                break
    return result


mock_questions = [
    Question(
        id=1,
        author='Student',
        title='Что такое переменная?',
        text='Можете объяснить, что такое переменная и как её объявить?',
        tags=['переменная', 'объявление', 'программирование'],
        upvotes=3,
    ),

    Question(
        id=2,
        author='Student',
        title='Чем отличаются типы данных?',
        text='Можете объяснить разницу между int, float и string?',
        tags=['типы данных', 'int', 'float', 'string'],
        upvotes=5,
    ),

    Question(
        id=3,
        author='Student',
        title='Для чего нужен if?',
        text='Расскажите, как работает конструкция if в программировании?',
        tags=['if', 'условия', 'программирование'],
        upvotes=4,
    ),

    Question(
        id=4,
        author='Student',
        title='Результат 10 % 3?',
        text='Какой будет результат операции 10 % 3 и почему?',
        tags=['операции', 'остаток', 'программирование'],
        upvotes=2,
    ),

    Question(
        id=5,
        author='Student',
        title='Что такое цикл?',
        text='Объясните, что такое цикл и чем отличаются for и while?',
        tags=['циклы', 'for', 'while', 'разница'],
        upvotes=3,
    ),

    Question(
        id=6,
        author='Student',
        title='Как создать массив?',
        text='Можете объяснить, как создать массив или список в программировании?',
        tags=['массив', 'список', 'создание', 'python'],
        upvotes=3,
    ),

    Question(
        id=7,
        author='Student',
        title='Что такое функция?',
        text='Объясните, что такое функция, как её объявить и вызвать?',
        tags=['функция', 'объявление', 'вызов', 'программирование'],
        upvotes=4,
    ),

    Question(
        id=8,
        author='Student',
        title='Что такое комментарии?',
        text='Можете рассказать, для чего нужны комментарии в коде?',
        tags=['комментарии', 'код', 'зачем нужны'],
        upvotes=2,
    ),

    Question(
        id=9,
        author='Student',
        title='Разница между = и ==?',
        text='Чем отличается знак "=" от "==" в программировании?',
        tags=['операторы', '=', '==', 'разница'],
        upvotes=3,
    ),

    Question(
        id=10,
        author='Student',
        title='Выход за пределы массива?',
        text='Что произойдёт, если выйти за пределы массива? Например, попытаться обратиться к несуществующему индексу?',
        tags=['массив', 'ошибки', 'индексы'],
        upvotes=3,
    ),
]