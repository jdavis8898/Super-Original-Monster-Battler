import React, { useEffect, useState } from "react"
import { Routes, Route } from "react-router-dom"
import NavBar from "./NavBar"
import Login from "./Login"
import Home from "./Home"
import BattlePage from "./BattlePage"
import MonstersPage from "./MonstersPage"
import ProfilePage from "./ProfilePage"
import MonsterDetails from "./MonsterDetails"
import Signup from "./Signup"

function Main() {
    const [user, setUser] = useState(null)
    const [opponent, setOpponent] = useState({})
    const [monster, setMonster] = useState({})

    useEffect(() => {
        fetch('/check_session')
            .then((resp) => {
                if (!resp.ok) {
                    throw new Error('Session check failed')
                }
                return resp.json()
            })
            .then((user) => setUser(user))
            .catch(() => setUser(null))
    }, [])

    function filterComputer(u) {
        if (u.computer === true) {
            return u
        }
    }

    function randomInt(x) {
        return Math.floor(Math.random() * x)
    }

    useEffect(() => {
        fetch("/users")
            .then(resp => resp.json())
            .then(usersData => {
                const filteredUsers = usersData.filter(u => filterComputer(u))
                setOpponent(filteredUsers[randomInt(filteredUsers.length)])
            })
    }, [])

    function onLogin(user) {
        setUser(user)
    }

    function onLogout() {
        setUser(null)
    }

    function createBattle() {
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
            .catch(error => {
                console.error("Error creating new battle", error)
            })
    }

    function completeBattle(id) {

        fetch(`/battles/${id}`,
            {
                method: "PATCH",
                headers:
                {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ complete: true })
            })
            .then(resp => resp.json())
    }

    function deleteUser(id) {
        fetch(`/users/${id}`, {
            method: "DELETE"
        }).then(resp => resp.json())

        fetch("/logout", {
            method: "DELETE",
        }).then(() => onLogout())

    }

    function updateUsername(id, username) {
        fetch(`/users/${id}`,
            {
                method: "PATCH",
                headers:
                {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ username: username })
            })
            .then(resp => resp.json())
            .then(updatedUser => setUser(updatedUser))
    }

    function handleMonsterSelect(mon) {
        setMonster(mon)
        console.log(mon)
    }

    return (
        <div>
            <NavBar />
            <Routes>
                <Route
                    path="/"
                    element={<Home user={user} onLogin={onLogin} onLogout={onLogout} handleMonsterSelect={handleMonsterSelect} makeOpp={makeOpp} />}
                />
                <Route
                    path="/login"
                    element={<Login onLogin={onLogin} />}
                />
                <Route
                    path="/signup"
                    element={<Signup />}
                />
                <Route
                    path="/battles"
                    element={<BattlePage user={user} opponent={opponent} updateBattle={completeBattle} monster={monster} />}
                />
                <Route
                    path="/monsters"
                    element={<MonstersPage />}
                />
                <Route
                    path="/monsters/:id"
                    element={<MonsterDetails user={user} updateUser={onLogin} />}
                />
                <Route
                    path="/profile"
                    element={<ProfilePage user={user} deleteUser={deleteUser} updateUsername={updateUsername} />}
                />
            </Routes>
        </div>
    )
}

export default Main