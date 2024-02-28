import React, { useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";
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

    function onLogin(user) {
        setUser(user)
    }

    function onLogout() {
        setUser(null)
    }

    return (
        <div>
            <NavBar />
            <Routes>
                <Route
                    path="/"
                    element={<Home user={user} onLogin={onLogin} onLogout={onLogout} />}
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
                    path="/battle"
                    element={<BattlePage user={user} />}
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
                    element={<ProfilePage user={user} />}
                />
            </Routes>
        </div>
    )
}

export default Main