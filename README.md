# **Welcome to Super Original Monster Battler!**
## Owner: Jeffrey Davis
## **Short Description**
The user will be able to pick 1 of 3 monsters to battle another monster!
## **Domain Model**
![Domain Model](https://imgur.com/nTDwq8t.png)
## **ERD**
![ERD](https://imgur.com/Z0kRwQy.png)
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
![React Components Tree](https://imgur.com/uUI3YsE.png)
## **MVP**
C - User, Battle, Monster\
R - User, Monster, Move\
U - User\
D - User
## **Backend**
### Models
- User
    - Relationships
        - A `User` has many `Monsters` and `Battles`
    - Validations
        - Must have `username` that is of type string, and `computer` that is of type boolean
- Battle
    - Relationships
        - A `Battle` has many `Users`
    - Validations
        - Must have `complete` of type bool
- Monster
    - Relationships
        - A `Monster` has many `Moves`
        - A `Monster` belongs to a `User`
    - Validations
        - Must have a `name` of type string, `type` of type string, `health` of type integer, `image` of type string, and an optional `nickname` of type string
- Move
    - Relationships
        - A `Move` has many `Monsters`
    - Validations
        - Must have a `name` of type string, `damage` of type integer, `accuracy` of type float, and `type` of type string

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

```
GET /battle_users
POST /battle_users
```

```
GET /battle_users/<int:id>
PATCH /battle_users/<int:id>
DELETE /battle_users/<int:id>
```

```
GET /monster_moves
POST /monster_moves
```

```
GET /monster_moves/<int:id>
PATCH /monster_moves/<int:id>
DELETE /monster_moves/<int:id>
```

## **Features to Add Later**
- Incoprorate animation with the moves
- Make `type` have an affect on damage
- Add an additional class `Item` that would have a many-to-many relationship with `User`
- Make a free roam area