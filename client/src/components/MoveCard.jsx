import React, { useState } from "react"
import Container from "react-bootstrap/Container"
import Button from "react-bootstrap/Button"

function MoveCard({ move, handleMoveSelect }) {
    const [showMoveInfo, setShowMoveInfo] = useState(false)

    function handleClick() {
        handleMoveSelect(move)
    }

    function showDetails() {
        setShowMoveInfo(true)
    }

    function hideDetails() {
        setShowMoveInfo(false)
    }

    return (
        <Container>
            <div className="move_card">
                <p onMouseEnter={() => showDetails()} onMouseLeave={() => hideDetails()}>{move.move.name}</p>

                {showMoveInfo ? (
                    <div>
                        <p>Damage: {move.move.damage}</p>
                        <p>Accuracy Modifier: {move.move.accuracy}</p>
                    </div>
                ) : (
                    <></>
                )}
                <Button type="button" class="btn btn-secondary" onClick={() => handleClick()}>Use</Button>
            </div>
        </Container>
    )
}

export default MoveCard