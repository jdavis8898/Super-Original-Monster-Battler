import React, { useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import Button from "react-bootstrap/Button"
import Container from "react-bootstrap/Container"
import MoveDetails from "./MoveDetails"

function MonsterDetails({ user, updateUser }) {
    const [monster, setMonster] = useState({})
    const { id } = useParams()
    const [checking, setChecking] = useState(true)

    useEffect(() => {
        fetch(`/monsters/${id}`)
            .then(resp => resp.json())
            .then(monsterData => {
                setMonster(monsterData)
                setChecking(false)
            })
    }, [id])

    // function updateMonsterMoves(monster, newMon) {

    // }

    function handleClick(monster) {
        if (user.monsters.length < 3) {

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

            console.log(new_monster)
            fetch("/monsters", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(new_monster)
            })
                .then(resp => resp.json())
                .then(newMonData => {
                    const new_mm =
                    {
                        monster_id: newMonData.id,
                        move_id: monster.moves[0].id
                    }
                    fetch("/monster_moves", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(new_mm)
                    })
                        .then(resp => resp.json())

                })
                .catch(error => {
                    console.error("Error adding monster to team", error)
                })
            updateUser(user)
        }

        else {
            console.log("Here")
        }
    }

    if (checking) {
        return <p>Loading...</p>
    }

    return (
        <Container className="monster_details_container">
            <h1>{monster.name}</h1>
            <img className="details_picture" src={monster.image} />
            <div className="card_content">
                <p>Type: {monster.type}</p>
                <p>Moves:</p>
                {monster.moves.length ? (
                    <p>
                        {monster.moves.map(move => <MoveDetails key={move.id} move={move} />)}
                    </p>
                ) : (
                    <p>No Moves to Display!</p>
                )}
                <Button className="details_button" variant="primary" type="button" onClick={() => handleClick(monster)}>Add to Team</Button>
            </div>
        </Container>
    )
}

export default MonsterDetails