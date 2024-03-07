import React from "react"
import Container from "react-bootstrap/Container"
import Button from "react-bootstrap/Button"
import TurnSummary from "./TurnSummary"

function MoveCard({ move, handleMoveSelec, playerMove, oppMove, oppHealth, playerHealth, updatePlayerHealth, updateOppHealth }) {

    function handleClick() {
        handleMoveSelect(move)
    }

    return (
        <Container>
            <div className="move_card">
                <p>{move.move.name} </p>
                <Button type="button" class="btn btn-secondary" onClick={() => handleClick()} data-bs-toggle="modal" data-bs-target="#resultsModalCenter">
                    Use
                </Button>

                <div class="modal fade" id="resultsModalCenter" tabindex="-1" role="dialog" aria-labelledby="resultsModalCenterTitle" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered" role="document">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="resultsModalLongTitle">Turn Summary</h5>
                                <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                            </div>
                            <div class="modal-body">
                                <TurnSummary playerMove={playerMove} oppMove={oppMonMove} oppHealth={oppHealth} playerHealth={playerHealth} updatePlayerHealth={updatePlayerHealth} updateOppHealth={updateOppHealth} />
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            </div>
                        </div>
                    </div>
                </div>

                {/* <BattleMessage /> */}
            </div>
        </Container>
    )
}

export default MoveCard