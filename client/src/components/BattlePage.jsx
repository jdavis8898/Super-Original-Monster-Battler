import React, { useState, Suspense } from "react"
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
    const [oppMonMove, setOppMonMove] = useState({})
    const [playerMove, setPlayerMove] = useState({})

    const [playSound] = useSound(SOMB_Moves, {
        interrupt: true,
        sprite: {
            "Fire Throw": [1000, 3000],
            "Water Throw": [5000, 2000],
            "Leaf Throw": [9000, 2000],
            "Cut": [13000, 2000]
        }
    })

    function setMoves(move) {
        let randomNum = Math.floor(Math.random() * 2)
        setOppMonMove(oppMon.moves[randomNum])

        setPlayerMove(move)
    }

    function updatePlayerHealth() {
        setHealth()
    }

    function updateOppHealth() {
        setOppHealth()
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
                            {monster.moves.map(move => <MoveCard key={move.id} move={move} handleMoveSelect={setMoves} />)}
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