import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function MoveDetails({ move }) {

    return (
        <ol>
            <li>{move.move.name}</li>
            <li>{move.move.type}</li>
            <li>{move.move.damage}</li>
        </ol>
    )
}

export default MoveDetails