from src.__main__ import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello World"
