document.addEventListener('DOMContentLoaded', () => {
    const cells = document.querySelectorAll('.cell');
    cells.forEach(cell => {
        cell.addEventListener('click', handleCellClick);
    });
});

function handleCellClick(event) {
    const cell = event.target;
    const cellIndex = cell.getAttribute('data-index');

    fetch('/play', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ move: parseInt(cellIndex) }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'win') {
            alert(`Game Over! Winner: ${data.winner}`);
            resetGame();
        } else if (data.status === 'draw') {
            alert('Game Over! It\'s a draw!');
            resetGame();
        } else {
            cell.textContent = 'X';
            document.querySelector(`.cell[data-index="${data.ai_move}"]`).textContent = 'O';
        }
    });
}

function resetGame() {
    const cells = document.querySelectorAll('.cell');
    cells.forEach(cell => {
        cell.textContent = '';
    });
    fetch('/reset', { method: 'POST' }); // Optional reset logic on the server
}
