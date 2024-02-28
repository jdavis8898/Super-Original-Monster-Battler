import React, { useEffect, useState } from "react"
import { Link, Routes, Route } from "react-router-dom"
import Login from "./Login"
import Logout from "./Logout"

function Home({ user, onLogin, onLogout }) {
    const [battle, setBattle] = useState({})

    function handleClick() {
        const new_battle =
        {
            complete: false
        }

        fetch("/battles", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(new_battle)
        })
            .then(resp => resp.json())
            .then(newBattleData => setBattle(newBattleData))
            .catch(error => {
                console.error("Error creating new battle", error)
            })

    }

    return (
        <>
            {user ? (
                <div>
                    <h1>Super Original</h1>
                    <h1>Monster Battler</h1>
                    <div className="menu">
                        <Link
                            to="/battles"
                            onClick={handleClick}>
                            <p>Start Battle</p>
                        </Link>
                        <Link
                            to="/monsters">
                            <p>View All Monsters</p>
                        </Link>
                        <Link
                            to="/profile">
                            <p>Profile</p>
                        </Link>
                        <Logout onLogout={onLogout} />
                    </div>
                </div >
            ) : (
                <div>
                    <Login onLogin={onLogin} />
                </div>
            )
            }
        </>
    )
}

export default Home