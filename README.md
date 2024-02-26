# **Welcome to Super Original Monster Battler!**
## Owner: Jeffrey Davis
## **Short Description**
The user will be able to pick 1 of 3 monsters to battle another monster!
## **Domain Model**
![Domain Model](https://imgur.com/fdvuG4M.png)
## **ERD**
![ERD](https://imgur.com/hoZ5QTF.png)
## **Wireframes**
****Main Menu****
![Main Menu Wireframe](https://imgur.com/PCDZqhE.png)
****Battle Screen****
![Battle Screen Wireframe](https://imgur.com/PWFcpVc.png)
****View All Monsters Screen****
![View All Monsters Page Wireframe](https://imgur.com/xXCYnvG.png)
****Monster Details Page****
![Monster Details Page Wireframe](https://imgur.com/6uUYLDI.png)
## **React Components Tree**
![React Components Tree](https://imgur.com/NM04eQk.png)
## **MVP**
C - User, Battle, Monster\
R - User, Battle, Monster, Move\
U - User\
D - User
## **Backend**
### Models
- User
    - Relationships
        - A `User` has many `Monsters` and `Battles`
    - Validations
        - Must have `name` that is of type string, and `computer` that is of type boolean
- Battle
    - Relationships
        - A `Battle` has many `Users`
    - Validations
        - Must have `user_turn` of type bool and `complete` of type bool
- Monster
    - Relationships
        - A `Monster` has many `Moves`
        - A `Monster` belongs to a `User`
    - Validations
        - Must have a `name` of type string, `type` of type string, `health` of type integer, and an optional `nickname` of type string
- Move
    - Relationships
        - A `Move` has many `Monsters`
    - Validations
        - Must have a `name` of type string, `damage` of type integer and `type` of type string

## **Controllers**
API routes
RESTful conventions

```
GET /users
POST /users
```

```
GET /users/<int:id>
PATCH /users/<int:id>
DELETE /users/<int:id>
```

```
GET /battles
POST /battles
```

```
GET /battles/<int:id>
PATCH /battles/<int:id>
DELETE /battles/<int:id>
```

```
GET /monsters
POST /monsters
```

```
GET /monsters/<int:id>
PATCH /monsters/<int:id>
DELETE /monsters/<int:id>
```

```
GET /moves
POST /moves
```

```
GET /moves/<int:id>
PATCH /moves/<int:id>
DELETE /moves/<int:id>
```

## **Stretch Goals**
- Incoprorate sound and/or animation with the moves
- Make a free roam area
- Make `type` have an affect on damage
- Add an additional class `Item` that would have a many-to-many relationship with `User`

## **Timeline**
- Wednesday (2/21): Have backend done by afternoon
- Monday (2/26): Have MVP completed by end of day
- Week of 2/25: Work on stretch goals