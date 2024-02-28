import React, { useEffect, useState } from "react"
import { Link, Route } from "react-router-dom"
import UserSide from "./UserSide"
import OpponentSide from "./OpponentSide"

function BattleScreen({ user, opponent }) {

    return (
        <div>
            <p>{user.username}</p>
            <UserSide user={user} />
            <OpponentSide opponent={opponent} />
        </div>
    )
}

export default BattleScreen