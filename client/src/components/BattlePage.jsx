import React, { useEffect, useState } from "react"
import { Switch, Route } from "react-router-dom"
import Button from "react-bootstrap/Button"
import BattleScreen from "./BattleScreen"

function BattlePage({ user, opponent }) {
    const monster = user.monsters[0]
    const oppMon = opponent.monsters[0]

    const [health, setHealth] = useState(monster.health)
    const [oppHealth, setOppHealth] = useState(oppMon.health)

    function handleClick(monster) {
        // setHealth(health - monster.moves[0]['damage'])
        // setOppHealth(oppHealth - monster.moves[0]['damage'])
    }






    console.log(monster.moves)

    return (
        <div>
            <h3>{user.username} VS {opponent.username}</h3>
            <p>{monster.name} VS {oppMon.name}</p>
            <div className="player">
                <img src={monster.image} />
                <p>{health}</p>
                <Button variant="primary" type="button" onClick={() => handleClick(monster)}>Attack</Button>
            </div>
            <div className="opponent">
                <img src={oppMon.image} />
                <p>{oppHealth}</p>
            </div>
            {/* <BattleScreen user={user} opponent={opponent} /> */}
        </div>
    )
}

export default BattlePage