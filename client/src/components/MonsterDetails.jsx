import React, { useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import Button from 'react-bootstrap/Button'
import MoveDetails from "./MoveDetails"

function MonsterDetails({ user, updateUser }) {
    const [monster, setMonster] = useState({})
    const { id } = useParams()

    useEffect(() => {
        fetch(`/monsters/${id}`)
            .then(resp => resp.json())
            .then(monsterData => setMonster(monsterData))
    }, [id])

    function handleClick(monster) {
        console.log(user)
        console.log(user.monsters)
        console.log(user.monsters.length)
        if (user.monsters.length < 3) {

            console.log("adding monster")

            const new_monster =
            {
                health: monster.health,
                image: monster.image,
                moves: monster.moves,
                name: monster.name,
                type: monster.type,
                user_id: user.id,
                nickname: monster.nickname
            }
            fetch("/monsters", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(new_monster)
            })
                .then(resp => resp.json())
                .catch(error => {
                    console.error("Error adding monster to team", error)
                })
            setMonster(new_monster)
            updateUser(user)
        }

        else {
            console.log("Here")
        }
    }


    return (
        <div className="monster_detils_container">
            <h1>{monster.name}</h1>
            <img src={monster.image} />
            <div className="card_content">
                <p>Type: {monster.type}</p>
                <p>Moves:</p>
                <ul>
                    {/* {monster.moves.map(move => <MoveDetails key={move.id} move={move} />)} */}
                </ul>
                <Button variant="primary" type="button" onClick={() => handleClick(monster)}>Add to Team</Button>
            </div>
        </div>
    )
}

export default MonsterDetails