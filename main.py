import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QPushButton
from ui import Ui_MainWindow
from about_ui import Ui_aboutDialog
from play_ui import Ui_playCheckers
from choose_side import Ui_choose_a_side
from choose_player import Ui_which_player_dialog
from random import randint, choice
from game import Board
from ai import minimax
import images_rc

AI_score = [0, 0, 0]
p1_score = [0, 0, 0]
p2_score = [0, 0, 0]


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.aboutButton.clicked.connect(self.show_about_dialog)
        self.ui.historyButton.clicked.connect(self.recent_games_popup)
        self.ui.playHumanButton.clicked.connect(self.play_human)
        self.ui.playAIButton.clicked.connect(self.play_ai)

    @staticmethod
    def show_about_dialog():
        about_dialog = AboutDialog()
        about_dialog.isModal()
        about_dialog.exec()

    @staticmethod
    def recent_games_popup():
        recent_games_window = QMessageBox()
        recent_games_window.setWindowTitle("Unavailable")
        recent_games_window.setText("This feature has not been added yet...")
        recent_games_window.setIcon(QMessageBox.Warning)
        recent_games_window.exec()

    def play_ai(self):
        print("Playing against AI")

        player_dialog = ChoosePlayer()
        x = player_dialog.exec()

        if x == 0:
            error_msg = QMessageBox()
            error_msg.setWindowTitle("Error!")
            error_msg.setText("Please choose a player!")
            error_msg.setIcon(QMessageBox.Warning)
            error_msg.exec()
            return 0

        side_dialog = ChooseSide()
        y = side_dialog.exec()

        if y == 0:
            error_msg = QMessageBox()
            error_msg.setWindowTitle("Error!")
            error_msg.setText("Please choose a side!")
            error_msg.setIcon(QMessageBox.Warning)
            error_msg.exec()
            return 0

        game = PlayWindow(x, y)
        game.exec()
        self.ui.player1_score_label.setText(f"{p1_score[0]}-{p1_score[1]}-{p1_score[2]}")
        self.ui.player2_score_label.setText(f"{p2_score[0]}-{p2_score[1]}-{p2_score[2]}")
        self.ui.ai_score_label.setText(f"{AI_score[0]}-{AI_score[1]}-{AI_score[2]}")

    def play_human(self):
        print("Playing against Human")

        info = QMessageBox()
        info.setWindowTitle("Info")
        info.setIcon(QMessageBox.Information)
        info.setText("Player 1 chooses sides...")
        info.exec()

        side_dialog = ChooseSide()
        y = side_dialog.exec()

        if y == 0:
            error_msg = QMessageBox()
            error_msg.setWindowTitle("Error!")
            error_msg.setText("Please choose a side!")
            error_msg.setIcon(QMessageBox.Warning)
            error_msg.exec()
            return 0

        game = PlayWindow(0, y)
        game.exec()
        self.ui.player1_score_label.setText(f"{p1_score[0]}-{p1_score[1]}-{p1_score[2]}")
        self.ui.player2_score_label.setText(f"{p2_score[0]}-{p2_score[1]}-{p2_score[2]}")


class AboutDialog(QDialog):
    def __init__(self):
        super(AboutDialog, self).__init__()
        self.ui = Ui_aboutDialog()
        self.ui.setupUi(self)


# UI Functions


def add_black_piece(piece):
    piece.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
                        "image: url(:/pieces/images for pieces/black-removebg-preview(1).png);")


def add_white_piece(piece):
    piece.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
                        "image: url(:/pieces/images for pieces/white-removebg-preview.png);")


def add_kill_move(piece):
    piece.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
                        "image: url(:/pieces/images for pieces/kill_move.png);")


def remove_piece(piece):
    piece.setStyleSheet(u"background-color: rgb(4, 55, 0);")


def add_white_king(piece):
    piece.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
                        "image: url(:/pieces/images for pieces/king-removebg-preview.png);")


def add_black_king(piece):
    piece.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
                        "image: url(:/pieces/images for pieces/king_balack-removebg-preview.png);")


def add_possible_move(piece):
    piece.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
                        "image: url(:/pieces/images for pieces/possible_move.png);")


class PlayWindow(QDialog):
    def __init__(self, which_player: int, which_side: int):
        super(PlayWindow, self).__init__()
        self.ui = Ui_playCheckers()
        self.ui.setupUi(self)

        self.choose_side = which_side
        self.player_playing = which_player

        self.player_turn = 1
        self.selected_piece = None

        self.current_mandatory_moves = []
        self.current_kill_pieces = []  # Connected to above variable
        self.current_killer_pieces = []  # Connected to above variable

        self.selected_piece = None
        self.show_possible_moves = []

        self.end = False

        self.game_board = Board()

        # Means that it's player 1 vs player 2 i.e. human vs human
        if self.player_playing == 0:
            self.human_mode()
        else:
            self.ai_mode()

    def human_mode(self):

        self.ui.textHistory.clear()
        if self.choose_side == 1:
            self.ui.textHistory.append("Player 1 plays white. Player 2 plays black.")
            self.ui.playerTurnLabel.setText("Player 1's turn\n(WHITE)")
        else:
            self.ui.textHistory.append("Player 1 plays black. Player 2 plays white.")
            self.ui.playerTurnLabel.setText("Player 2's turn\n(WHITE)")

        self.ui.surrenderButton.clicked.connect(self.confirm_surrender)
        self.ui.drawButton.clicked.connect(self.confirm_draw)

        self.ui.playing_spots.buttonClicked.connect(self.click_piece)

    def click_piece(self, piece):
        piece_coords = self.find_button_coords(piece)

        if self.player_playing == 0 or (
                self.player_playing != 0 and self.choose_side == 1 and self.player_turn == 1) or (
                self.player_playing != 0 and self.choose_side == 2 and self.player_turn == 2):
            if len(self.current_mandatory_moves) > 0:  # We're doing a kill move here
                if self.selected_piece is None:
                    # DEBUG:    print(f"Killer pieces: {self.current_killer_pieces}")
                    # DEBUG:    print(f"Selected piece: {self.selected_piece}")
                    if piece_coords in self.current_killer_pieces:
                        self.selected_piece = piece
                        # DEBUG:    print(f'selected: {self.selected_piece}')
                    else:
                        self.ui.textHistory.append(
                            "Invalid piece to play! You must makes moves that kills the opponent piece if possible!")

                else:
                    if piece_coords in self.current_mandatory_moves:
                        selected_pieces_coords = self.find_button_coords(self.selected_piece)
                        combination = self.current_mandatory_moves.index(piece_coords)
                        our_dead_piece = self.current_kill_pieces[combination]
                        king = self.game_board.is_king(selected_pieces_coords[0], selected_pieces_coords[1])
                        result1 = self.game_board.move(selected_pieces_coords[0], selected_pieces_coords[1],
                                                       piece_coords[0], piece_coords[1], our_dead_piece[0],
                                                       our_dead_piece[1], king, self.player_turn)
                        if result1 is not False:
                            if self.player_turn == 1:
                                self.ui.textHistory.append(f"White moved to {piece.objectName()[8:11]}")
                            else:
                                self.ui.textHistory.append(f"Black moved to {piece.objectName()[8:11]}")
                            remove_piece(self.selected_piece)
                            for x in self.current_mandatory_moves:
                                remove_piece(self.return_button_from_coords(x))
                            self.selected_piece = None
                            dead_piece = self.return_button_from_coords((our_dead_piece[0], our_dead_piece[1]))
                            remove_piece(dead_piece)
                            if self.player_turn == 1:
                                self.ui.textHistory.append(f"Black piece at {dead_piece.objectName()[8:11]} killed.")
                            else:
                                self.ui.textHistory.append(f"White piece at {dead_piece.objectName()[8:11]} killed.")
                            if self.player_turn == 1:
                                if king:
                                    add_white_king(piece)
                                else:
                                    add_white_piece(piece)
                            elif self.player_turn == 2:
                                if king:
                                    add_black_king(piece)
                                else:
                                    add_black_piece(piece)

                            self.check_status()
                            print('double move check:', self.current_mandatory_moves)
                            if len(self.current_mandatory_moves) == 0:  # Means no double kill available
                                self.selected_piece = None
                                self.player_turn = 1 if self.player_turn == 2 else 2
                                if self.player_playing == 0:
                                    if self.player_turn == 1:
                                        self.ui.playerTurnLabel.setText(f"Player {self.who_player()}'s turn\n(WHITE)")
                                    else:
                                        self.ui.playerTurnLabel.setText(f"Player {self.who_player()}'s turn\n(BLACK)")
                                else:
                                    self.ui.playerTurnLabel.setText(f"AI's turn to play")
                                    self.ai_move(self.player_turn)
                            else:  # The turn continues
                                self.ui.textHistory.append("There is another kill available")
                                self.selected_piece = None
                    else:
                        self.selected_piece = None

            else:  # Making a normal move into an empty spot
                if piece in self.show_possible_moves:  # Then make a move
                    selected_pieces_coords = self.find_button_coords(self.selected_piece)
                    king = self.game_board.is_king(selected_pieces_coords[0], selected_pieces_coords[1])
                    result1 = self.game_board.move(selected_pieces_coords[0], selected_pieces_coords[1],
                                                   piece_coords[0], piece_coords[1], -1, -1, king, self.player_turn)
                    print(result1)
                    if result1:
                        if self.player_turn == 1:
                            self.ui.textHistory.append(f"White moved to {piece.objectName()[8:11]}")
                        else:
                            self.ui.textHistory.append(f"Black moved to {piece.objectName()[8:11]}")
                        remove_piece(self.selected_piece)
                        for x in self.show_possible_moves:
                            remove_piece(x)
                        self.selected_piece = None
                        self.show_possible_moves = []
                        if self.player_turn == 1:
                            if king:
                                add_white_king(piece)
                            else:
                                add_white_piece(piece)
                        elif self.player_turn == 2:
                            if king:
                                add_black_king(piece)
                            else:
                                add_black_piece(piece)
                        self.player_turn = 1 if self.player_turn == 2 else 2
                        if self.player_playing == 0:
                            if self.player_turn == 1:
                                self.ui.playerTurnLabel.setText(f"Player {self.who_player()}'s turn\n(WHITE)")
                            else:
                                self.ui.playerTurnLabel.setText(f"Player {self.who_player()}'s turn\n(BLACK)")
                        else:
                            self.ui.playerTurnLabel.setText(f"AI's turn to play")
                            self.ai_move(self.player_turn)

                else:
                    if self.selected_piece is not None:
                        self.selected_piece = None
                        for x in self.show_possible_moves:
                            remove_piece(x)
                        self.show_possible_moves = []

                    moves = self.game_board.possible_empty_moves(piece_coords[0], piece_coords[1], self.player_turn)
                    if len(moves) > 0:
                        self.selected_piece = piece
                        for x in moves:
                            button = self.return_button_from_coords(x)
                            self.show_possible_moves.append(button)
                            add_possible_move(button)

                self.check_status()
            self.check_status()

    def return_button_from_coords(self, x):
        button_id = (x[0] * 4) + x[1] + 1
        button = self.findChild(QPushButton, "checkers" + str(button_id))
        return button

    def check_status(self):
        if self.game_board.has_won() == 0:  # Game is not over yet, so we check for kings and mandatory moves
            change_king_logo = self.game_board.make_king()
            while len(change_king_logo) > 0:
                change_this_loop = change_king_logo.pop()
                self.promote_to_king(change_this_loop)

            self.current_mandatory_moves = []
            self.current_kill_pieces = []
            self.current_killer_pieces = []

            for x in self.game_board.mandatory_moves(self.player_turn):
                self.current_mandatory_moves.append(x[0])
                self.current_kill_pieces.append(x[1])
                self.current_killer_pieces.append(x[2])

            if len(self.current_mandatory_moves) > 0:
                print('found a kill move')
                for x in self.current_kill_pieces:
                    x = self.return_button_from_coords(x)
                    self.ui.textHistory.append(f"There is a mandatory kill move at {x.objectName()[8:11]}")
                for x in self.current_mandatory_moves:
                    x = self.return_button_from_coords(x)
                    print(self.current_mandatory_moves)
                    add_kill_move(x)

        else:  # Game over
            if self.game_board.has_won() == 1:  # White won
                if self.player_playing == 0:  # Means it was human vs human
                    if self.choose_side == 1:  # Meaning player 1 chose white
                        print("Player 1 (White) has won!")
                        p1_score[0] += 1
                        p2_score[1] += 1
                        win = QMessageBox()
                        win.setText("Player 1 (White) has won!")
                        win.setWindowTitle("Player 1 wins!")
                        win.exec()
                        self.close()
                    else:  # Means player 1 chose black
                        print("Player 2 (White) has won!")
                        p1_score[1] += 1
                        p2_score[0] += 1
                        win = QMessageBox()
                        win.setText("Player 2 (White) has won!")
                        win.setWindowTitle("Player 2 wins!")
                        win.exec()
                        self.close()

                else:
                    if self.choose_side == 1:
                        print("Impossible! The AI has lost.")
                        if self.player_playing == 1:
                            p1_score[0] += 1
                        else:
                            p2_score[0] += 1
                        AI_score[1] += 1
                        win = QMessageBox()
                        win.setText(
                            f"Player {self.player_playing} (White) has won! The AI has been beaten!")
                        win.setWindowTitle(f"Player {self.player_playing} wins!")
                        win.exec()
                        self.close()
                    elif self.choose_side == 2:
                        print("As expected, AI has won.")
                        AI_score[0] += 1
                        if self.player_playing == 1:
                            p1_score[1] += 1
                        else:
                            p2_score[1] += 1
                        win = QMessageBox()
                        win.setText("AI has won!")
                        win.setWindowTitle("AI wins!")
                        win.exec()
                        self.close()

            elif self.game_board.has_won() == 2:
                if self.player_playing == 0:
                    if self.choose_side == 1:
                        print("Player 2 (Black) has won!")
                        p1_score[1] += 1
                        p2_score[0] += 1
                        win = QMessageBox()
                        win.setText("Player 2 (Black) has won!")
                        win.setWindowTitle("Player 2 wins!")
                        win.exec()
                        self.close()
                    else:
                        print("Player 1 (Black) has won!")
                        p1_score[0] += 1
                        p2_score[1] += 1
                        win = QMessageBox()
                        win.setText("Player 1 (Black) has won!")
                        win.setWindowTitle("Player 1 wins!")
                        win.exec()
                        self.close()

                else:
                    if self.choose_side == 2:
                        print("Impossible! The AI has lost.")
                        if self.player_playing == 1:
                            p1_score[0] += 1
                        else:
                            p2_score[0] += 1
                        AI_score[1] += 1
                        win = QMessageBox()
                        win.setText(
                            f"Player {self.player_playing} (White) has won! The AI has been beaten!")
                        win.setWindowTitle(f"Player {self.player_playing} wins!")
                        win.exec()
                        self.close()
                    elif self.choose_side == 1:
                        print("As expected, AI has won.")
                        AI_score[0] += 1
                        if self.player_playing == 1:
                            p1_score[1] += 1
                        else:
                            p2_score[1] += 1
                        win = QMessageBox()
                        win.setText("AI has won!")
                        win.setWindowTitle("AI wins!")
                        win.exec()
                        self.close()

            else:
                if self.player_playing == 0:
                    print("Game ended in a draw.")
                    p1_score[2] += 1
                    p2_score[2] += 1
                    win = QMessageBox()
                    win.setText("Game ended in a draw.")
                    win.setWindowTitle("Draw")
                    win.exec()
                    self.close()

                else:
                    print("Game ended in a draw.")
                    if self.player_playing == 1:
                        p1_score[2] += 1
                    else:
                        p2_score[2] += 1
                    AI_score[2] += 1
                    win = QMessageBox()
                    win.setText("Game ended in a draw!")
                    win.setWindowTitle("Draw!")
                    win.exec()
                    self.close()

    def who_player(self):
        if self.player_playing != 0:
            return self.player_playing
        else:
            if self.choose_side == self.player_turn:
                return 1
            else:
                return 2

    def promote_to_king(self, change_this_loop):
        if change_this_loop[0] == 0:  # It's in the top most row, so we need to promote the white piece
            piece_to_change = change_this_loop[1]
            self.ui.textHistory.append(f"White piece at {piece_to_change + 1} has been promoted to king!")
            piece_to_change = self.return_button_from_coords(change_this_loop)
            add_white_king(piece_to_change)
        else:
            piece_to_change = change_this_loop[1]
            self.ui.textHistory.append(f"Black at {piece_to_change + 28} has been promoted to king!")
            piece_to_change = self.return_button_from_coords(change_this_loop)
            add_black_king(piece_to_change)

    def confirm_surrender(self):
        ask_box = QMessageBox()
        ask_box.setWindowTitle("Are you sure?")
        ask_box.setText(f"Are you sure you want to surrender, player {self.who_player()}?")
        ask_box.setIcon(QMessageBox.Question)
        ask_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ask_box.setDefaultButton(QMessageBox.Ok)
        ask_box.buttonClicked.connect(self.result_of_confirm_surrender)
        ask_box.exec()
        if self.end:
            self.close()

    @staticmethod
    def find_button_coords(piece):
        print(piece.objectName())
        piece_id = piece.objectName()
        piece_id = int(piece_id[8:11])
        piece_coords = ((piece_id - 1) // 4, (piece_id - 1) % 4)
        print(piece_coords)
        return piece_coords

    def confirm_draw(self):
        other_player = 1 if self.who_player() == 2 else 2
        ask_box = QMessageBox()
        ask_box.setWindowTitle("Agree")
        ask_box.setText(f"Do you agree to a draw, player {other_player}?")
        ask_box.setIcon(QMessageBox.Question)
        ask_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ask_box.setDefaultButton(QMessageBox.Ok)
        ask_box.buttonClicked.connect(self.result_of_confirm_draw)
        ask_box.exec()
        if self.end:
            self.close()

    def result_of_confirm_draw(self, i):
        if i.text() == "OK":
            global p1_score, p2_score
            p1_score[2] += 1
            p2_score[2] += 1

            self.end = True
            self.close()

    def result_of_confirm_surrender(self, i):
        if i.text() == "OK":
            global p1_score, p2_score, AI_score
            if self.player_playing == 0:
                if self.player_turn == 1:
                    p1_score[1] += 1
                    p2_score[0] += 1
                elif self.player_turn == 2:
                    p1_score[0] += 1
                    p2_score[1] += 1

            elif self.player_playing == 1:
                p1_score[1] += 1
                AI_score[0] += 1

            elif self.player_playing == 2:
                p2_score[1] += 1
                AI_score[0] += 1

            self.end = True
            self.close()

    def ai_mode(self):
        self.ui.textHistory.clear()
        self.ui.drawButton.setEnabled(False)
        if self.choose_side == 1:
            self.ui.textHistory.append(f"Player {self.player_playing} plays white. AI plays black.")
            self.ui.playerTurnLabel.setText(f"Player {self.player_playing}'s turn")
            self.ui.playing_spots.buttonClicked.connect(self.click_piece)
        else:
            self.ui.textHistory.append(f"Player {self.player_playing} plays black. AI plays white.")
            self.ui.playerTurnLabel.setText("AI's turn")
            mandatory, first_move = self.game_board.return_all_valid_moves(1)
            print('test')
            first_move = choice(first_move)
            print(first_move)
            piece_to_move = first_move[0]
            piece_to_move_into = first_move[1]
            self.game_board.move(piece_to_move[0], piece_to_move[1], piece_to_move_into[0], piece_to_move_into[1], -1,
                                 -1, False, 1)
            move_button = self.return_button_from_coords(piece_to_move)
            moved_to_button = self.return_button_from_coords(piece_to_move_into)
            self.ui.textHistory.append(
                f"AI has moved into {moved_to_button.objectName()[8:11]} from {move_button.objectName()[8:11]}.")
            self.ui.playerTurnLabel.setText(f"Player {self.player_playing}'s turn")
            remove_piece(move_button)
            add_white_piece(moved_to_button)
            self.player_turn = 2
            self.ui.playing_spots.buttonClicked.connect(self.click_piece)

        self.ui.surrenderButton.clicked.connect(self.confirm_surrender)

    def ai_move(self, ai_side):
        print('waiting for ai move')
        self.check_status()
        score, best_move = minimax(self.game_board, ai_side, ai_side, True, 9)
        print('ai decided:', best_move, "with the score of", score)
        if best_move is None:
            for i, x in enumerate(self.game_board.board):
                for j, y in enumerate(x):
                    if y == ai_side or y ** 10 == ai_side:
                        self.game_board.board[i][j] = 0
            self.check_status()
        moved, move, dead, is_king = best_move
        if dead == -1:  # No piece was killed
            result = self.game_board.move(moved[0], moved[1], move[0], move[1], -1, -1, is_king, ai_side)
            if result:
                moved_piece = self.return_button_from_coords(moved)
                moved_to_piece = self.return_button_from_coords(move)
                remove_piece(moved_piece)
                if ai_side == 1:
                    if is_king:
                        add_white_king(moved_to_piece)
                    else:
                        add_white_piece(moved_to_piece)
                if ai_side == 2:
                    if is_king:
                        add_black_king(moved_to_piece)
                    else:
                        add_black_piece(moved_to_piece)
                self.ui.textHistory.append(
                    f"AI moved from {moved_piece.objectName()[8:11]} to {moved_to_piece.objectName()[8:11]}")
                self.ui.playerTurnLabel.setText(f"Player {self.who_player()}'s turn")
                self.player_turn = 2 if ai_side == 1 else 1
                self.check_status()
        else:
            result = self.game_board.move(moved[0], moved[1], move[0], move[1], dead[0], dead[1], is_king, ai_side)
            if result:
                moved_piece = self.return_button_from_coords(moved)
                moved_to_piece = self.return_button_from_coords(move)
                dead_piece = self.return_button_from_coords(dead)
                remove_piece(moved_piece)
                remove_piece(dead_piece)
                if ai_side == 1:
                    if is_king:
                        add_white_king(moved_to_piece)
                    else:
                        add_white_piece(moved_to_piece)
                if ai_side == 2:
                    if is_king:
                        add_black_king(moved_to_piece)
                    else:
                        add_black_piece(moved_to_piece)
                self.ui.textHistory.append(
                    f"AI moved from {moved_piece.objectName()[8:11]} to {moved_to_piece.objectName()[8:11]} and killed {dead_piece.objectName()[8:11]}")
                self.check_status()
                while len(self.current_mandatory_moves) > 0:
                    self.ai_move(ai_side)
                self.ui.playerTurnLabel.setText(f"Player {self.who_player()}'s turn")
                self.player_turn = 2 if ai_side == 1 else 1
                self.check_status()


class ChooseSide(QDialog):
    def __init__(self):
        super(ChooseSide, self).__init__()
        self.ui = Ui_choose_a_side()
        self.ui.setupUi(self)

        self.ui.toss_button.clicked.connect(self.toss_choice)
        self.ui.chose_white_button.clicked.connect(lambda: self.done(1))
        self.ui.chose_black_button.clicked.connect(lambda: self.done(2))

    def toss_choice(self):
        toss_result = randint(1, 2)
        toss_result_word = "White" if toss_result == 1 else "Black"
        result_msg = QMessageBox()
        result_msg.setWindowTitle("Result...")
        result_msg.setText(f"The toss resulted in {toss_result_word}.")
        result_msg.exec()
        self.done(toss_result)


class ChoosePlayer(QDialog):
    def __init__(self):
        super(ChoosePlayer, self).__init__()
        self.ui = Ui_which_player_dialog()
        self.ui.setupUi(self)

        self.ui.player1_button.clicked.connect(lambda: self.done(1))
        self.ui.player2_button.clicked.connect(lambda: self.done(2))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
