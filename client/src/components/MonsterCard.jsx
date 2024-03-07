import React from "react"
import { Link } from "react-router-dom"

function MonsterCard({ monster }) {

    return (
        <div>
            <li className="card">
                <div className="card_content">
                    <h4 className="card_title">{monster.name}</h4>
                    <Link to={`/monsters/${monster.id}`}>
                        <img src={monster.image} />
                    </Link>
                </div>
            </li>
        </div>
    )
}

export default MonsterCard