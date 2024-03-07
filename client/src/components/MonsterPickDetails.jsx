import React from "react"
import { Link } from "react-router-dom"

function MonsterPickDetails({ monster, handleMonsterSelect, makeOpp }) {

    function handleClick(mon) {
        handleMonsterSelect(mon)
    }

    return (
        <div>
            <li className="card">
                <div className="card_content">
                    <Link to={`/battles`}>
                        <img src={monster.image} data-bs-dismiss="modal" onClick={handleClick(monster)} />
                    </Link>
                    <p>{monster.type}</p>
                </div>
            </li>
        </div>
    )
}
export default MonsterPickDetails