def test_func():
    def Inner_func():
        print('Я в области видимости функции test_func')
    Inner_func()

test_func()
# Inner_func() Мы не можем вызвать данную функцию так как она находитсь только внутри функции test_func