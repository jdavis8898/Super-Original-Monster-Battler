import React from "react"

function MoveDetails({ move }) {

    return (
        <div>
            <p>Name: {move.move.name}</p>
            <p>Type: {move.move.type}</p>
            <p>Damage: {move.move.damage}</p>
            <p>Accuracy Modifier: {move.move.accuracy}</p>
            <br></br>
        </div>
    )
}

export default MoveDetails