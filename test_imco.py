from imco import validate_file, validate_path, results, get_all_files_from_folder, is_folder_empty
import pytest
import os


def test_validate_file():
    assert validate_file("bild.jpg") == True
    assert validate_file("bild..jpg") == False
    assert validate_file("bi.ld.jpg") == False
    assert validate_file("bil,d.jpg") == False
    assert validate_file("bild.jpgl") == False
    assert validate_file("bild.jpg.webp") == False


def test_validate_path():
    assert validate_path("test") == False
    assert validate_path("../test") == False
    assert validate_path("../test/") == True
    assert validate_path("./test/") == True
    assert validate_path("../te,st/") == False
    assert validate_path("../test.jpg/") == False
    assert validate_path("../_jpg/") == True


def test_results():
    assert results("Hello", "World") == "\nHello\n\nWorld\n"


def test_results_TypeError():
    with pytest.raises(TypeError):
        results("hello")


def test_get_all_files_from_folder_SystemExit():
    with pytest.raises(SystemExit):
        get_all_files_from_folder("./unknown_folder", "webp")


def test_get_all_files_from_folder():
    if not os.path.isdir("test/"):
        os.mkdir("test/")
    assert get_all_files_from_folder("test/", "webp") == []


def test_is_folder_empty():
    assert is_folder_empty(['bild1.jpg', 'bild2.jpg'], "jpg", "./folder/") == True


def test_is_folder_empty_SystemExit():
    with pytest.raises(SystemExit):
        is_folder_empty([], "jpg", "./folder/")