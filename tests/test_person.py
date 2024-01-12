from demo_package_cli.person import Person


def test_person():
    p1 = Person('a', 'a')
    p2 = p1

    assert p1 == p2
