## Chess Package
A Python package implementing chess game logic, providing components for building chess applications.

### Setup
This package uses `poetry` for dependency management ([Installation Instructions](https://python-poetry.org/docs/#installation)). To set up the correct environment, run the following from the root directory after installation:
```bash
poetry install
```

### Importing from the package
After installing the package with `poetry install`, you can import its modules in your Python code as follows:
```python
from chess.models import Board
from chess.pieces import Bishop
```

If you're running scripts or using an interactive shell within the project directory, make sure you're using the poetry-managed environment:
```bash
poetry run python
```

Then you can import and use the package like normal. For example:
```python
from chess.models import Board, Position
from chess.pieces import Knight
from chess.constants import Player

board = Board()
position = Position(1,1)
knight = Knight(player=Player.WHITE, position=position)
board.add_piece(knight)
```


### Testing
To run the tests, run the following from the root directory
```bash
poetry run pytest --cov=chess
```