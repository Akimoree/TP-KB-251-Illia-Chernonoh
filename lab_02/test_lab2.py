import pytest

import lab2


@pytest.fixture(autouse=True)
def prepareList():
    lab2.students.clear()
    lab2.students.extend([
        {"name": "Bob", "phone": "1", "email": "bob@gmail.com", "group": "KB-252"},
        {"name": "Emma", "phone": "2", "email": "emma@gmail.com", "group": "KB-241"},
        {"name": "Zak", "phone": "3", "email": "zak@gmail.com", "group": "KB-251"},
    ])


def getNames():
    return [item["name"] for item in lab2.students]


def test_findInsertPosition():
    assert lab2.findInsertPosition("Adam") == 0
    assert lab2.findInsertPosition("Jon") == 2
    assert lab2.findInsertPosition("Zoe") == 3


def test_findPosition():
    assert lab2.findPosition("Emma") == 1
    assert lab2.findPosition("Nobody") == -1


def test_addElement():
    lab2.addElement("Jon", "4", "jon@gmail.com", "KB-242")
    assert getNames() == ["Bob", "Emma", "Jon", "Zak"]


def test_removeElement():
    assert lab2.removeElement("Emma") is True
    assert getNames() == ["Bob", "Zak"]


def test_removeElementNotFound():
    assert lab2.removeElement("Nobody") is False
    assert len(lab2.students) == 3


def test_changeElementPartially():
    assert lab2.changeElement("Bob", "", "999", "", "") is True
    item = lab2.students[lab2.findPosition("Bob")]
    assert item["phone"] == "999"
    assert item["email"] == "bob@gmail.com"
    assert item["group"] == "KB-252"


def test_changeElementName():
    lab2.changeElement("Bob", "Yan", "", "", "")
    assert getNames() == ["Emma", "Yan", "Zak"]


def test_changeElementNotFound():
    assert lab2.changeElement("Nobody", "A", "", "", "") is False
    assert getNames() == ["Bob", "Emma", "Zak"]


def test_saveAndLoad(tmp_path):
    fileName = str(tmp_path / "out.csv")
    expected = [dict(item) for item in lab2.students]
    lab2.saveToCsv(fileName)
    lab2.students.clear()
    lab2.loadFromCsv(fileName)
    assert lab2.students == expected


def test_saveWritesHeader(tmp_path):
    fileName = tmp_path / "out.csv"
    lab2.saveToCsv(str(fileName))
    firstLine = fileName.read_text(encoding="utf-8").splitlines()[0]
    assert firstLine == "Name,Phone,Email,Group"


def test_loadSortsByName(tmp_path):
    fileName = tmp_path / "in.csv"
    fileName.write_text("Name,Phone,Email,Group\nZak,3,z@g.com,KB-1\nBob,1,b@g.com,KB-2\n",
                        encoding="utf-8")
    lab2.loadFromCsv(str(fileName))
    assert getNames() == ["Bob", "Zak"]


def test_loadFileNotFound():
    with pytest.raises(FileNotFoundError):
        lab2.loadFromCsv("no_such_file.csv")


def test_mainSavesBeforeExit(tmp_path, monkeypatch):
    fileName = tmp_path / "book.csv"
    fileName.write_text("Name,Phone,Email,Group\nBob,1,b@g.com,KB-2\n", encoding="utf-8")
    answers = iter(["c", "Adam", "5", "a@g.com", "KB-1", "x"])
    monkeypatch.setattr("lab2.argv", ["lab2.py", str(fileName)])
    monkeypatch.setattr("builtins.input", lambda text: next(answers))
    lab2.main()
    lab2.loadFromCsv(str(fileName))
    assert getNames() == ["Adam", "Bob"]