import React, { useState, useEffect } from "react"
import { Link } from "react-router-dom"
import Form from "react-bootstrap/Form"
import Button from "react-bootstrap/Button"
import Container from "react-bootstrap/Container"

function Signup() {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")


    function handleSubmit(e) {
        e.preventDefault()

        const new_user =
        {
            username: username,
            password: password,
            computer: false
        }

        fetch("/users", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(new_user)
        })
            .then(resp => {
                if (resp.ok) {
                    return resp.json()
                } else if (resp.status === 400 || resp.status === 401 || resp.status === 500) {
                    throw new Error("Invalid username or password")
                }
            })
            .then(user => {
                window.alert("Sign up Successful! Please log in")
                setUsername("")
                setPassword("")
            })
            .catch(error => {
                if (error.message === "Invalid username or password") {
                    window.alert("Invalid username or password. Please try again.")
                }
            })
    }
    return (
        <Container>
            <Form onSubmit={handleSubmit}>
                <Form.Label as="h2">Signup</Form.Label>

                <Form.Group className="mb-3" controlId="formGroupEmail">
                    <Form.Label>Username</Form.Label>
                    <Form.Control type="text" placeholder="Enter username"
                        onChange={e => setUsername(e.target.value)}
                        value={username}
                    />
                </Form.Group>

                <Form.Group className="mb-3" controlId="formBasicPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" placeholder="Enter password"
                        onChange={e => setPassword(e.target.value)}
                        value={password}

                    />
                </Form.Group>
                <Button variant="primary" type="submit">Submit</Button>
            </Form>
            Already a member?
            <Link to={"/"}>
                <Button variant="link">Login</Button>
            </Link>

        </Container>
    )
}

export default Signup