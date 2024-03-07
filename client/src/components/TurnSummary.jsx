import React from "react"
import Container from "react-bootstrap/Container"
import Button from "react-bootstrap/Button"

function TurnSummary({ playerMove, oppMove, oppHealth, playerHealth, updatePlayerHealth, updateOppHealth }) {

    function handleTurn() {
        console.log(playerMove)
        console.log(oppMove)
        console.log(playerHealth)
        console.log(oppHealth)

        const new_health = parseInt(health) - parseInt(oppMove.move.damage)
        const new_opp_health = parseInt(oppHealth) - parseInt(move.move.damage)

        let playerChanceToHit = (Math.floor(Math.random() * 100))
        let oppChanceToHit = (Math.floor(Math.random() * 100))
        let playerChanceToHitUpdate = playerChanceToHit + (playerMove.move.accuracy * 60)
        let oppChanceToHitUpdate = oppChanceToHit + (oppMove.move.accuracy * 60)
        console.log("Player % to hit, need 60 or higher")
        console.log(playerChanceToHit)
        console.log(playerMove.move.accuracy)
        console.log(playerChanceToHitUpdate)
        console.log("Computer % to hit, need 60 or higher")
        console.log(oppChanceToHit)
        console.log(oppMove.move.accuracy)
        console.log(oppChanceToHitUpdate)


        if (playerChanceToHitUpdate >= 60) {
            playSound({ id: playerMove.move.name })
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
        </>
    )
}
export default TurnSummary