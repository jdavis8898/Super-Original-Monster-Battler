import React from "react"
import MonsterPickDetails from "./MonsterPickDetails"

function MonsterPick({ monsters, handleMonsterSelect, makeOpp }) {

    return (
        <>
            {monsters.length ? (
                <ul className="pick_monster_cards">
                    {monsters.map(monster => <MonsterPickDetails key={monster.id} monster={monster} handleMonsterSelect={handleMonsterSelect} makeOpp={makeOpp} />)}
                </ul>
            ) : (
                <p>No monsters to display.  Please go to the "View All Monsters" section on the home page to select a monster to battle with.</p>
            )}
        </>
    )
}
export default MonsterPick