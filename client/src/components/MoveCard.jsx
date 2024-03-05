import React from "react"

function MoveCard({ move }) {

    return (
        <div>
            <li className="move_card">
                {console.log(move.name)}
                <h3>{move.name}</h3>
            </li>
        </div>
    )
}

export default MoveCard