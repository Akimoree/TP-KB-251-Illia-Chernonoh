import pytest

import main
from student import Student
from student_list import StudentList
from utils import StudentFile


@pytest.fixture
def studentList():
    result = StudentList()
    result.add(Student("Zak", "3", "zak@gmail.com", "KB-251"))
    result.add(Student("Bob", "1", "bob@gmail.com", "KB-252"))
    result.add(Student("Emma", "2", "emma@gmail.com", "KB-241"))
    return result



def test_studentAttributes():
    s = Student("Bob", "1", "b@g.com", "KB-1")
    assert (s.name, s.phone, s.email, s.group) == ("Bob", "1", "b@g.com", "KB-1")


def test_studentStr():
    s = Student("Bob", "1", "b@g.com", "KB-1")
    assert str(s) == "Student name is Bob,  Phone is 1,  Email is b@g.com,  Group is KB-1"


def test_studentEquality():
    assert Student("A", "1", "e", "g") == Student("A", "1", "e", "g")
    assert Student("A", "1", "e", "g") != Student("B", "1", "e", "g")



def test_addKeepsSorted(studentList):
    assert studentList.names() == ["Bob", "Emma", "Zak"]
    studentList.add(Student("Jon", "4", "j@g.com", "KB-242"))
    assert studentList.names() == ["Bob", "Emma", "Jon", "Zak"]


def test_findInsertPosition(studentList):
    assert studentList.findInsertPosition("Adam") == 0
    assert studentList.findInsertPosition("Jon") == 2
    assert studentList.findInsertPosition("Zoe") == 3


def test_findPosition(studentList):
    assert studentList.findPosition("Emma") == 1
    assert studentList.findPosition("Nobody") == -1


def test_remove(studentList):
    assert studentList.remove("Emma") is True
    assert studentList.names() == ["Bob", "Zak"]


def test_removeNotFound(studentList):
    assert studentList.remove("Nobody") is False
    assert len(studentList) == 3


def test_updatePartially(studentList):
    assert studentList.update("Bob", "", "999", "", "") is True
    item = studentList[studentList.findPosition("Bob")]
    assert item.phone == "999"
    assert item.email == "bob@gmail.com"
    assert item.group == "KB-252"


def test_updateNameResorts(studentList):
    studentList.update("Bob", "Yan", "", "", "")
    assert studentList.names() == ["Emma", "Yan", "Zak"]


def test_updateNotFound(studentList):
    assert studentList.update("Nobody", "A", "", "", "") is False
    assert studentList.names() == ["Bob", "Emma", "Zak"]


def test_printAll(studentList, capsys):
    studentList.printAll()
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == 3
    assert lines[0].startswith("Student name is Bob")



def test_saveAndLoad(tmp_path, studentList):
    storage = StudentFile(str(tmp_path / "out.csv"))
    storage.save(studentList)
    loaded = StudentList()
    storage.load(loaded)
    assert list(loaded) == list(studentList)


def test_saveWritesHeader(tmp_path, studentList):
    path = tmp_path / "out.csv"
    StudentFile(str(path)).save(studentList)
    assert path.read_text(encoding="utf-8").splitlines()[0] == "Name,Phone,Email,Group"


def test_loadSortsByName(tmp_path):
    path = tmp_path / "in.csv"
    path.write_text("Name,Phone,Email,Group\nZak,3,z@g.com,KB-1\nBob,1,b@g.com,KB-2\n",
                    encoding="utf-8")
    result = StudentList()
    StudentFile(str(path)).load(result)
    assert result.names() == ["Bob", "Zak"]


def test_loadFileNotFound():
    with pytest.raises(FileNotFoundError):
        StudentFile("no_such_file.csv").load(StudentList())



def runMain(monkeypatch, path, answers):
    it = iter(answers)
    monkeypatch.setattr("main.argv", ["main.py", str(path)])
    monkeypatch.setattr("builtins.input", lambda text: next(it))
    main.main()


def test_mainCreateAndSave(tmp_path, monkeypatch):
    path = tmp_path / "book.csv"
    path.write_text("Name,Phone,Email,Group\nBob,1,b@g.com,KB-2\n", encoding="utf-8")
    runMain(monkeypatch, path, ["c", "Adam", "5", "a@g.com", "KB-1", "x"])
    result = StudentList()
    StudentFile(str(path)).load(result)
    assert result.names() == ["Adam", "Bob"]


def test_mainUpdateAndDelete(tmp_path, monkeypatch):
    path = tmp_path / "book.csv"
    path.write_text("Name,Phone,Email,Group\nBob,1,b@g.com,KB-2\nEmma,2,e@g.com,KB-3\n",
                    encoding="utf-8")
    runMain(monkeypatch, path, ["u", "Bob", "", "777", "", "", "d", "Emma", "x"])
    result = StudentList()
    StudentFile(str(path)).load(result)
    assert result.names() == ["Bob"]
    assert result[0].phone == "777"


def test_mainNoArgs(monkeypatch, capsys):
    monkeypatch.setattr("main.argv", ["main.py"])
    main.main()
    assert "Please specify" in capsys.readouterr().out


def test_mainMissingFile(monkeypatch, capsys):
    monkeypatch.setattr("main.argv", ["main.py", "nope.csv"])
    main.main()
    assert "File was not found" in capsys.readouterr().out