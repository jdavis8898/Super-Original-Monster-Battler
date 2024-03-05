import React, { useState } from "react"
import Button from "react-bootstrap/Button"
import useSound from "use-sound"
import ResultsScreen from "./ResultsScreen"
import MoveCard from "./MoveCard"
import SOMB_Moves from "../sounds/SOMB_Moves.mp3"

function BattlePage({ user, opponent, battle, updateBattle, monster }) {
    const oppMon = opponent.monsters[0]

    const [health, setHealth] = useState(monster.health)
    const [oppHealth, setOppHealth] = useState(oppMon.health)

    const [playSound] = useSound(SOMB_Moves, {
        interrupt: false,
        sprite: {
            "Fire Throw": [1000, 3000],
            "Water Throw": [5000, 2000],
            "Leaf Throw": [9000, 2000],
            "Cut": [13000, 2000]
        }
    })

    function handleMoveSelect(move) {
        console.log(oppMon)
        let randomNum = Math.floor(Math.random() * 2)
        const oppMonMove = oppMon.moves[randomNum]
        console.log(oppMonMove)

        const new_health = parseInt(health) - parseInt(oppMonMove.move.damage)
        const new_opp_health = parseInt(oppHealth) - parseInt(move.move.damage)

        let playerChanceToHit = (Math.floor(Math.random() * 100))
        let oppChanceToHit = (Math.floor(Math.random() * 100))
        let playerChanceToHitUpdate = playerChanceToHit + (move.move.accuracy * 60)
        let oppChanceToHitUpdate = oppChanceToHit + (oppMonMove.move.accuracy * 60)
        console.log("Player % to hit, need 60 or higher")
        console.log(playerChanceToHit)
        console.log(move.move.accuracy)
        console.log(playerChanceToHitUpdate)
        console.log("Computer % to hit, need 60 or higher")
        console.log(oppChanceToHit)
        console.log(oppMonMove.move.accuracy)
        console.log(oppChanceToHitUpdate)


        if (playerChanceToHitUpdate >= 60) {
            playSound({ id: move.move.name })
            setOppHealth(new_opp_health)
        }

        if (oppChanceToHitUpdate >= 60) {
            setHealth(new_health)
        }

        if ((new_health <= 0) || (new_opp_health <= 0)) {
            // updateBattle(battle.id)
        }
    }

    return (
        <>
            {health > 0 && oppHealth > 0 ? (
                <div>
                    <h3>{user.username} VS {opponent.username}</h3>
                    <p>{monster.name} VS {oppMon.name}</p>
                    <div className="player">
                        <img src={monster.image} />
                        <p>{health}</p>
                        <ul className="user_moves">
                            {monster.moves.map(move => <MoveCard key={move.id} move={move} handleMoveSelect={handleMoveSelect} />)}
                        </ul>
                        {/* <Button variant="primary" type="button" onClick={() => handleClick(monster)}>Attack</Button> */}
                    </div>
                    <div className="opponent">
                        <img src={oppMon.image} />
                        <p>{oppHealth}</p>
                    </div>
                </div>
            ) : (
                <div>
                    <ResultsScreen user={user} opponent={opponent} monster={monster} oppMon={oppMon} health={health} oppHealth={oppHealth} />
                </div>
            )}
        </>
    )
}

export default BattlePage