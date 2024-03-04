import React from "react"

function ResultsScreen({ user, opponent, monster, oppMon, health, oppHealth }) {

    return (
        <>
            {health <= 0 ? (
                <div>
                    <h3>You Lose</h3>
                </div>
            ) : (
                <div>
                    <h3>You Win!</h3>
                </div>
            )}
            <p>To return to the home screen, please click on "Home" in the top left</p>
        </>
    )
}

export default ResultsScreen