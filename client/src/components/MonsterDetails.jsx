import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import MoveDetails from "./MoveDetails"

function MonsterDetails() {
    const [monster, setMonster] = useState({})
    const { id } = useParams()

    useEffect(() => {
        fetch(`/monsters/${id}`)
            .then(resp => resp.json())
            .then(monsterData => setMonster(monsterData))
    }, [id])

    return (
        <div className="monster_detils_container">
            <h1>{monster.name}</h1>
            <img src={monster.image} />
            <div className="card_content">
                <p>Type: {monster.type}</p>
                <p>Moves:</p>
                <ul>
                    {monster.moves.map(move => <MoveDetails key={move.id} move={move} />)}
                </ul>
            </div>
        </div>
    )
}

export default MonsterDetails