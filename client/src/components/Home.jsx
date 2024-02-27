import React, { useEffect, useState } from "react"
import { Link, Routes, Route } from "react-router-dom"

function Home({ user, onLogin, onLogOut }) {

    return (
        <>
        {user ? (
            <div>
                <h1>Super Original</h1>
                <h1>Monster Battler</h1>
                <div className="menu">
                    <Link
                        to="/battle">
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
                    <p>Logout</p>
                </div>
            </div>
        ) : (
            <div>
                <Login onLogin={onLogin} />
            </div>
        )}
        </>
    )
}

export default Home