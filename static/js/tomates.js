function getRandomPosition(min, max) {
    return Math.random() * (max - min) + min;
}

function isPositionOccupied(occupiedPositions, top, left) {
    return occupiedPositions.some(position => position.top === top && position.left === left);
}

function adicionarTomates() {
    const tdElements = document.querySelectorAll('.tabela td');
    const occupiedPositions = [];

    tdElements.forEach(td => {
        const numTomates = Math.floor(Math.random() * 2) + 1; 

        for (let i = 0; i < numTomates; i++) {
            let top, left;
            
            do {
                top = getRandomPosition(0, 90) + '%';
                left = getRandomPosition(0, 90) + '%';
            } while (isPositionOccupied(occupiedPositions, top, left));

            occupiedPositions.push({ top, left });

            const tomate = document.createElement('div');
            tomate.classList.add('tomate');
            tomate.style.top = top;
            tomate.style.left = left;

            td.appendChild(tomate);
        }
    });
}

window.onload = adicionarTomates;