import React from "react"
import Container from "react-bootstrap/Container"
import Button from "react-bootstrap/Button"
// import Modal from "react-bootstrap/Modal"
import { Link } from "react-router-dom"
import Login from "./Login"
import Logout from "./Logout"
import MonsterPick from "./MonsterPick"

function Home({ user, onLogin, onLogout, handleMonsterSelect, makeOpp }) {

    return (
        <Container>
            {user ? (
                <div>
                    <h1>Super Original</h1>
                    <h1>Monster Battler</h1>
                    <div className="menu">
                        <Button type="button" data-bs-toggle="modal" data-bs-target="#monstersModalCenter">
                            Battle!
                        </Button>

                        <div class="modal fade" id="monstersModalCenter" tabindex="-1" role="dialog" aria-labelledby="monstersModalCenterTitle" aria-hidden="true">
                            <div class="modal-dialog modal-dialog-centered" role="document">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="monstersModalLongTitle">Select Your Partner</h5>
                                        <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
                                            <span aria-hidden="true">&times;</span>
                                        </button>
                                    </div>
                                    <div class="modal-body">
                                        <MonsterPick monsters={user.monsters} handleMonsterSelect={handleMonsterSelect} makeOpp={makeOpp} />
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    </div>
                                </div>
                            </div>
                        </div>
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
            )}
        </Container>
    )
}

export default Home