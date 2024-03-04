import React from "react"
import MonsterPickDetails from "./MonsterPickDetails"

function MonsterPick({ monsters, handleMonsterSelect }) {

    function handleSelect(monster) {
        handleMonsterSelect(monster)
    }

    return (
        <>
            {monsters.length ? (
                <ul className="pick_monster_cards">
                    {monsters.map(monster => <MonsterPickDetails key={monster.id} monster={monster} handleMonsterSelect={handleSelect} />)}
                </ul>
            ) : (
                <p>No monsters to display.  Please go to the "View All Monsters" section on the home page to select a monster to battle with.</p>
            )}
        </>
    )
}
export default MonsterPick