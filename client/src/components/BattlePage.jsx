import React, { useState } from "react"
import Button from "react-bootstrap/Button"
import Container from "react-bootstrap/Container"
import useSound from "use-sound"
import ResultsScreen from "./ResultsScreen"
import MoveCard from "./MoveCard"
import SOMB_Moves from "../sounds/SOMB_Moves.mp3"

function BattlePage({ user, opponent, battle, updateBattle, monster }) {
    const oppMon = opponent.monsters[0]

    const [health, setHealth] = useState(monster.health)
    const [oppHealth, setOppHealth] = useState(oppMon.health)
    const [turnSummary, setTurnSummary] = useState(false)
    const [playerMove, setPlayerMove] = useState({})
    const [oppMove, setOppMove] = useState({})
    const [playerHit, setPlayerHit] = useState(false)
    const [oppHit, setOppHit] = useState(false)

    const [playSound] = useSound(SOMB_Moves, {
        interrupt: true,
        sprite: {
            "Fire Throw": [1000, 3000],
            "Water Throw": [5000, 2000],
            "Leaf Throw": [9000, 2000],
            "Cut": [13000, 2000]
        }
    })

    function handleMoveSelect(move) {
        let randomNum = Math.floor(Math.random() * 2)
        const oppMonMove = oppMon.moves[randomNum]

        setPlayerMove(move)
        setOppMove(oppMonMove)

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
            setOppHit(true)
        }

        else if (playerChanceToHitUpdate < 60) {
            setOppHit(false)
        }

        if (oppChanceToHitUpdate >= 60) {
            setHealth(new_health)
            setPlayerHit(true)
        }

        else if (oppChanceToHitUpdate < 60) {
            setPlayerHit(false)
        }

        if ((new_health <= 0) || (new_opp_health <= 0)) {
            // updateBattle(battle.id)
        }

        setTurnSummary(true)
    }

    function handleClick() {
        setTurnSummary(false)
    }

    return (
        <div className="full_page">
            {health > 0 && oppHealth > 0 ? (
                <Container className="battle">
                    <div>
                        <h3>{user.username} VS {opponent.username}</h3>
                        <p>{monster.name} VS {oppMon.name}</p>
                    </div>
                    <div className="player">
                        <img src={monster.image} />
                        <div className="player_health">
                            <p>Remaining Health: {health}</p>
                            <progress id="health" value={health} max={monster.health}></progress>
                        </div>
                        <p className="user_moves">
                            {monster.moves.map(move => <MoveCard key={move.id} move={move} handleMoveSelect={handleMoveSelect} />)}
                        </p>
                    </div>
                    <div className="opponent">
                        <img src={oppMon.image} />
                        <br></br>
                        <br></br>
                        <br></br>
                        <div className="opp_health">
                            <p>Remaing Health: {oppHealth}</p>
                            <progress id="oppHealth" value={oppHealth} max={oppMon.health}></progress>
                        </div>
                    </div>
                    {turnSummary ? (
                        <Container className="turn_summary">
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <p>
                                {user.username}'s {monster.name} used {playerMove.move.name} and it {oppHit ? ("hit!") : ("missed.")}
                            </p>
                            <p>
                                {opponent.username}'s {oppMon.name} used {oppMove.move.name} and it {playerHit ? ("hit!") : ("missed.")}
                            </p>
                            <Button type="button" class="btn btn-dark" onClick={() => handleClick()}>Close</Button>
                        </Container>
                    ) : (
                        <div>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <br></br>
                            <p>Turn in Progress...</p>
                        </div>
                    )}
                </Container>
            ) : (
                <div>
                    <ResultsScreen user={user} opponent={opponent} monster={monster} oppMon={oppMon} health={health} oppHealth={oppHealth} />
                </div>
            )}
        </div>
    )
}

export default BattlePage