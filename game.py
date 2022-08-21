class Board:
    def __init__(self):
        self.board = [([2] * 4) for _ in range(3)] + [([0] * 4) for _ in range(2)] + [([1] * 4) for _ in range(3)]

        print(self._return_possible_spots(5, 0, True))


    @staticmethod
    def odd_or_even_row(val):
        return (val + 1) % 2

    def is_king(self, i, j):
        if self.board[i][j] >= 10:
            return True
        else:
            return False

    def has_won(self):
        white_found = False
        black_found = False
        for x in self.board:
            for y in x:
                if y == 1 or y == 10:
                    white_found = True
                    break

            if white_found:
                break

        for x in self.board:
            if black_found:
                break

            for y in x:
                if y == 2 or y == 20:
                    black_found = True
                    break

        if not white_found:
            return 2

        elif not black_found:
            return 1

        if (len(self.return_all_valid_moves(1)[0]) == 0 and len(self.return_all_valid_moves(1)[1]) == 0) or (
                len(self.return_all_valid_moves(2)[0]) == 0 and len(self.return_all_valid_moves(2)[1]) == 0):
            return 3
        else:
            return 0

    def make_king(self):
        kings = []

        for i, x in enumerate(self.board[0]):
            if x == 1:
                self.board[0][i] = 10
                kings.append((0, i))

        for i, x in enumerate(self.board[7]):
            if x == 2:
                self.board[7][i] = 20
                kings.append((7, i))

        return kings  # Returns pieces that were made king for the UI to update

    def move(self, i, j, x, y, a, b, is_king,
             player):  # (i, j) is the selected piece, (x, y) is the piece to where we jump, (a, b) is the piece that dies if it's a kill move
        piece_to_move_into = []  # All variables if there's a kill-piece-move available
        dead_piece = []  # All variables if there's a kill-piece-move available
        killer_piece = []  # All variables if there's a kill-piece-move available
        for z in self.mandatory_moves(player):
            piece_to_move_into.append(z[0])
            dead_piece.append(z[1])
            killer_piece.append(z[2])

        optional_move = self.possible_empty_moves(i, j, player)

        if len(piece_to_move_into) == 0:  # Then the player can make a move into any empty spot
            if (x, y) in optional_move:
                self.board[i][j] = 0
                if is_king:
                    self.board[x][y] = player * 10
                else:
                    self.board[x][y] = player
                print(f'Player {player} moved ({i}, {j}) to ({x}, {y})')
                return True
            else:
                return False

        else:  # Then must make the mandatory move or else the turn is not valid
            if (x, y) in piece_to_move_into:
                combination = piece_to_move_into.index((x, y))
                print("Combination of kill move:", combination)
                print(killer_piece, dead_piece, piece_to_move_into)
                if (i, j) == killer_piece[combination] and (a, b) == dead_piece[combination]:
                    print("COMBINATION FOUND")
                    self.board[i][j] = 0
                    self.board[a][b] = 0
                    if is_king:
                        self.board[x][y] = player * 10

                    else:
                        self.board[x][y] = player
                    print('Piece successfully killed')
                    return True
                else:
                    return False
            else:
                return False

    # According to rules of English and International draught:
    # It is mandatory for the player to kill the opponent tile if possible
    # Hence you can set up moves so that the opponent kills one of your pieces, but you can
    # Kill multiple of his pieces together in one move
    def mandatory_moves(self, player):
        found = False
        mandatory_move = []
        for i, x in enumerate(self.board):
            for j, y in enumerate(x):
                if y == player or y // 10 == player:
                    if player == 1:
                        spot1, spot2, spot1_loc, spot2_loc = self._return_possible_spots(i, j, True)

                        found = self._mandatory_move_check_kill(found, i, j, mandatory_move, spot1,
                                                                spot1_loc, True, 2)
                        found = self._mandatory_move_check_kill(found, i, j, mandatory_move, spot2,
                                                                spot2_loc, True, 2)

                        if y == player * 10:
                            spot1, spot2, spot1_loc, spot2_loc = self._return_possible_spots(i, j, False)

                            found = self._mandatory_move_check_kill(found, i, j, mandatory_move,
                                                                    spot1, spot1_loc, False, 2)
                            found = self._mandatory_move_check_kill(found, i, j, mandatory_move,
                                                                    spot2,
                                                                    spot2_loc, False, 2)

                    elif player == 2:

                        spot1, spot2, spot1_loc, spot2_loc = self._return_possible_spots(i, j, False)

                        found = self._mandatory_move_check_kill(found, i, j, mandatory_move, spot1,
                                                                spot1_loc, False, 1)
                        found = self._mandatory_move_check_kill(found, i, j, mandatory_move, spot2,
                                                                spot2_loc, False, 1)

                        if y == player * 10:
                            spot1, spot2, spot1_loc, spot2_loc = self._return_possible_spots(i, j, True)

                            found = self._mandatory_move_check_kill(found, i, j, mandatory_move,
                                                                    spot1, spot1_loc, True, 1)
                            found = self._mandatory_move_check_kill(found, i, j, mandatory_move,
                                                                    spot2,
                                                                    spot2_loc, True, 1)

                else:
                    continue
        return mandatory_move

    def _mandatory_move_check_kill(self, found, i, j, mandatory_move, spot1, spot1_loc, lookAhead,
                                   otherPiece):
        if spot1 == otherPiece or spot1 == otherPiece * 10:
            spot_behind, spot_behind2, spot_behind_loc, spot_behind2_loc = self._return_possible_spots(spot1_loc[0],
                                                                                                       spot1_loc[1],
                                                                                                       lookAhead)

            if spot_behind_loc is not None and spot_behind_loc[1] != j and spot_behind == 0:
                mandatory_move.append([spot_behind_loc, spot1_loc, (i, j)])
                print(f'Mandatory move at {spot_behind_loc} by killing {spot1_loc} using piece {(i, j)}')
                found = True

            if spot_behind2_loc is not None and spot_behind2_loc[1] != j and spot_behind2 == 0:
                mandatory_move.append([spot_behind2_loc, spot1_loc, (i, j)])
                print(f'Mandatory move at {spot_behind2_loc} by killing {spot1_loc} using piece {(i, j)}')
                found = True
        return found

    def possible_empty_moves(self, i, j, player):
        list_of_moves = []  # If returned empty, means no possible moves

        if self.board[i][j] == player:  # Player selected his piece
            if player == 1:
                spot1, spot2, spot1_loc, spot2_loc = self._return_possible_spots(i, j, True)
                if spot1 == 0:
                    list_of_moves.append(spot1_loc)
                if spot2 == 0:
                    list_of_moves.append(spot2_loc)

                return list_of_moves
            else:
                spot1, spot2, spot1_loc, spot2_loc = self._return_possible_spots(i, j, False)
                if spot1 == 0:
                    list_of_moves.append(spot1_loc)
                if spot2 == 0:
                    list_of_moves.append(spot2_loc)

                return list_of_moves

        elif self.board[i][j] // 10 == player:  # Player selected his own king
            spot1, spot2, spot1_loc, spot2_loc = self._return_possible_spots(i, j, True)
            spot3, spot4, spot3_loc, spot4_loc = self._return_possible_spots(i, j, False)

            if spot1 == 0:
                list_of_moves.append(spot1_loc)
            if spot2 == 0:
                list_of_moves.append(spot2_loc)
            if spot3 == 0:
                list_of_moves.append(spot3_loc)
            if spot4 == 0:
                list_of_moves.append(spot4_loc)

            return list_of_moves

        else:  # Not a valid piece for player to move
            return list_of_moves

    def _return_possible_spots(self, i: int, j: int, direction_upwards: bool):
        spot1 = None
        spot1_loc = None
        spot2 = None
        spot2_loc = None

        if direction_upwards:  # Checking tiles above a piece
            if i - 1 >= 0:
                if self.odd_or_even_row(i) == 0:  # Checking if a row is even or odd
                    if j - 1 >= 0:
                        spot1 = self.board[i - 1][j - 1]
                        spot1_loc = (i - 1, j - 1)
                    spot2 = self.board[i - 1][j]
                    spot2_loc = (i - 1, j)

                else:
                    spot1 = self.board[i - 1][j]
                    spot1_loc = (i - 1, j)
                    if j + 1 <= 3:
                        spot2 = self.board[i - 1][j + 1]
                        spot2_loc = (i - 1, j + 1)

            else:
                return spot1, spot2, spot1_loc, spot2_loc

        else:  # Checking tiles below a piece
            if i + 1 <= 7:
                if self.odd_or_even_row(i) == 0:  # Checking if the row is even or odd
                    if j - 1 >= 0:
                        spot1 = self.board[i + 1][j - 1]
                        spot1_loc = (i + 1, j - 1)
                    spot2 = self.board[i + 1][j]
                    spot2_loc = (i + 1, j)

                else:
                    spot1 = self.board[i + 1][j]
                    spot1_loc = (i + 1, j)
                    if j + 1 <= 3:
                        spot2 = self.board[i + 1][j + 1]
                        spot2_loc = (i + 1, j + 1)

            else:
                return spot1, spot2, spot1_loc, spot2_loc

        return spot1, spot2, spot1_loc, spot2_loc

    def evaluate(self, player):  # function for AI
        score = 0
        for i, x in enumerate(self.board):
            for j, y in enumerate(x):
                if y == 1:
                    score += 1 if player == 1 else -1
                elif y == 10:
                    score += 2 if player == 1 else -2
                elif y == 2:
                    score += -1 if player == 1 else 1
                elif y == 20:
                    score += -2 if player == 1 else 2
        return score

    def return_all_valid_moves(self, player):  # Function for AI
        mandatory_moves = self.mandatory_moves(player)
        valid_moves = []
        if len(mandatory_moves) > 0:
            return mandatory_moves, valid_moves
        else:
            for i, x in enumerate(self.board):
                for j, y in enumerate(x):
                    if y == player or y == player * 10:
                        optional_move = self.possible_empty_moves(i, j, player)
                        while len(optional_move) > 0:
                            valid_moves.append([(i, j), optional_move.pop()])

            return mandatory_moves, valid_moves


board = Board()
print(board.board)
