'''
This file defines the variables that are used in the quiz.

For each level, there are three variables. The first contains the string 
(paragraph) with blanks (..._paragraph), the second contains the list with these
blanks (..._blanks), and the third contains the list of correct answers to fill 
in these blanks (..._answers):
'''
easy_paragraph = '''A chessboard has __1__ squares of __2__ colors. Each player 
has __3__ chess men: __4__ pieces and __5__ pawns.'''
easy_blanks = ['__1__', '__2__', '__3__', '__4__', '__5__']
easy_answers = [['64', 'sixty four'], ['2', 'two'], ['16', 'sixteen'], 
                ['8', 'eight'], ['8', 'eight']]
medium_paragraph = '''The king moves __1__ square in any direction. The king 
also has a special move called __2__ that involves also moving a rook. The rook 
can move any number of squares along a __3__ or file, but cannot leap over other
pieces. The bishop can move any number of squares __4__, but cannot leap over 
other pieces. The queen combines the power of a __5__ and bishop and can move
any number of squares along a rank, __6__, or diagonal, but cannot leap over 
other pieces. The move of the __7__ forms an "L"-shape: two squares vertically 
and one square horizontally, or two squares horizontally and one square 
vertically. It is the only piece that can __8__ over other pieces.'''
medium_blanks = ['__1__', '__2__', '__3__', '__4__', '__5__', '__6__', '__7__', 
                 '__8__'] 
medium_answers = [['1', 'one'], ['castling', 'castle'], ['rank', 'horizontal'], 
                  ['diagonally', 'along the diagonal'], ['rook'], 
                  ['file', 'vertical'], ['knight', 'horse'], ['leap', 'jump']]
hard_paragraph = '''The __1__ can move forward to the unoccupied square 
immediately in front of it on the same file, or on its first move it can advance
__2__ squares along the same file, provided both squares are unoccupied. It can 
capture an opponent's piece on a square diagonally in front of it on an adjacent
__3__, by moving to that square. It can not move __4__. It has two special 
moves: the en passant __5__ and promotion. The latest happens when it reaches 
the __6__ rank. It just goes away from the board while any other piece (except 
for itself and the __7__) arises on the promotion square. In the vast majority 
of cases, the piece mentioned above is __8__. When it is not, such a promotion 
is called the __9__. Only players decide what is right for them. Sometimes, 
promoting to the minor piece may lead to the immediate __10__!'''
hard_blanks = ['__1__', '__2__', '__3__', '__4__', '__5__', '__6__', '__7__', 
               '__8__', '__9__', '__10__']
hard_answers = [['pawn', 'Pawn'], ['2', 'two'], ['file', 'vertical'], 
                ['back', 'backwards'], ['capture', 'take'], 
                ['8', 'back', 'eights'], ['king', 'King'], ['queen', 'Queen'], 
                ['underpromotion'], ['mate', 'checkmate', 'win']]
# The next block defines variables that are used within prompts/notifications:
you_lost = '''You have used all the attempts. There was no correct answer. 
Well, you lost... Start over!'''
welcome = '''
Welcome to the chess quiz :) There are three levels: easy, medium, and hard.
Which one would you like to try? >>> '''
wrong_level = '''
It is not an option! There are three levels: easy, medium, and hard. 
Which one would you like to try? >>> '''
attempts_num = '''
How many attempts per problem do you want to have?
You can choose from 1 to 5 >>> '''
wrong_attempts =  '''
It is not an option! How many attempts per problem do you want to have?
You can choose from 1 to 5 >>> '''