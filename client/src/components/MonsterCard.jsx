import React, { useEffect, useState } from "react";
import { Link, Route } from "react-router-dom";

function MonsterCard({ monster }) {

    return (
        <div>
            <li className="card">
                <div className="card_content">
                    <h4 className="card_title">{monster.name}</h4>
                    <Link to={`/monsters/${monster.id}`}>
                        <img src={monster.image} />
                    </Link>
                    <p>{monster.type}</p>
                </div>
            </li>
        </div>
    )
}

export default MonsterCard