def check_age(age):
    if age>=18:
        return "adult"
    return "child"

def test_age():
    assert check_age(19)== "adult"
def test_child():
    assert check_age(9) == "child"