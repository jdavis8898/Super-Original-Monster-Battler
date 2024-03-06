import React, { useState } from "react"
import { Link } from "react-router-dom"
import Button from "react-bootstrap/Button"
import Form from "react-bootstrap/Form"
import MonstersList from "./MonstersList"
import MonsterCard from "./MonsterCard"

function ProfilePage({ user, deleteUser, updateUsername }) {
    const [username, setUsername] = useState("")
    const [editing, setEditing] = useState(false)
    const [monsters, setMonsters] = useState(user.monsters)

    function handleUsernameEdit() {
        setEditing(!editing)
    }

    function handleSubmit() {
        updateUsername(user.id, username)
        setEditing(!editing)
    }

    function handleClick() {
        deleteUser(user.id)
    }

    return (
        <div className="profile_page">
            <h1>Welcome To Your Profile Page {user.username}!</h1>

            {editing ? (
                <Form onSubmit={handleSubmit}>
                    <Form.Label as="h4">Update Username</Form.Label>

                    <Form.Group controlId="formUpdateUsername">
                        <Form.Label>New Username: </Form.Label>
                        <Form.Control type="text" placeholder="Enter new username" value={username}
                            onChange={e => setUsername(e.target.value)} />
                    </Form.Group>
                    <Button variant="primary" type="submit" className="profile_button">Submit</Button>
                </Form>
            ) : (
                <div>
                    <h3>Your Team!</h3>
                    <MonstersList monsters={monsters} />
                    <Button variant="primary" type="button" className="profile_button" onClick={() => handleUsernameEdit()}>Update Username</Button>
                    <Link to="/login">
                        <Button variant="primary" type="button" className="bad_button" onClick={() => handleClick()}>Delete Account</Button>
                    </Link>
                </div>
            )}
        </div>
    )
}

export default ProfilePage