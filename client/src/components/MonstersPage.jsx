import React, { useEffect, useState } from "react"
import MonstersList from "./MonstersList"

function MonstersPage() {
    const [monsters, setMonsters] = useState([])

    function checkOwner(monster) {
        if (monster.user_id === null) {
            return monster
        }
    }

    useEffect(() => {
        fetch("/monsters")
            .then(resp => resp.json())
            .then(monsterData => {
                setMonsters(monsterData)
            })
    }, [])

    const filteredMonsters = monsters.filter(monster => checkOwner(monster))

    return (
        <div>
            <MonstersList monsters={filteredMonsters} />
        </div>
    )
}

export default MonstersPage