from copy import deepcopy
times_run = 0
times_pruned = 0


def minimax(board, ai_side, player_turn, max_player, max_depth, alpha=float('-inf'), beta=float('inf')):
    temp_board = deepcopy(board)
    temp_board.make_king()
    global times_run
    global times_pruned
    times_run += 1
    if max_depth == 0 or temp_board.has_won() != 0:
        print(f"Times minimax ran: {times_run}\nTimes minimax pruned: {times_pruned}")
        print("AI evaluated:", temp_board.evaluate(ai_side), "for the move", temp_board.board)
        return temp_board.evaluate(ai_side), temp_board

    if max_player:
        best_score = float('-inf')
        best_move = None

        mandatory_move, optional_moves = temp_board.return_all_valid_moves(player_turn)
        if len(mandatory_move) > 0:
            for x in mandatory_move:
                piece_to_move_into = x[0]
                dead_piece = x[1]
                piece_to_move = x[2]
                is_king = temp_board.is_king(piece_to_move[0], piece_to_move[1])

                temp_board.move(piece_to_move[0], piece_to_move[1], piece_to_move_into[0], piece_to_move_into[1],
                                dead_piece[0], dead_piece[1], is_king, player_turn)
                mandatory_move, optional_moves = temp_board.return_all_valid_moves(player_turn)
                print("Length after first check:", len(mandatory_move))
                if len(mandatory_move) > 0:
                    score = minimax(temp_board, ai_side, player_turn, True, max_depth)[0]
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)

                    if score == best_score:
                        best_move = piece_to_move, piece_to_move_into, dead_piece, is_king

                    if beta <= alpha:
                        times_pruned += 1
                        break
                else:
                    change_turn = 2 if player_turn == 1 else 1
                    score = minimax(temp_board, ai_side, change_turn, False, max_depth - 1)[0]
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)

                    if score == best_score:
                        best_move = piece_to_move, piece_to_move_into, dead_piece, is_king

                    if beta <= alpha:
                        times_pruned += 1
                        break

        else:
            for x in optional_moves:
                piece_to_move = x[0]
                piece_to_move_into = x[1]
                is_king = temp_board.is_king(piece_to_move[0], piece_to_move[1])

                temp_board.move(piece_to_move[0], piece_to_move[1], piece_to_move_into[0], piece_to_move_into[1], -1,
                                -1, is_king, player_turn)
                change_turn = 2 if player_turn == 1 else 1
                score = minimax(temp_board, ai_side, change_turn, False, max_depth - 1)[0]
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)

                if score == best_score:
                    best_move = piece_to_move, piece_to_move_into, -1, is_king

                if beta <= alpha:
                    times_pruned += 1
                    break
        # print(best_score, best_move)
        return best_score, best_move

    else:
        best_score = float('inf')
        best_move = None

        mandatory_move, optional_moves = temp_board.return_all_valid_moves(player_turn)
        if len(mandatory_move) > 0:
            for x in mandatory_move:
                piece_to_move_into = x[0]
                dead_piece = x[1]
                piece_to_move = x[2]
                is_king = temp_board.is_king(piece_to_move[0], piece_to_move[1])

                temp_board.move(piece_to_move[0], piece_to_move[1], piece_to_move_into[0], piece_to_move_into[1],
                                dead_piece[0], dead_piece[1], is_king, player_turn)
                mandatory_move, optional_moves = temp_board.return_all_valid_moves(player_turn)
                print("Length after first check:", len(mandatory_move))
                # while len(mandatory_move) > 0:
                #     for x in mandatory_move:
                #         piece_to_move_into = x[0]
                #         dead_piece = x[1]
                #         piece_to_move = x[2]
                #
                #         temp_board.move(piece_to_move[0], piece_to_move[1], piece_to_move_into[0], piece_to_move_into[1],
                #                         dead_piece[0], dead_piece[1],
                #                         temp_board.is_king(piece_to_move[0], piece_to_move[1]), player_turn)
                #         mandatory_move, optional_moves = temp_board.return_all_valid_moves(player_turn)
                #     print("Length after second check:", len(mandatory_move))

                if len(mandatory_move) > 0:
                    score = minimax(temp_board, ai_side, player_turn, False, max_depth)[0]
                    best_score = min(best_score, score)
                    beta = min(alpha, best_score)

                    if score == best_score:
                        best_move = piece_to_move, piece_to_move_into, dead_piece, is_king

                    if beta <= alpha:
                        times_pruned += 1
                        break
                else:
                    change_turn = 2 if player_turn == 1 else 1
                    score = minimax(temp_board, ai_side, change_turn, True, max_depth - 1)[0]
                    best_score = min(best_score, score)
                    beta = min(alpha, best_score)

                    if score == best_score:
                        best_move = piece_to_move, piece_to_move_into, dead_piece, is_king

                    if beta <= alpha:
                        times_pruned += 1
                        break

        else:
            for x in optional_moves:
                piece_to_move = x[0]
                piece_to_move_into = x[1]
                is_king = temp_board.is_king(piece_to_move[0], piece_to_move[1])

                temp_board.move(piece_to_move[0], piece_to_move[1], piece_to_move_into[0], piece_to_move_into[1], -1,
                                -1, is_king, player_turn)
                change_turn = 2 if player_turn == 1 else 1
                score = minimax(temp_board, ai_side, change_turn, True, max_depth - 1)[0]
                best_score = min(best_score, score)
                beta = min(alpha, best_score)

                if score == best_score:
                    best_move = piece_to_move, piece_to_move_into, -1, is_king

                if beta <= alpha:
                    times_pruned += 1
                    break

        # print(best_score, best_move)
        return best_score, best_move
