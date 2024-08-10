def test_function():
    def inner_function():
        def home_function():
            a = "Я в области функции test_function"
            print(a)

        home_function()

    inner_function()


test_function()
inner_function()