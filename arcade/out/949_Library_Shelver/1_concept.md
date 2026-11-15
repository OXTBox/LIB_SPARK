# Library Shelver
PITCH: Walk through the top-down library with arrow keys to place books on their numbered shelves before the reader requests them, creating a satisfying puzzle of matching and ordering.
It is fun because every step of the library layout rewards careful navigation and precise placement to complete the shelf sequence.
CONTROLS: Arrow keys move the player; walking into a numbered shelf places the current book on that shelf.
OBJECTS:
- player | box w=30 h=30 | wireframe cyan | the moving player who walks through the library
- book | box w=25 h=25 | wireframe yellow | the item carried by the player to place on shelves
- shelf | box w=120 h=40 | wireframe green | the numbered shelf where books must be placed
- reader | box w=40 h=40 | wireframe magenta | the character who requests books in sequence
RULES:
- The player moves only with arrow keys through the library floor.
- Each book is carried by the player until a shelf is entered.
- Placing a book on its numbered shelf adds 10 to the score.
- The reader requests books in order; placing them out of order costs 1 life.
- The game ends when all books are correctly placed on their numbered shelves.
WIN: The score reaches the target of 100 points after all books are correctly placed.
LOSE: The player loses all lives when the reader requests a book that is not on its correct numbered shelf.
NUMBERS: player_speed=120, book_speed=0, shelf_speed=0, reader_speed=40, score=0, lives=3, target_score=100
RISK: Programming the reader to request books in the exact sequence required for correct placement without breaking the top-down movement logic.
