import React from "react"
import Button from "react-bootstrap/Button"
import Container from "react-bootstrap/Container"

function MoveCard({ move, handleMoveSelect }) {

    function handleClick() {
        handleMoveSelect(move)
    }

    return (
        <Container>
            <li className="move_card">
                console.log(move)
                <h3>{move.move.name} </h3>
                <Button variant="primary" type="button" onClick={() => handleClick()}>Attack</Button>
            </li>
        </Container>
    )
}

export default MoveCard