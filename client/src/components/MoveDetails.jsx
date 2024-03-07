import React from "react"

function MoveDetails({ move }) {

    return (
        <div>
            <li>Name: {move.move.name}</li>
            <ul>Type: {move.move.type}</ul>
            <ul>Damage: {move.move.damage}</ul>
            <ul>Accuracy Modifier: {move.move.accuracy}</ul>
        </div>
    )
}

export default MoveDetails