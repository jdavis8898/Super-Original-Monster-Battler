import React from "react"
import Button from "react-bootstrap/Button"
import Container from "react-bootstrap/Container"


function Logout({ onLogout }) {

    function handleLogout() {
        fetch("/logout", {
            method: "DELETE",
        }).then(() => onLogout())
    }

    return (
        <Button onClick={handleLogout} className="bad_button">Logout</Button>
    )
}



export default Logout