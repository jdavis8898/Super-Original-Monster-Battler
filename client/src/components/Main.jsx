import React, { useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";
import NavBar from "./NavBar"
import Login from "./Login"
import Home from "./Home"
import BattlePage from "./BattlePage"
import MonstersPage from "./MonstersPage"
import ProfilePage from "./ProfilePage"

function Main() {

    return (
        <div>
            <NavBar />
            <Routes>
                <Route
                    path="/"
                    element={<Home />}
                />
            </Routes>
        </div>
    )
}

export default Main