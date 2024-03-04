import React from "react"
import { Link } from "react-router-dom"

function MonsterPickDetails({ monster, handleMonsterSelect }) {

    function handleClick(monster) {
        handleMonsterSelect(monster)
    }

    return (
        <div>
            <li className="card">
                <div className="card_content">
                    <Link to={`/battles`}>
                        <img src={monster.image} data-bs-dismiss="modal" onClick={handleClick} />
                    </Link>
                    <p>{monster.type}</p>
                </div>
            </li>
        </div>
    )
}
export default MonsterPickDetails