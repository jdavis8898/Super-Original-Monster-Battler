import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";


function NavBar() {

    return (
        <header>
            <Link
                to="/">
                <h3>
                    Home
                </h3>
            </Link>
        </header>
    )
}

export default NavBar