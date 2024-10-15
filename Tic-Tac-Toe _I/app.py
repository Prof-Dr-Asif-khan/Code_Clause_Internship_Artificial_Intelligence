from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initialize the Tic-Tac-Toe board
board = ['' for _ in range(9)]

def check_winner(board):
    # Possible winning combinations
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != '':
            return board[combo[0]]
    return None

def is_draw(board):
    return all(cell != '' for cell in board)

def get_ai_move(board):
    # Simple AI logic: choose the first available cell
    for i in range(len(board)):
        if board[i] == '':
            return i
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.json
    player_move = data['move']
    board[player_move] = 'X'  # User's move

    winner = check_winner(board)
    if winner:
        return jsonify({'status': 'win', 'winner': 'Player'})
    
    if is_draw(board):
        return jsonify({'status': 'draw'})

    # AI move
    ai_move = get_ai_move(board)
    board[ai_move] = 'O'
    winner = check_winner(board)
    if winner:
        return jsonify({'status': 'win', 'winner': 'AI'})
    
    return jsonify({'status': 'continue', 'ai_move': ai_move})

if __name__ == '__main__':
    app.run(debug=True)
