import React, { useState } from "react"
import Button from "react-bootstrap/Button"
import useSound from "use-sound"
import ResultsScreen from "./ResultsScreen"
import MoveCard from "./MoveCard"
import TestSound from "./sounds/TestSound.wav"

function BattlePage({ user, opponent, battle, updateBattle, monster }) {
    const oppMon = opponent.monsters[0]

    const [health, setHealth] = useState(monster.health)
    const [oppHealth, setOppHealth] = useState(oppMon.health)

    const [playSound, { stop }] = useSound(TestSound)

    function handleClick(monster) {

        const new_health = parseInt(health) - parseInt(oppMon.moves[0].move.damage)
        const new_opp_health = parseInt(oppHealth) - parseInt(monster.moves[0].move.damage)

        let playerChanceToHit = Math.floor(Math.random() * 100)
        let oppChanceToHit = Math.floor(Math.random() * 100)
        // console.log("Player % to hit, need 60 or higher")
        // console.log(playerChanceToHit)
        // console.log("Computer % to hit, need 60 or higher")
        // console.log(oppChanceToHit)


        if (playerChanceToHit >= 60) {
            playSound()
            setOppHealth(new_opp_health)
        }

        if (oppChanceToHit >= 60) {
            playSound()
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
                            {console.log(monster.moves)}
                            {/* {monster.moves.map(move => <MoveCard key={move.id} move={move} />)} */}
                        </ul>
                        <Button variant="primary" type="button" onClick={() => handleClick(monster)}>Attack</Button>
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