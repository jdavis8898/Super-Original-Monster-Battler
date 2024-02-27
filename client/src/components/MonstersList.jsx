import React, { useEffect, useState } from "react";
import { Route } from "react-router-dom";
import MonsterCard from "./MonsterCard"

function MonstersList({ monsters }) {

    return (
        <div>
            <ul className="all_monsters_card">
                {monsters.map(monster => <MonsterCard key={monster.id} monster={monster} />)}
            </ul>
        </div>
    )
}

export default MonstersList