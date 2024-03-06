import React from "react"
import Container from "react-bootstrap/Container"

function MoveCard({ move, handleMoveSelect }) {

    function handleClick() {
        handleMoveSelect(move)
    }

    return (
        <Container>
            <li className="move_card">
                <p>{move.move.name} </p>
                <button type="button" onClick={() => handleClick()}>Use</button>
            </li>
        </Container>
    )
}

export default MoveCard