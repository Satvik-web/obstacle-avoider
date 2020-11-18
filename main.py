input.onButtonPressed(Button.A, function () {
    Bird.change(LedSpriteProperty.Y, 1)
})
input.onButtonPressed(Button.B, function () {
    Bird.change(LedSpriteProperty.Y, -1)
})
let Tick = 0
let Bird: game.LedSprite = null
game.setScore(0)
let index_2 = 0
Bird = game.createSprite(0, 2)
let Obstacle: game.LedSprite[] = []
let Empty_Obstacle_Y = randint(0, 4)
Bird.set(LedSpriteProperty.Blink, 200)
for (let index_22 = 0; index_22 <= 4; index_22++) {
    if (index_22 != Empty_Obstacle_Y) {
        Obstacle.push(game.createSprite(4, index_22))
    }
}
basic.forever(function () {
    while (Obstacle.length > 0 && Obstacle[0].get(LedSpriteProperty.X) == 0) {
        Obstacle.removeAt(0).delete()
    }
    for (let Obstacle_1 of Obstacle) {
        Obstacle_1.change(LedSpriteProperty.X, -1)
    }
    if (Tick % 1 == 0) {
        Empty_Obstacle_Y = randint(0, 4)
        for (let index_22 = 0; index_22 <= 4; index_22++) {
            if (index_22 != Empty_Obstacle_Y) {
                Obstacle.push(game.createSprite(4, index_22))
            }
        }
    }
    for (let Obstacle_2 of Obstacle) {
        if (Obstacle_2.get(LedSpriteProperty.X) == Bird.get(LedSpriteProperty.X) && Obstacle_2.get(LedSpriteProperty.Y) == Bird.get(LedSpriteProperty.Y)) {
            game.gameOver()
        }
    }
    Tick += 1
    basic.pause(1000)
})
