import React from "react"

function MoveDetails({ move }) {

    return (
        <div>
            <h4>Name: {move.move.name}</h4>
            <ul>Type: {move.move.type}</ul>
            <ul>Damage: {move.move.damage}</ul>
        </div>
    )
}

export default MoveDetails